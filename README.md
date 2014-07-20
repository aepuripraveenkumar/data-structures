[![Build Status](https://travis-ci.org/johnshiver/data-structures.png)](https://travis-ci.org/johnshiver/data-structures)

data-structures
===============

Data structures in Python

This repository will hold sample code for a number of classic data structures implemented in Python.

resources used
===============
http://greenteapress.com/thinkpython/html/chap17.html
https://www.python.org/doc/essays/graphs/  -- for guido_graph
Introduction to Computation and Programming by Eric Grimson -- Breadth First Search
https://www.youtube.com/watch?v=05WQNgR4Urk  -- for bellman_ford algorithm
http://stackoverflow.com/questions/2592769/what-is-the-relaxation-condition-in-graph-theory - Understanding relaxing
https://www.youtube.com/watch?v=ozsuci5pIso - Lecture on bellman-ford
gist.gisthub.com/econchick/4666413 -- for Dijkstra
http://interactivepython.org/courselib/static/pythonds/Trees/balanced.html - for balanced binary tree
http://www.csanimated.com/animation.php?t=Quicksort - for quicksort

collaborations
===============
Larry Fritts

Implementaitons
===============
1. Linked list
2. Stack
3. Queue
4. Double linked list
5. Binary Heap
6. Graph
    a. Changed the edge from a list to a dictionary with keys being the other
    vertex and the value being the weight.
7. Dijkstra added to graph
8. Binary Tree
9. Balanced Binary Tree

Bellman_Ford Algo:

The reason you would choose Bellman over Dijkstra is that Bellman can be used
for graphs with negative edge values. This makes it useful for a system with
financial transactions, where it is inevitable that some investements will
return a negative number.

**Added Travis**