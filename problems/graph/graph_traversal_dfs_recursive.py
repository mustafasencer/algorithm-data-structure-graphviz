from collections import defaultdict


class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def add_edge(self, u, v) -> None:
        self.graph[u].append(v)

    def _dfs_util(self, v, visited) -> None:
        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                self._dfs_util(i, visited)

    def dfs(self, v) -> None:
        visited = [False] * (len(self.graph))
        self._dfs_util(v, visited)


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    g.dfs(2)
