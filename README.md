# Algorithm-to-calculate-shortest-path-and-centrality-measures
This was a part of Team work and has been Contributed by Yash Kashiwala, Xisheng chen and Xianhong Cao.

The code written uses different data types to implement Dijkstra's Shortest path algorithm and solve various problems explained below.

#Prerequisite
The first line of the input file should contain a flag to indicate which format the file is in:
• S for a stream of arcs; or
• A for an arc-weight matrix.


The program help users to read in the graph from a file, either
• as a stream of weighted arcs {(i, j, dij ) : ij is an arc of G}; or
• as an arc-weight matrix (i.e., arc-weight array).


This program implements Dijkstra’s Shortest Path Algorithm in Python, for a directed weighted
graph with positive arc weights. For the selection set it helps to allow the user to choose between
(a) an array (the original approach used by Dijkstra), i.e., Python list; and
(b) a heap (Tarjan’s modification).
Your program gves users a choice to choose between any two types of Data structure based on input file.
##The inputs to this program should be a graph G (e.g., an array of adjacency lists), and the index
r of the root node as chosen by the user.
The output is a shortest path spanning tree rooted at r,
implemented as arrays (Python lists) p and D.

PROBLEM 1.
You have been given the job of organising the annual Roller-blading Race in Ballyskate. The
network in Figure 1 below shows the layout of Ballyskate, with streets being edges and street
junctions being vertices. The number on each street represents its length in hundreds of metres.
There are no one-way streets. The street 4-9 has a bridge over the street 3-5.
You must set up a viewing podium for the Mayor and his grandmother at vertex p. Unfortunately,
the materials for the podium are all located at the race’s start vertex. Since you will have several
trips transporting the materials before starting your work, you wish to minimise the total distance
you have to travel from vertex 1 to vertex p, and find a shortest path from 1 to p.

![image](https://user-images.githubusercontent.com/71339403/94329097-be94bd80-ffaf-11ea-944d-07bf0916019d.png)

PROBLEM 2.
. Padgett’s data on marriage alliances among leading Florentine families in the later
Renaissance1
are given in Figure 2. There, each node is a family, and each edge denotes a connection
by marriage.
For each node, compute the following measures of centrality, using your shortest path program:
• Closeness centrality
• Betweenness centrality
Also calculate the degree centrality and eigenvector centrality of each node. All of the centrality
measures should be normalised (relative) centrality measures.



