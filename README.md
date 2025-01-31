# Summary of the Greedy Heuristic Code:

This Python script implements a graph-based heuristic algorithm to find the Minimum Dominating Set (MDS) in a given network. The MDS is a subset of nodes such that every node in the graph is either in this set or adjacent to a node in the set. The script constructs a graph, applies heuristics to find an optimal solution, and evaluates the computational efficiency of the approach.

# Key Components of the Code:

1. Graph Construction:

  a. Reads an adjacency matrix from a CSV file.
  b. Uses NetworkX to create an undirected graph (G2) from the matrix.
  c. Implements custom graph functions (add_vertex(), add_edge(), print_graph()) to store and manipulate graph data.

# Graph Representation & Initialization:

  1. The graph is represented as an adjacency list where each node has an edge weight.
  2. The adjacency matrix is parsed, and edges are added between connected nodes.
  3. The graph is visualized using nx.draw_circular().

# Heuristic Algorithm for MDS:

1. A greedy heuristic approach is used to determine a near-optimal Minimum Dominating Set (MDS).
2. The function heuristics():
  a. Selects the node with the highest degree (most connections).
  b. Adds it to the dominating set.
  c. Removes its neighbors from the graph to prevent redundancy.
  d. Repeats the process until all nodes are covered.
3. The final MDS is printed, along with its cardinality (size of the set).
# Performance Evaluation:

1. Measures the execution time of the heuristic algorithm.
2. Outputs the final MDS solution and its computation time.

# Summary of the Stochastic Local Search Algorithm:
This Python script implements a graph-based local search algorithm to find the Minimum Dominating Set (MDS) in a given network. The Minimum Dominating Set is a subset of nodes such that every node in the graph is either in this set or adjacent to a node in the set. The script constructs a graph, applies local search optimization, and evaluates computational efficiency.

# Key Components of the Code:
1. Graph Construction:

  a. Loads an adjacency matrix from a CSV file.
  b. Constructs an undirected graph (G2) using NetworkX.
  c. Identifies edges between connected nodes and visualizes the graph.

# Computation of Minimum Dominating Set (MDS):

1. Degree-Based Node Selection:
  a. Determines node degrees (number of connections).
  b. Sorts nodes based on their connectivity to identify key influencers.

2. Iterative Node Selection:
  a. Uses a greedy heuristic to iteratively select the most influential nodes.
  b. Removes covered nodes to minimize redundancy.

3. Local Search Optimization:
  a. Evaluates coverage using an objective function.
  b. Swaps nodes to refine the solution and minimize the dominating set size.

# Performance Evaluation:

1. The final Minimum Dominating Set (MDS) is printed along with its cardinality (size).
2. Execution time is calculated to measure computational efficiency.
