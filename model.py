class Graph:
  # nodes: number of nodes
  # edges: number of edges
  # a: adjList destinations
  # w: adjList weights
  # m: adjMatrix representation
  # p: edge pheremone matrix
  # d: edge desirability matrix

  def __init__(self, nodes: int, edges: int):
    self.nodes = nodes
    self.edges = edges
    self.a = []
    self.w = []
    self.m = []
    self.p = []
    self.d = []
    for x in range(nodes):
      self.a.append([])
      self.w.append([])
      self.m.append([-1.0] * nodes)
      self.p.append([0.0] * nodes)
      self.d.append([0.0] * nodes)
  
  def addEdge(self, src: int, dst: int, cst: float):
    self.a[src].append(dst)
    self.w[src].append(cst)
    self.m[src][dst] = cst

class Ant:
  # age: number of tours executed by this ant
  # home: start node
  # currentNode: current node
  # lastTour: last tour path
  # lastTourLength: last tour length

  def __init__(self):
    self.age = 0
    self.home = 0
    self.currentNode = 0
    self.lastTour = []
    self.lastTourLength = 0.0
