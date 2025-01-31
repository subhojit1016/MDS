import time

startTime = time.time()

import pandas as pd

import networkx as nx

import copy


def add_vertex(v):
    global graph
    global vertices_no
    global vertices
    if v in vertices:
        print("Vertex ", v, " already exists")
    else:
        vertices_no = vertices_no + 1
    vertices.append(v)
    if vertices_no > 1:
        for vertex in graph:
            vertex.append(0)
    temp = []
    for i in range(vertices_no):
        temp.append(0)
    graph.append(temp)

# Add an edge between vertex v1 and v2 with edge weight e
def add_edge(v1, v2, e):
    global graph
    global vertices_no
    global vertices
    # Check if vertex v1 is a valid vertex
    if v1 not in vertices:
        print("Vertex ", v1, " does not exist.")
    # Check if vertex v1 is a valid vertex
    elif v2 not in vertices:
        print("Vertex ", v2, " does not exist.")
    # Since this code is not restricted to a directed or 
    # an undirected graph, an edge between v1 v2 does not
    # imply that an edge exists between v2 and v1
    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = e

# Print the graph
def print_graph():
  global graph
  global vertices_no
  for i in range(vertices_no):
    for j in range(vertices_no):
      if graph[i][j] != 0:
        print(vertices[i], " -> ", vertices[j], \
        " edge weight: ", graph[i][j])


def check(i,j):
    if (graph[i][j]!=0):
        return True
    else:
        return False


def second_smallest(numbers, c):
    l=copy.deepcopy(numbers)
    l.sort()
    for x in range(len(l)):
        if all(y < l[x] for y in c):
            return (l[x])
  
#second_smallest(bb, c)
def covered(arr, node_arr, G):
     
    cov=[]
    for i in range(len(arr)):
        if (arr[i] == 1):
            index_ele = node_arr[i]
            list1 = [n for n in G.neighbors(index_ele)]
            cov = cov + list1
                        #if (len(list1)>1):
            #    list1.remove(index_ele)
            
        
        
    cov = list(dict.fromkeys(cov))
    #print(cov)
    return (len(cov))
            

def countX(lst, x):
    return lst.count(x)       

  

def objective(DS_cover, arr, node_arr):
    
    fx = (DS_cover/len(node_arr)) + (1/(len(node_arr)*sum(arr)))
    return fx

def objective1(DS_cover, node_arr):
    fx1 = (DS_cover/len(node_arr))
    return fx1


def degree(arr, node_arr, G):
    deg = []
    for i in range(len(arr)):
        index_ele = node_arr[i]
        deg.append(G.degree[index_ele] - 2)
    #print(deg)
    return deg

def heuristics(arr, node_arr, G):
    if (len(node_arr)==0):
        z = arr
    else:
        maximal_count = []
        for i in range(len(node_arr)):
            index_ele = node_arr[i]
            maximal_count.append(G.degree[index_ele] - 2)
        #print(maximal_count)
        c= max(maximal_count)
        idx=maximal_count.index(c)
        element = node_arr[idx]
        arr=arr+[element]
        #print(arr)
        neighbour = [n for n in G.neighbors(element)]
        for k in range(len(neighbour)):
            G.remove_node(neighbour[k])
            node_arr.remove(neighbour[k])
        #print(node_arr)
        z = heuristics(arr, node_arr, G)
    return z
    
    

df = pd.read_csv ('C:/Users/subhojit.biswas/621_Project/621_Project_data3.csv')
print (df)
corr=df.to_numpy()


vertices = []
# stores the number of vertices in the graph
vertices_no = 0
graph = []
# Add vertices to the graph


G2 = nx.Graph()

nodes = df.columns.values

for h in range(len(nodes)):
    add_vertex(int(nodes[h]))

for h in range(len(nodes)):
    for r in range(len(nodes)):
        if (h ==r):
            add_edge(int(nodes[h]), int(nodes[r]), 0)
        else:
            if (int(nodes[h])>int(nodes[r]) and h>0):
                if ((check(int(nodes[r]), int(nodes[h])))):
                    add_edge(int(nodes[h]), int(nodes[r]), graph[int(nodes[r])][int(nodes[h])])
            else:
                add_edge(int(nodes[h]), int(nodes[r]), corr[h][r])
                #add_edge(potential_nodes[h], potential_nodes[r], random.randint(20, 100))


print_graph()
nodes_i=[]
nodes_j=[]
for i in range(len(corr)):
    for j in range(len(corr[0])):
        if (corr[i][j]==1):
            nodes_i.append(i)
            nodes_j.append(j)
            
for i,j in zip (nodes_i,nodes_j):
    G2.add_edges_from([(j, i)])   
    

    
nx.draw_circular(G2, with_labels = True, node_size = 500)

#G2.remove_node(0)

potential_nodes=list(G2.nodes())

dominating_set = []
MDS = heuristics(dominating_set, potential_nodes, G2)
print("The minimum dominating set using the heursitics " + str(MDS))
print("The cardinality of minimum dominating set using heursitics is " + str(len(MDS)))
executionTime = (time.time() - startTime)
print('Execution time in seconds for heuristics: ' + str(executionTime))    
