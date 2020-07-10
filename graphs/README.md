# Graphs

In this lesson, we’ll build a robust implementation of the graph data structure. With just two classes, Vertex and Graph, we can implement a variety of graphs that satisfy the requirements of many algorithms.

Let’s detail the functionality we require from these classes:

_Vertex_ stores some data.
_Vertex_ stores the edges to connected vertices and their weight.
_Vertex_ can add a new edge to its collection.
_Graph_ stores all the vertices.
_Graph_ knows if it is directed or undirected.
_Graph_ can add a new vertex to its collection.
_Graph_ can add a new edge between stored vertices.
_Graph_ can tell whether a path exists between stored vertices.

Since we’re dealing with multiple classes, we’ll use multiple files for this implementation. To keep the concepts grounded in a real-world application, we’ll build up a transportation network of railroads and train stations as we go.
