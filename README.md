# tsp-aco
Travelling salesman problem indeterministic solution using ant colony optimization technique.

### Dataset
The dataset directory contains the input files and the optimal solution of two datasets. The input file is a list of different locations (nodes), each line describe a single node as two real numbers, x and y, which represent the coordinates of this node.

### converter
Convert a dataset file from euclidean distance format to graph format. The input file is a list of coordinates of different nodes. The output file represents a fully connected graph as a list of edges. Each line of the output file describes a single edge as three numbers, u the source node, v the destination node, and d the distance between them.

### model
This file exports two helper classes for used as data wrappers, a graph data structure, and an ant.

### loader
Exports a function that loads the graph into a graph data structure as defined in model

### aco
This is the main script that contains the bulk of the logic.

### How to use
The main driver script is main, it expects an input file in the same directory with the name 'in.txt'. Simply, run main (using python 3) and pass any of the following optional cmd parameters:
- '--itr': number of iterations
- '--ants' : number of ants
- '--alpha' : alpha constant
- '--beta' : beta constant
- '--evp' : evaporation rate
- '--q' : q constant