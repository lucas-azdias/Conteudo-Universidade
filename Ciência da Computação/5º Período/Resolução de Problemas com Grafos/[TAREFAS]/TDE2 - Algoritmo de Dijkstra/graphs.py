import numpy as np

from collections import defaultdict
from copy import deepcopy
from heapq import heappop, heappush
from typing import Literal


# Literal type for specifying search method
_SEARCH_METHODS = Literal["iterative", "recursive"]


# Class representing an adjacency list graph
class adj_list_graph:
    """
    Class representing an adjacency list graph.

    Attributes:
        _order (int): Number of nodes in the graph.
        _size (int): Number of edges in the graph.
        _list (defaultdict): Adjacency list representation.
        _is_directed (bool): Whether the graph is directed or not.
        _is_weighted (bool): Whether the edges have weights or not.
    """


    # Initialize the graph
    def __init__(self, is_directed:bool=True, is_weighted:bool=True) -> None:
        """
        Initialize the graph.

        Args:
            is_directed (bool, optional): Whether the graph is directed or not. Defaults to True.
            is_weighted (bool, optional): Whether the edges have weights or not. Defaults to True.
        """
        self._order = 0
        self._size = 0
        self._list = defaultdict()
        self._is_directed = is_directed
        self._is_weighted = is_weighted


    # Return a string representation of the graph
    def __str__(self) -> str:
        """
        Return a string representation of the graph.

        Returns:
            str: String representation of the graph.
        """
        text = ""
        if self._list:  # Check if graph is not empty
            for u, edges in self._list.items():
                text += f"{u}: "
                for (v, weight) in edges:
                    text += f"({v}, {weight}) > " if self._is_weighted else f"({v}) > "
                text = text.removesuffix(" > ")
                text += "\n"
        else:
            text = "<Empty graph>"
        return text.removesuffix("\n")


    # Get the number of nodes in the graph
    def get_order(self) -> int:
        """
        Get the number of nodes in the graph.

        Returns:
            int: Number of nodes in the graph.
        """
        return self._order


    # Get the number of edges in the graph
    def get_size(self) -> int:
        """
        Get the number of edges in the graph.

        Returns:
            int: Number of edges in the graph.
        """
        if self._is_directed:
            return self._size
        else:
            return int(self._size / 2)


    # Get a deepcopy of the adjacency list
    def get_data_list(self) -> defaultdict:
        """
        Get a deepcopy of the adjacency list.

        Returns:
            defaultdict: Deepcopy of the adjacency list.
        """
        return deepcopy(self._list)


    # Get the adjacency matrix representation of the graph
    def get_data_matrix(self) -> tuple[dict, np.ndarray]:
        """
        Get the adjacency matrix representation of the graph.

        Returns:
            tuple[dict, np.ndarray]: Adjacency matrix representation of the graph.
        """
        matrix = np.ones((self.get_order(), self.get_order())) * np.inf
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
                matrix[nodes_index[node]][nodes_index[edges[i][0]]] = edges[i][1]
        return (nodes_index, matrix)


    # Add a node to the graph
    def add_node(self, u:str) -> None:
        """
        Add a node to the graph.

        Args:
            u (str): Name of the node to be added.
        """
        if not self.has_node(u):
            self._list[u] = list()
            self._order += 1


    # Remove a node from the graph
    def remove_node(self, u:str) -> None:
        """
        Remove a node from the graph.

        Args:
            u (str): Name of the node to be removed.
        """
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


    # Check if a node exists in the graph
    def has_node(self, u:str) -> bool:
        """
        Check if a node exists in the graph.

        Args:
            u (str): Name of the node to be checked.

        Returns:
            bool: True if the node exists, otherwise False.
        """
        return u in self._list.keys()


    # Get the adjacency list of a node
    def adjacencies_node(self, u:str) -> tuple[tuple[str, float]] | None:
        """
        Get the adjacency list of a node.

        Args:
            u (str): Name of the node.

        Returns:
            tuple[tuple[str, float]] | None: Adjacency list of the node if it exists, otherwise None.
        """
        if self.has_node(u):
            return tuple(deepcopy(self._list[u]))
        else:
            return None
    

    # Add an edge between nodes u and v with an optional weight
    def add_edge(self, u:str, v:str, weight:float=1.) -> None:
        """
        Add an edge between nodes u and v with an optional weight.

        Args:
            u (str): Name of the source node.
            v (str): Name of the destination node.
            weight (float, optional): Weight of the edge. Defaults to 1.
        """
        self._add_directed_edge(u, v, weight)
        if not self._is_directed:
            self._add_directed_edge(v, u, weight)

    
    # Remove the edge between nodes u and v
    def remove_edge(self, u:str, v:str) -> None:
        """
        Remove the edge between nodes u and v.

        Args:
            u (str): Name of the source node.
            v (str): Name of the destination node.
        """
        self._remove_directed_edge(u, v)
        if not self._is_directed:
            self._remove_directed_edge(v, u)
    

    # Check if there is an edge between nodes u and v
    def has_edge(self, u:str, v:str) -> bool:
        """
        Check if there is an edge between nodes u and v.

        Args:
            u (str): Name of the source node.
            v (str): Name of the destination node.

        Returns:
            bool: True if there is an edge between the nodes, otherwise False.
        """
        if self.has_node(u) and self.has_node(v):
            for (node, _) in self._list[u]:
                if node == v:
                    return True
        return False


    # Get the weight of the edge between nodes u and v
    def edge_weight(self, u:str, v:str) -> float | None:
        """
        Get the weight of the edge between nodes u and v.

        Args:
            u (str): Name of the source node.
            v (str): Name of the destination node.

        Returns:
            float | None: Weight of the edge if it exists, otherwise None.
        """
        if self.has_node(u) and self.has_node(v):
            for (node, weight) in self._list[u]:
                if node == v:
                    return weight
        return None

    
    # Get the degree of a node
    def degree(self, u:str) -> int | None:
        """
        Get the degree of a node.

        Args:
            u (str): Name of the node.

        Returns:
            int | None: Degree of the node if it exists, otherwise None.
        """
        if self.has_node(u) and self._is_directed:
            return self.indegree(u) + self.outdegree(u)
        elif self.has_node(u) and not self._is_directed:
            return int((self.indegree(u) + self.outdegree(u)) / 2)
        else:
            return None

    
    # Get the outdegree of a node
    def outdegree(self, u:str) -> int | None:
        """
        Get the outdegree of a node.

        Args:
            u (str): Name of the node.

        Returns:
            int | None: Outdegree of the node if it exists, otherwise None.
        """
        if self.has_node(u):
            return len(self._list[u])
        else:
            return None

    
    # Get the indegree of a node
    def indegree(self, u:str) -> int | None:
        """
        Get the indegree of a node.

        Args:
            u (str): Name of the node.

        Returns:
            int | None: Indegree of the node if it exists, otherwise None.
        """
        if self.has_node(u):
            indegree = 0
            for node, edges in self._list.items():
                for (node, _) in edges:
                    if node == u:
                        indegree += 1
            return indegree
        else:
            return None


    # Get the maximum number of edges for the graph
    def maximum_edges(self) -> int:
        """
        Get the maximum number of edges for the graph.

        Returns:
            int: Maximum number of edges for the graph.
        """
        return np.power(self.get_order(), 2) - self.get_order()


    # Perform Warshall's algorithm to find transitive closure
    def warshall(self) -> np.ndarray:
        """
        Perform Warshall's algorithm to find transitive closure.

        Returns:
            np.ndarray: Transitive closure for the graph.
        """
        matrix = self.get_data_matrix()
        warshall = np.zeros((self.get_order(), self.get_order()))
        warshall[matrix != np.inf] = 1

        for n in range(self.get_order()):
            for i in range(self.get_order()):
                for j in range(self.get_order()):
                    warshall[i][j] = warshall[i][j] or (warshall[i][n] and warshall[n][j])
        return warshall


    # Perform Dijkstra's algorithm to find shortest path between u and v
    def dijkstra(self, u:str, v:str) -> tuple[tuple[str], float] | None:
        """
        Perform Dijkstra's algorithm to find the shortest path between u and v.

        Args:
            u (str): Name of the source node.
            v (str): Name of the destination node.

        Returns:
            tuple[tuple[str], float] | None: Tuple containing the shortest path and its length if it exists, otherwise None.
        """
        if self.has_node(u) and self.has_node(v):
            pending = [(0, u)]
            visited = dict([(node, False) for node in self._list.keys()])
            paths = dict([(node, (np.inf, None)) for node in self._list.keys()])

            paths[u] = (0, None)  # Default path for source node

            while pending:
                # Chooses the current node based on the best path
                cur_path_cost, cur_node = heappop(pending)

                # Skips if visited
                if visited[cur_node]:
                    continue
                else:
                    visited[cur_node] = True

                # Breaks if end node is reached
                if cur_node == v:
                    break

                # Loops for adjacencies nodes looking for better paths
                for adj_node, weight in self.adjacencies_node(cur_node):
                    new_path_cost = cur_path_cost + weight
                    if new_path_cost < paths[adj_node][0]:
                        paths[adj_node] = (new_path_cost, cur_node)
                        heappush(pending, (new_path_cost, adj_node))
                
            # Reconstructing path to end node
            best_path = []
            cur_node = v
            while cur_node != None:
                best_path.insert(0, cur_node)
                cur_node = paths[best_path[0]][1]
            best_path_cost = paths[v][0]

            return tuple(best_path), best_path_cost
        else:
            return None
    

    # Perform depth-first search from u to v using iterative or recursive method
    def deepfirst_search(self, u:str, v:str|None=None, visited:list[str]=None, method:_SEARCH_METHODS="iterative") -> tuple[str]:
        """
        Perform depth-first search from u to v using iterative or recursive method.

        Args:
            u (str): Name of the source node.
            v (str|None, optional): Name of the destination node. Defaults to None.
            visited (list[str], optional): List of visited nodes. Defaults to None.
            method (Literal["iterative", "recursive"], optional): Search method to use. Defaults to "iterative".

        Returns:
            tuple[str]: Tuple containing the visited nodes if the search is successful, otherwise None.
        """
        if method == "iterative":
            pending = list()  # LIFO Stack
            visited = list()

            # Adds source node to pending
            pending.append(u)

            # Executes while pending nodes exists and if the destination node has not been reached
            while len(pending) > 0 and not v in visited:
                # Takes the top node pending
                cur_node = pending.pop()

                # Adds current node to visited
                if not cur_node in visited:
                    visited.append(cur_node)

                # Adds all non-visited adjacencies nodes to pending
                for adj_node, _ in sorted(self.adjacencies_node(cur_node), reverse=True):
                    if not adj_node in visited:
                        pending.append(adj_node)
        
        elif method == "recursive":
            # Creates visited if first execution
            if not visited:
                visited = list()
            else:
                visited = list(visited)

            # Adds source node to visited 
            visited.append(u)
            
            # Checks if the destination node has not been reached
            if u != v:
                # Executes the function recursively across all adjacent nodes 
                for adj_node, _ in sorted(self.adjacencies_node(u), reverse=False):
                    if not adj_node in visited:
                        visited = self.deepfirst_search(adj_node, v, visited, method)
                    
                    # Ends the search if v is found
                    if v in visited:
                        break
            
        else:
            visited = None
        
        return tuple(visited) if visited is not None else None
    

    def breadthfirst_search(self, u:str, v:str|None=None, visited:list[str]=None, method:_SEARCH_METHODS="iterative") -> tuple[str]:
        if method == "iterative":
            pending = list()  # FIFO Queue
            visited = list()

            # Adds source node to pending
            pending.append(u)

            # Executes while pending nodes exists and if the destination node has not been reached
            while len(pending) > 0 and not v in visited:
                # Takes the bottom node pending
                cur_node = pending.pop(0)

                # Adds current node to visited
                if not cur_node in visited:
                    visited.append(cur_node)

                # Adds all non-visited adjacencies nodes to pending
                for adj_node, _ in sorted(self.adjacencies_node(cur_node), reverse=False):
                    if not adj_node in visited:
                        pending.append(adj_node)
        
        elif method == "recursive":
            # Creates visited if first execution
            if not visited:
                visited = [u]
            else:
                visited = list(visited)
            
            adj_pending = list()  # Adjacent nodes pending to visit
            
            # Checks if the destination node has not been reached
            if not v in visited:
                # Checks every adjacent node
                for adj_node, _ in sorted(self.adjacencies_node(u), reverse=False):
                    if not adj_node in visited:
                        visited.append(adj_node)
                        adj_pending.append(adj_node)
                    
                    # Ends the search if v is found
                    if adj_node == v:
                        break
            
            # Checks if the destination node has not been reached
            if not v in visited:
                # Executes the function recursively across all adjacent nodes
                for adj_node in adj_pending:
                    visited = self.breadthfirst_search(adj_node, v, visited, method)
            
        else:
            visited = None
        
        return tuple(visited) if visited is not None else None
    

    # Print the graph
    def print(self) -> None:
        """
        Print the graph.
        """
        print(self)
    

    # Add a directed edge from u to v with an optional weight
    def _add_directed_edge(self, u:str, v:str, weight:float=1.) -> None:
        """
        Add a directed edge from u to v with an optional weight.

        Args:
            u (str): Name of the source node.
            v (str): Name of the destination node.
            weight (float, optional): Weight of the edge. Defaults to 1.
        """
        if not self._is_weighted:
            weight = 1.
        
        self.add_node(u)
        self.add_node(v)

        if self.has_edge(u, v):  # Removes the old edge if it exists
            self._remove_directed_edge(u, v)
        self._list[u].append((v, weight))

        self._size += 1
    
    
    # Remove a directed edge from u to v
    def _remove_directed_edge(self, u:str, v:str) -> None:
        """
        Remove a directed edge from u to v.

        Args:
            u (str): Name of the source node.
            v (str): Name of the destination node.
        """
        if self.has_edge(u, v):
            self._list[u].pop(self._list[u].index((v, self.edge_weight(u, v))))
            self._size -= 1


