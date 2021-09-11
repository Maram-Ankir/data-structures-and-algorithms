# Graphs

Graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges

## Challenge

- Implement Graph class

## Approach & Efficiency

- add_node: time O(1), space O(1)
- add_edge:time O(n), space O(n)
- get_nodes:time O(n), space O(n)
- get_neighbors:time O(n), space O(n)
- size:time O(1), space O(1)

## API

- add_node : adds a new node to the graph, returns the added node
- add_edge: adds new edge between two nodes, takes in two nodes, has ability to add weight
- get_node : returns all of the nodes as a collection
- get_neighbors :: returns a collection of nodes (with weights) connected to a node, takes in a node
- size : returns number of nodes in Graph; integer
