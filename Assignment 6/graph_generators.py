from numpy import random as r
import math

def random_graph(n):
	# generates enough vertex labels
	def lexicographic(n):
		max_length = math.ceil(math.log(n)/math.log(26))
		if n < 26:
			return [chr(i+97) for i in range(26)]
		else:
			A = []
			for i in range(26):
				A += [chr(i+97)+s for s in lexicographic(n//26)]
				if len(A) > n: break
			return lexicographic(n//26) + A

	rng = r.default_rng()
	# draws a random number of edges between 0 and n^2
	edge_count = int((n*r.random())**2)
	letters = lexicographic(n)
	graph = {letters[i]: [] for i in range(n)}
	# draws vertex pairs randomly and adds them to the adjacency list
	for i in range(edge_count):
		source = letters[rng.integers(0,n)]
		sink = letters[rng.integers(0,n)]
		graph[source].append(sink)
		graph[source] = list(set(graph[source]))
	return graph

def random_weighted_graph(n, weight_range = (1,10), negative_weights = False):
	rng = r.default_rng()
	unweighted_graph = random_graph(n)
	graph = {u: {} for u in unweighted_graph}
	for u in graph:
		for v in unweighted_graph[u]:
			w = rng.integers(weight_range[0], weight_range[1])
			graph[u][v] = w
	return graph