# Entry point for running the script
if __name__ == "__main__":
    # Code for testing the graph class
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

    g = adj_list_graph(is_directed=False)
    g.add_edge("0", "1", 4)
    g.add_edge("0", "7", 8)
    g.add_edge("1", "7", 11)
    g.add_edge("1", "2", 8)
    g.add_edge("2", "8", 2)
    g.add_edge("2", "5", 4)
    g.add_edge("2", "3", 7)
    g.add_edge("3", "5", 14)
    g.add_edge("3", "4", 9)
    g.add_edge("4", "5", 10)
    g.add_edge("5", "6", 2)
    g.add_edge("6", "8", 6)
    g.add_edge("6", "7", 1)
    g.add_edge("7", "8", 7)
    g.add_edge("9", "10", 9)

    print(g.dijkstra("0", "4"))
    print()

    g = adj_list_graph(is_weighted=False)
    g.add_edge("S", "A")
    g.add_edge("S", "H")
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("B", "E")
    g.add_edge("C", "G")
    g.add_edge("D", "I")
    g.add_edge("I", "J")
    g.add_edge("I", "K")

    print(g.deepfirst_search(u="S", v="C", method="iterative"))
    print()

    print(g.deepfirst_search(u="S", v="C", method="recursive"))
    print()

    print(g.breadthfirst_search(u="S", v="C", method="iterative"))
    print()

    print(g.breadthfirst_search(u="S", v="C", method="recursive"))
    print()
