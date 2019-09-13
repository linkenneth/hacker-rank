from Queue import Queue

DISTANCE = 6

class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = { v: [] for v in range(n)}

    def connect(self, v1, v2):
        self.edges[v1].append(v2)
        self.edges[v2].append(v1)

    def find_all_distances(self, start):
        distances = {}
        visited = set()
        queue = Queue()
        queue.put((0, start))
        # print 'edges', self.edges
        while not queue.empty():
            # print queue
            (dist, node) = queue.get()
            if node in visited:
                continue
            visited.add(node)
            distances[node] = dist
            for neighbor in self.edges[node]:
                queue.put((dist + DISTANCE, neighbor))

        dlist = []
        for node in range(self.n):
            if node == start:
                continue
            if node in distances:
                dlist.append(str(distances[node]))
            else:
                dlist.append(str(-1))
        print ' '.join(dlist)

t = input()
for i in range(t):
    n,m = [int(x) for x in raw_input().split()]
    graph = Graph(n)
    for i in xrange(m):
        x,y = [int(x) for x in raw_input().split()]
        graph.connect(x-1,y-1)
    s = input()
    graph.find_all_distances(s-1)
