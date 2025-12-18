class AdjacencyList:
    def __init__(self):
        self.tree = {}

    def add_node(self, parent, child):
        if parent not in self.tree:
            self.tree[parent] = []
        self.tree[parent].append(child)

        if child not in self.tree:
            self.tree[child] = []

    def get_children(self, node):
        return self.tree.get(node, [])

    def __repr__(self):
        return f"AdjacencyList({self.tree})"


class MaterializedPath:
    def __init__(self):
        self.paths = {}

    def add_node(self, node, path):
        self.paths[node] = path

    def __repr__(self):
        return f"MaterializedPath({self.paths})"

#Ковертация из списка смежности в материализованный путь
def adjacency_to_materialized(adj_list, root):
    mp = MaterializedPath()

    def dfs(node, path):
        mp.add_node(node, path)
        for child in adj_list.get_children(node):
            dfs(child, f"{path}/{child}")

    dfs(root, str(root))
    return mp

#Ковертация из материализованного пути в список смежности
def materialized_to_adjacency(mp):
    adj = AdjacencyList()

    for node, path in mp.paths.items():
        parts = path.split("/")
        if len(parts) > 1:
            parent = int(parts[-2])
            adj.add_node(parent, node)
        else:
            # корень
            if node not in adj.tree:
                adj.tree[node] = []

    return adj

if __name__ == "__main__":
    adj = AdjacencyList()
    adj.add_node(1, 2)
    adj.add_node(1, 3)
    adj.add_node(2, 4)
    adj.add_node(2, 5)

    print("Исходный список смежности:")
    print(adj)

    # Конвертация в материализованный путь
    mp = adjacency_to_materialized(adj, root=1)
    print("\nМатериализованный путь:")
    print(mp)

    # Обратная конвертация
    adj_restored = materialized_to_adjacency(mp)
    print("\nВосстановленный список смежности:")
    print(adj_restored)

if __name__ == "__main__":
    mp = MaterializedPath()
    mp.add_node(1, "1")
    mp.add_node(2, "1/2")
    mp.add_node(3, "1/3")
    mp.add_node(4, "1/2/4")
    mp.add_node(5, "1/2/5")

    print("Исходный материализованный путь:")
    print(mp)

    # Конвертация в список смежности
    adj = materialized_to_adjacency(mp)
    print("\nСписок смежности:")
    print(adj)

    # Обратная конвертация в материализованный путь
    mp_restored = adjacency_to_materialized(adj, root=1)
    print("\nВосстановленный материализованный путь:")
    print(mp_restored)