import sys, loader, utilities, aco

DEFAULT_ITR = 50
DEFAULT_ALPHA = 6
DEFAULT_BETA = 6
DEFAULT_EVP = 0.5
DEFAULT_Q = 1000

graph = loader.load('in.txt')
argMap = utilities.extractArgs(sys.argv[1:])

# print(graph.nodes, graph.edges)
# print(graph.a)
# print(graph.w)
# print(graph.p)

itr = argMap.get('--itr', DEFAULT_ITR)
ants = min(max(argMap.get('--ants', graph.nodes - 1), 1), graph.nodes)
alpha = argMap.get('--alpha', DEFAULT_ALPHA)
beta = argMap.get('--beta', DEFAULT_BETA)
evp = argMap.get('--evp', DEFAULT_EVP)
q = argMap.get('--q', DEFAULT_Q)

print('nodes ', graph.nodes)
print('edges ', graph.edges)
print('itr ', itr)
print('ants ', ants)
print('alpha ', alpha)
print('beta ', beta)
print('evp ', evp)
print('q ', q)

aco.run(graph, itr, ants, alpha, beta, evp, q)