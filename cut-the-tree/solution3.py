# Iterative solution so that recursion depth problem is fixed. This is the
# one that works.

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

def subtree_sum(graph, values):
    stack = [(1, None)]  # arbitrarily use vertex 1 as root
    visited = set()
    F = {}

    while stack:
        vertex, parent = stack.pop()
        visited.add(vertex)
        children = [n for n in graph[vertex] if n != parent]
        if all(c in visited for c in children):
            F[vertex] = values[vertex] + sum(F[c] for c in children)
        else:
            stack.append((vertex, parent))
            for c in children:
                stack.append((c, vertex))

    return F

def tree_diff(F, graph, values):
    stack = [(1, None)]  # arbitrarily use vertex 1 as root
    minimum = float('inf')
    total = sum(values[v] for v in graph)

    while stack:
        vertex, parent = stack.pop()
        children = [n for n in graph[vertex] if n != parent]
        for c in children:
            minimum = min(minimum, abs(total - 2 * F[c]))
            stack.append((c, vertex))

    return minimum

def main():
    graph, values = read_input()

    F = subtree_sum(graph, values)
    print tree_diff(F, graph, values)

if __name__ == '__main__':
    main()
