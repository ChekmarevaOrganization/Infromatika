from collections import deque

class Graph:
    def __init__(self):
        self.edges = {}

    def add_vertex(self, vertex):
        if vertex not in self.edges:
            self.edges[vertex] = []

    def add_edge(self, ver1, ver2):
        self.add_vertex(ver1)
        self.add_vertex(ver2)

        self.edges[ver1].append(ver2)
        self.edges[ver2].append(ver1)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        visited.add(start)

        while queue:
            vertex = queue.popleft()
            result.append(vertex)

            for neighbor in sorted(self.edges[vertex]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return ''.join(result)

    def dfs(self, start):
        visited = set()
        result = []

        def dfs_recursive(vertex):
            visited.add(vertex)
            result.append(vertex)

            for neighbor in sorted(self.edges[vertex]):
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return ''.join(result)

graph = Graph()
for ver in ["A", "B", "C", "D", "E", "F", "G", "H"]:
    graph.add_vertex(ver)

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("B", "E")
graph.add_edge("C", "F")
graph.add_edge("C", "G")
graph.add_edge("D", "H")


print("\nСтруктура графа:")
for vertex in sorted(graph.edges.keys()):
    neighbors = graph.edges[vertex]
    print(f"{vertex}: {neighbors}")

bfs_result = graph.bfs("A")
dfs_result = graph.dfs("A")

print(f"Поиск в ширину: {bfs_result}")
print(f"Поиск в глубину: {dfs_result}")