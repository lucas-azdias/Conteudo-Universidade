from collections import defaultdict


class AdjListGraph:
    _order = None
    _size = None
    _list = None


    def __init__(self, n:int) -> None:
        self._order = n
        self._size = 0
        self._list = defaultdict()


    def __str__(self) -> str:
        text = ""
        if self._list.items() != defaultdict().items():
            for u, edges in self._list.items():
                text += f"{u}: "
                for (v, weight) in edges:
                    text += f"({v}, {weight}) > "
                text = text.removesuffix(" > ")
                text += "\n"
        else:
            text = "<Empty graph>"
        return text.removesuffix("\n")


    def get_order(self) -> int:
        return self._order


    def get_size(self) -> int:
        return self._size


    def get_data(self) -> defaultdict:
        return self._list.copy()


    def add_node(self, u:str) -> None:
        if not self.has_node(u):
            self._list[u] = list()


    def remove_node(self, u:str) -> None:
        if self.has_node(u):
            self._list.pop(u)
            for node, edges in self._list.items():
                i = 0
                while i < len(edges):
                    if edges[i][0] == u:
                        self._list[node].pop(i)
                    else:
                        i += 1


    def has_node(self, u:str) -> bool:
        return u in self._list.keys()
    

    def add_edge(self, u:str, v:str, weight:float) -> None:
        self.add_node(u)
        self.add_node(v)
        self._list[u].append((v, weight))

    
    def remove_edge(self, u:str, v:str) -> None:
        if self.has_node(u) and self.has_node(v):
            i = 0
            while i < len(self._list[u]):
                if self._list[u][i][0] == v:
                    self._list[u].pop(i)
                else:
                    i += 1
    

    def has_edge(self, u:str, v:str) -> bool:
        if self.has_node(u) and self.has_node(v):
            for (node, _) in self._list[u]:
                if node == v:
                    return True
        return False

    
    def degree(self, u:str) -> int | None:
        if self.has_node(u):
            # DEGREE = OUTDEGREE + INDEGREE - LOOPS
            outdegree_non_loops = 0
            for (node, _) in self._list[u]:
                if node != u:
                    outdegree_non_loops += 1
            return self.indegree(u) + outdegree_non_loops
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


    def edge_weight(self, u:str, v:str) -> tuple[float] | None:
        if self.has_node(u) and self.has_node(v):
            weights = list()
            for (node, weight) in self._list[u]:
                if node == v:
                    weights.append(weight)
            return tuple(weights)
        else:
            return None


    def print(self) -> None:
        print(self)


if __name__ == "__main__":
    g = AdjListGraph(4)
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
