def find_subtree_sum(graph, values, vertex=1, parent=None, F=None, visited=None):
	if not F:
		F = {}
	if not visited:
		visited = set()

	visited.add(vertex)

	neighbors = graph[vertex]
	for neighbor in neighbors:
		if neighbor in visited:
			continue
		find_subtree_sum(graph, values, vertex=neighbor, parent=vertex,
						 F=F, visited=visited)
	F[vertex] = values[vertex] + sum(F[neighbor] for neighbor in neighbors
									 if neighbor is not parent)

def find_tree_diff(graph, values, F, vertex=1, visited=None, current=0, _min=0):
	if not visited:
		visited = set()
	if not current:
		current = values[vertex]

	visited.add(vertex)

	for neighbor in graph[vertex]:
		_min = min(_min, abs(current - F[neighbor]))

	for neighbor in graph[vertex]:
		if neighbor in visited:
			continue
		_min = find_tree_diff(graph, values, F, vertex=neighbor,
							  current=current + values[neighbor],
							  _min=_min)
	return _min

def main():
	graph = {}
	values = {}
	N = int(raw_input())
	v_list = map(int, raw_input().split())
	for n in xrange(1, N + 1):
		graph[n] = []
		values[n] = v_list[n - 1]
	for n in xrange(N - 1):
		edge = map(int, raw_input().split())
		graph[edge[0]].append(edge[1])
		graph[edge[1]].append(edge[0])

	total_sum = sum(v_list)
	F = { 1 : values[1] }
	find_subtree_sum(graph, values, F=F)
	print F

	print find_tree_diff(graph, values, F)

if __name__ == '__main__':
	main()
