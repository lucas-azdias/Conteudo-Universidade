import numpy as np

from collections import defaultdict
from copy import deepcopy


class adj_list_graph:
    _order = None
    _size = None
    _list = None
    _is_directed = None
    _is_weighted = None


    def __init__(self, is_directed:bool=True, is_weighted:bool=True) -> None:
        self._order = 0
        self._size = 0
        self._list = defaultdict()
        self._is_directed = is_directed
        self._is_weighted = is_weighted


    def __str__(self) -> str:
        text = ""
        if self._list.items() != defaultdict().items():
                for u, edges in self._list.items():
                    text += f"{u}: "
                    for (v, weight) in edges:
                        text += f"({v}, {weight}) > " if self._is_weighted else f"({v}) > "
                    text = text.removesuffix(" > ")
                    text += "\n"
        else:
            text = "<Empty graph>"
        return text.removesuffix("\n")


    def get_order(self) -> int:
        return self._order


    def get_size(self) -> int:
        if self._is_directed:
            return self._size
        else:
            return int(self._size / 2)


    def get_data_list(self) -> defaultdict:
        return deepcopy(self._list)


    def get_data_matrix(self) -> tuple[dict, np.ndarray]:
        matrix = np.frompyfunc(list, 0, 1)(np.empty((self.get_order(), self.get_order()), dtype=object))
        nodes_index = dict()

        cur_index = 0
        for node, edges in self._list.items():
            if not node in nodes_index.keys():
                nodes_index[node] = cur_index
                cur_index += 1
            for i in range(len(edges)):
                if not edges[i][0] in nodes_index.keys():
                    nodes_index[edges[i][0]] = cur_index
                    cur_index += 1
                matrix[nodes_index[node]][nodes_index[edges[i][0]]].append(edges[i][1])
        return (nodes_index, matrix)


    def add_node(self, u:str) -> None:
        if not self.has_node(u):
            self._list[u] = list()
            self._order += 1


    def remove_node(self, u:str) -> None:
        if self.has_node(u):
            self._size -= len(self._list[u])
            self._list.pop(u)
            for node, edges in self._list.items():
                i = 0
                while i < len(edges):
                    if edges[i][0] == u:
                        self._list[node].pop(i)
                        self._size -= 1
                    else:
                        i += 1
            self._order -= 1


    def has_node(self, u:str) -> bool:
        return u in self._list.keys()


    def adjacencies_node(self, u:str) -> tuple[tuple[str, float]] | None:
        if self.has_node(u):
            return tuple(deepcopy(self._list[u]))
        else:
            return None
    

    def add_edge(self, u:str, v:str, weight:float=1.) -> None:
        self._add_directed_edge(u, v, weight)
        if not self._is_directed:
            self._add_directed_edge(v, u, weight)

    
    def remove_edge(self, u:str, v:str) -> None:
        self._remove_directed_edge(u, v)
        if not self._is_directed:
            self._remove_directed_edge(v, u)
    

    def has_edge(self, u:str, v:str) -> bool:
        if self.has_node(u) and self.has_node(v):
            for (node, _) in self._list[u]:
                if node == v:
                    return True
        return False


    def edge_weight(self, u:str, v:str) -> tuple[float] | None:
        if self.has_node(u) and self.has_node(v):
            weights = list()
            for (node, weight) in self._list[u]:
                if node == v:
                    weights.append(weight)
            return tuple(weights)
        else:
            return None

    
    def degree(self, u:str) -> int | None:
        if self.has_node(u) and self._is_directed:
            return self.indegree(u) + self.outdegree(u)
        elif self.has_node(u) and not self._is_directed:
            return int((self.indegree(u) + self.outdegree(u)) / 2)
        else:
            return None

    
    def outdegree(self, u:str) -> int | None:
        if self.has_node(u):
            return len(self._list[u])
        else:
            return None

    
    def indegree(self, u:str) -> int | None:
        if self.has_node(u):
            indegree = 0
            for node, edges in self._list.items():
                for (node, _) in edges:
                    if node == u:
                        indegree += 1
            return indegree
        else:
            return None


    def maximum_edges(self) -> int:
        return np.power(self.get_order(), 2) - self.get_order()


    def warshall(self) -> np.ndarray:
        matrix = self.get_data_matrix()
        warshall = np.zeros((self.get_order(), self.get_order()))
        warshall[matrix != np.inf] = 1

        for n in range(self.get_order()):
            for i in range(self.get_order()):
                for j in range(self.get_order()):
                    warshall[i][j] = warshall[i][j] or (warshall[i][n] and warshall[n][j])
        return warshall


    def print(self) -> None:
        print(self)
    

    def _add_directed_edge(self, u:str, v:str, weight:float=0.) -> None:
        if not self._is_weighted:
            weight = 0
        self.add_node(u)
        self.add_node(v)
        self._list[u].append((v, weight))
        self._size += 1
    
    
    def _remove_directed_edge(self, u:str, v:str) -> None:
        if self.has_node(u) and self.has_node(v):
            i = 0
            while i < len(self._list[u]):
                if self._list[u][i][0] == v:
                    self._list[u].pop(i)
                    self._size -= 1
                else:
                    i += 1


if __name__ == "__main__":
    g = adj_list_graph(is_directed=False)
    print(g)

    g.add_node("Lucas")
    g.add_edge("Lucas", "Barney", 4)
    g.add_edge("Barney", "Maria", 5)
    g.add_edge("Maria", "Lucas", 3)
    g.add_edge("Pedro", "Lucas", 2)
    g.add_edge("Pedro", "Lucas", 8)
    g.add_edge("Lucas", "Lucas", 2)
    g.add_edge("Lucas", "Lucas", 9)
    print(g)
    print()

    print(g.get_data_matrix())
    print()

    print(g.warshall())
    print()

    print(g.has_edge("Pedro", "Lucas"))
    print(g.outdegree("Lucas"))
    print(g.indegree("Lucas"))
    print(g.degree("Lucas"))
    print(g.edge_weight("Lucas", "Lucas"))
    print()

    g.remove_edge("Pedro", "Lucas")
    print(g)
    print()

    print(g.has_edge("Pedro", "Lucas"))
    print()

    g.remove_node("Lucas")
    print(g)
    print(g.has_node("Lucas"))
    print()

    print(g.get_order())
    print(g.get_size())
    print()
    
    print(g.get_data_matrix())
    print()
