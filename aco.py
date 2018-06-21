from random import shuffle
from random import random
from functools import reduce

from model import Graph
from model import Ant

# initialize the home node for each ant in the provided list
# NOTE: the funtion modifies in the Ant objects of the provided list
def initAntsHome(colony: "list of Ant", nodes: int) -> "list of Ant":
  if(nodes < 1):
    raise Exception('aco-operators: initAntsHome: invalid number of nodes:', nodes)
  
  if(len(colony) < 1):
    raise Exception(
        'aco-operators: initAntsHome: invalid number of ants:', len(colony))

  if(len(colony) > nodes):
    raise Exception(
        'aco-operators: initAntsHome: number of ants must be less than or equal to the number of nodes:', len(colony))

  homes = list(range(nodes))
  shuffle(homes)
  for idx, ant in enumerate(colony):
    ant.home = homes[idx]
    ant.currentNode = homes[idx]

  return colony

# calculates the edge desirability for each edge in the provided graph
# using the provided coefficients
# return a Graph with the updated desirability
# NOTE: the function modifies in the provided Graph object
def updateEdgesDesirability(graph: Graph, alpha: float, beta: float) -> Graph:
  for src, neighbours in enumerate(graph.a):
    for dst in neighbours:
      graph.d[src][dst] = ((graph.p[src][dst] + 1)**alpha) * ((1 / graph.m[src][dst])**beta)

  return graph

# execute a single tour for the provided ant on the provided graph
# return an ant with its lastTour property set to a list of int
# representing the order of the graph nodes in the tour excluding the 
# start node which are always the ant home node
# NOTE: the funtion modifies in the provided Ant object
def executeAntTour(ant: Ant, graph: Graph, alpha: float, beta: float) -> Ant:
  ant.lastTour = []
  ant.lastTourLength = 0
  visited = [False] * graph.nodes
  remainingSteps = graph.nodes

  while(remainingSteps > 0):
    allowedNeighbours = []
    neighboursDesirability = []
    neighboursCumulativeProbability = [0.0]
    totalDesirability = 0.0

    for neighbour in graph.a[ant.currentNode]:
      if not visited[neighbour]:
        allowedNeighbours.append(neighbour)
        neighboursDesirability.append(graph.d[ant.currentNode][neighbour])
    
    if not allowedNeighbours:
      break

    totalDesirability = reduce(
        lambda total, value: total + value,
        neighboursDesirability,
        0.0)

    for idx, desirability in enumerate(neighboursDesirability):
      neighboursCumulativeProbability.append(
          desirability / totalDesirability + neighboursCumulativeProbability[idx])

    neighboursCumulativeProbability = neighboursCumulativeProbability[1:]
    roulette = random()
    nextNode = allowedNeighbours[-1]
    
    for idx, probability in enumerate(neighboursCumulativeProbability):
      if(roulette < probability):
        nextNode = allowedNeighbours[idx]
        break
    
    visited[nextNode] = True
    ant.lastTour.append(nextNode)
    ant.lastTourLength += graph.m[ant.currentNode][nextNode]
    ant.currentNode = nextNode
    remainingSteps -= 1

  return ant

# update the pheremone score of each edge after the evaporation
# NOTE: the function modifies in the provided Graph object
def evpPheremone(graph: Graph, evp: float) -> Graph:
  for src, neighbours in enumerate(graph.a):
    for dst in neighbours:
      graph.p[src][dst] *= (evp)

  return graph

# increment the pheremone score of the edges visited by the provided 
# ant in its last tour
# return a graph object with the pheremone matrix updated
# NOTE: the function modifies in the provided Graph object
def depositPheremone(ant: Ant, graph: Graph, q: float) -> Graph:
  antTour = [ant.home] + ant.lastTour
  deltaPheremone = q / ant.lastTourLength
  for idx in range(len(antTour) - 1):
    node, nextNode = antTour[idx], antTour[idx + 1]
    graph.p[node][nextNode] += deltaPheremone
    graph.p[nextNode][node] += deltaPheremone

  return graph

# the main entry point, it runs the aco on the provided graph given
# provided optmization parameters
# return a list of int representing the best tour, and a Graph object
# with the optimized pheremone score
# NOTE: the function modifies in the provided Graph object
def run(graph: Graph,
        itr: int,
        ants: int,
        alpha: float,
        beta: float,
        evp: float,
        q: float) -> ("list of Ant", Graph):

  colony = []
  for x in range(ants):
    colony.append(Ant())

  colony = initAntsHome(colony, graph.nodes)
  updateEdgesDesirability(graph, alpha, beta)

  for i in range(itr):
    for ant in colony:
      executeAntTour(ant, graph, alpha, beta)
    
    evpPheremone(graph, evp)

    for ant in colony:
      depositPheremone(ant, graph, q)
    
    updateEdgesDesirability(graph, alpha, beta)

  return (colony, graph)
