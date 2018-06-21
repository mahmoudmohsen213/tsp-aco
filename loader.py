# Input file structure:

# The first line contains exactly two integers n the number of nodes and m the 
# number of edges.

# Follow, m lines, each line represent and edge and contains exactly three 
# integers u the source node, v the destination node, and c the edge weight.

# The file is processed as an undirected graph, that is, a line with the contents
# "u v c" represents an edge from u to v with weight c, and also an edge from v
# to u with weight c.
# ==============================================================================

from model import Graph

# load a txt file into an adjacency list graph
def load(fileName: str) -> Graph:
  print('loader: load: loading graph ' + fileName + '...')
  with open(fileName, 'r') as inputFile:
    inputData = list(map(float, inputFile.read().split()))
    n, m = int(inputData[0]), int(inputData[1])

    if(n < 1):
      raise Exception('loader: load: invalid number of nodes', n)

    if(m < (n - 1)):
      raise Exception('loader: load: invalid number of edges', m)

    print(len(inputData))

    g = Graph(n, m)
    inputIndex, edgeIndex = 2, 0
    while(edgeIndex < m):
      u, inputIndex = int(inputData[inputIndex]), inputIndex + 1
      v, inputIndex = int(inputData[inputIndex]), inputIndex + 1
      c, inputIndex = inputData[inputIndex], inputIndex + 1

      if(u >= n):
        raise Exception('loader: load: invalid node id', u)

      if(v >= n):
        raise Exception('loader: load: invalid node id', v)

      g.addEdge(u, v, c)
      g.addEdge(v, u, c)
      edgeIndex += 1
      
  print('loader: load: loading graph done', g)
  return g
