def read_input():
	graph, values = {}, {}
	N = int(raw_input())
	v_list = map(int, raw_input().split())

	for n in xrange(1, N + 1):
		graph[n] = []
		values[n] = v_list[n - 1]

	for _ in xrange(N - 1):
		edge = map(int, raw_input().split())
		graph[edge[0]].append(edge[1])
		graph[edge[1]].append(edge[0])

	return graph, values

def subtree_sum(vertex, parent, graph, values, F):
	''' Finds the sum of the subtree rooted at `vertex` with parent `parent`. '''
	neighbors = graph[vertex]
	for neighbor in neighbors:
		if neighbor is parent:
			continue
		subtree_sum(neighbor, vertex, graph, values, F=F)
	F[vertex] = values[vertex] + sum(F[neighbor] for neighbor in neighbors
									 if neighbor is not parent)
	return F

def tree_diff(vertex, parent, minimum, graph, values, F, total):
	for neighbor in graph[vertex]:
		if neighbor is parent:
			continue
		minimum = min(minimum, abs(total - 2 * F[neighbor]))
	for neighbor in graph[vertex]:
		if neighbor is parent:
			continue
		minimum = min(minimum, tree_diff(neighbor, vertex, minimum,
										 graph, values, F, total))
	return minimum

def main():
	graph, values = read_input()

	F = {}
	F = subtree_sum(1, None, graph, values, F)
	total = sum(values[v] for v in graph)
	print tree_diff(1, None, float('inf'), graph, values, F, total)

if __name__ == '__main__':
	main()
