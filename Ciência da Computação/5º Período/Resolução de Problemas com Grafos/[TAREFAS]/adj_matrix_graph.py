import numpy as np

from copy import deepcopy


class AdjMatrixGraph:
    _order = None
    _size = None
    _matrix = None


    def __init__(self, n:int) -> None:
        self._order = n
        self._size = 0
        self._matrix = np.ones((n, n)) * np.inf
    

    def __str__(self) -> str:
        text = "" 
        for i in range(self.get_order()):
            text += str(self._matrix[i]) + "\n"
        return text.removesuffix("\n")
    

    def copy(self):
        return deepcopy(self)


    def get_order(self) -> int:
        return self._order


    def get_size(self) -> int:
        return self._size


    def get_data(self) -> np.ndarray:
        return self._matrix.copy()
        

    def add_node(self) -> None:
        # self._matrix = np.append(self._matrix, np.ones((1, self.get_order())) * np.inf, axis=0)
        # self._matrix = np.append(self._matrix, np.ones((self.get_order() + 1, 1)) * np.inf, axis=1)
        self._matrix = np.hstack((self._matrix, np.ones((self.get_order(), 1)) * np.inf))
        self._matrix = np.vstack((self._matrix, np.ones((1, self.get_order()  + 1)) * np.inf))
        self._order += 1


    def add_edge(self, u:int, v:int, weight:float) -> None:
        if self._is_valid_node(u) and self._is_valid_node(v):
            if not self.has_edge(u, v):
                self._size += 1
            self._matrix[u][v] = weight
        else:
            print("Invalid node detected!")


    def remove_edge(self, u:int, v:int) -> None:
        if self._is_valid_node(u) and self._is_valid_node(v):
            if self.has_edge(u, v):
                self._matrix[u][v] = np.inf
                self._size -= 1
        else:
            print("Invalid node detected!")


    def has_edge(self, u, v) -> bool:
        if self._is_valid_node(u) and self._is_valid_node(v):
            return self._matrix[u][v] != np.inf
        else:
            print("Invalid node detected!")
            return False


    def degree(self, u:int) -> int | None:
        if self._is_valid_node(u):
            degree = 0
            for i in range(self.get_order()):
                if self._matrix[u][i] != np.inf:
                    degree += 1
                if self._matrix[i][u] != np.inf:
                    degree += 1
            if self._matrix[u][u] != np.inf:
                degree -= 1
            return degree
        else:
            print("Invalid node detected!")
            return None


    def outdegree(self, u:int) -> int | None:
        if self._is_valid_node(u):
            outdegree = 0
            for i in range(self.get_order()):
                if self._matrix[u][i] != np.inf:
                    outdegree += 1
            return outdegree
        else:
            print("Invalid node detected!")
            return None


    def indegree(self, u:int) -> int | None:
        if self._is_valid_node(u):
            indegree = 0
            for i in range(self.get_order()):
                if self._matrix[i][u] != np.inf:
                    indegree += 1
            return indegree
        else:
            print("Invalid node detected!")
            return None
        
    def warshall(self) -> np.ndarray:
        warshall = np.zeros((self.get_order(), self.get_order()))
        warshall[self._matrix != np.inf] = 1

        for n in range(self.get_order()):
            for i in range(self.get_order()):
                for j in range(self.get_order()):
                    warshall[i][j] = warshall[i][j] or (warshall[i][n] and warshall[n][j])
        
        return warshall


    def maxmimum_edges(self) -> int:
        return np.power(self.get_order(), 2) - self.get_order()


    def is_dense(self) -> bool:
        # Dense graph = >90% of the maximum amount of edges
        return self._size > 0.9 * self.maxmimum_edges()
    

    def has_path(self, u:int, v:int) -> bool:
        return self.warshall()[u][v] == 1


    def print(self) -> None:
        print(self)


    def _is_valid_node(self, u:int) -> bool:
        return u < self.get_order()


if __name__ == "__main__":
    g = AdjMatrixGraph(4)
    print(g, g.get_order(), g.get_size(), g.degree(3), g.indegree(3), g.outdegree(3), "\n")

    g.add_edge(3, 2, 1)
    print(g, g.get_order(), g.get_size(), g.degree(3), g.indegree(3), g.outdegree(3), "\n")

    g.add_edge(3, 3, 1)
    print(g, g.get_order(), g.get_size(), g.degree(3), g.indegree(3), g.outdegree(3), "\n")

    g.add_edge(3, 1, 1)
    print(g, g.get_order(), g.get_size(), g.degree(3), g.indegree(3), g.outdegree(3), "\n")

    g.add_node()
    print(g, g.get_order(), g.get_size(), g.degree(3), g.indegree(3), g.outdegree(3), "\n")

    g.remove_edge(3, 1)
    print(g, g.get_order(), g.get_size(), g.degree(3), g.indegree(3), g.outdegree(3), "\n")

    g.add_edge(1, 2, 1)
    g.add_edge(4, 2, 1)
    g.add_edge(4, 4, 1)
    g.add_edge(2, 1, 1)
    print(g, "\n")
    print(g.warshall(), "\n")
    print(g.has_path(1, 3))
