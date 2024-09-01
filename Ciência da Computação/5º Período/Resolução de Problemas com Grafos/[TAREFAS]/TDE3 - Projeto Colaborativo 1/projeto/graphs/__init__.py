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
        __order (int): Number of nodes in the graph.
        __size (int): Number of edges in the graph.
        __list (defaultdict): Adjacency list representation.
        __is_directed (bool): Whether the graph is directed or not.
        __is_weighted (bool): Whether the edges have weights or not.
    """


    # Initialize the graph
    def __init__(self, is_directed:bool=True, is_weighted:bool=True) -> None:
        """
        Initialize the graph.

        Args:
            is_directed (bool, optional): Whether the graph is directed or not. Defaults to True.
            is_weighted (bool, optional): Whether the edges have weights or not. Defaults to True.
        """
        self.__order = 0
        self.__size = 0
        self.__list = defaultdict()
        self.__is_directed = is_directed
        self.__is_weighted = is_weighted


    # Return a string representation of the graph
    def __str__(self) -> str:
        """
        Return a string representation of the graph.

        Returns:
            str: String representation of the graph.
        """
        text = ""
        if self.__list:  # Check if graph is not empty
            for u, edges in self.__list.items():
                text += f"{u}: "
                for (v, weight) in edges:
                    text += f"({v}, {weight}) > " if self.__is_weighted else f"({v}) > "
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
        return self.__order


    # Get the number of edges in the graph
    def get_size(self) -> int:
        """
        Get the number of edges in the graph.

        Returns:
            int: Number of edges in the graph.
        """
        if self.__is_directed:
            return self.__size
        else:
            return int(self.__size / 2)


    # Get a deepcopy of the adjacency list
    def get_data_list(self) -> defaultdict:
        """
        Get a deepcopy of the adjacency list.

        Returns:
            defaultdict: Deepcopy of the adjacency list.
        """
        return deepcopy(self.__list)


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
        for node, edges in self.__list.items():
            if not node in nodes_index.keys():
                nodes_index[node] = cur_index
                cur_index += 1
            for i in range(len(edges)):
                if not edges[i][0] in nodes_index.keys():
                    nodes_index[edges[i][0]] = cur_index
                    cur_index += 1
                matrix[nodes_index[node]][nodes_index[edges[i][0]]] = edges[i][1]
        return (nodes_index, matrix)
    

    # Return a list of nodes registered in the graph
    def nodes(self) -> tuple[str]:
        """
        Return a list of nodes registered in the graph.

        Returns:
            tuple[str]: List of nodes
        """
        return tuple(sorted(self.__list.keys()))


    # Add a node to the graph
    def add_node(self, u:str) -> None:
        """
        Add a node to the graph.

        Args:
            u (str): Name of the node to be added.
        """
        if not self.has_node(u):
            self.__list[u] = list()
            self.__order += 1


    # Remove a node from the graph
    def remove_node(self, u:str) -> None:
        """
        Remove a node from the graph.

        Args:
            u (str): Name of the node to be removed.
        """
        if self.has_node(u):
            self.__size -= len(self.__list[u])
            self.__list.pop(u)
            for node, edges in self.__list.items():
                i = 0
                while i < len(edges):
                    if edges[i][0] == u:
                        self.__list[node].pop(i)
                        self.__size -= 1
                    else:
                        i += 1
            self.__order -= 1


    # Check if a node exists in the graph
    def has_node(self, u:str) -> bool:
        """
        Check if a node exists in the graph.

        Args:
            u (str): Name of the node to be checked.

        Returns:
            bool: True if the node exists, otherwise False.
        """
        return u in self.nodes()


    # Get the adjacency list of a node
    def adjacencies_nodes(self, u:str) -> tuple[tuple[str, float]] | None:
        """
        Get the adjacency list of a node.

        Args:
            u (str): Name of the node.

        Returns:
            tuple[tuple[str, float]] | None: Adjacency list of the node if it exists, otherwise None.
        """
        if self.has_node(u):
            return tuple(deepcopy(self.__list[u]))
        else:
            return None
    

    # Return a list of edges registered in the graph
    def edges(self) -> tuple[str]:
        """
        Return a list of edges registered in the graph.

        Returns:
            tuple[str]: List of edges
        """
        edges = list()
        for cur_node in self.nodes():
            for (node, weight) in self.__list[cur_node]:
                edges.append((cur_node, node, weight))
        return tuple(sorted(edges))
    

    # Add an edge between nodes u and v with an optional weight
    def add_edge(self, u:str, v:str, weight:float=1.) -> None:
        """
        Add an edge between nodes u and v with an optional weight.

        Args:
            u (str): Name of the source node.
            v (str): Name of the destination node.
            weight (float, optional): Weight of the edge. Defaults to 1.
        """
        self.__add_directed_edge(u, v, weight)
        if not self.__is_directed:
            self.__add_directed_edge(v, u, weight)

    
    # Remove the edge between nodes u and v
    def remove_edge(self, u:str, v:str) -> None:
        """
        Remove the edge between nodes u and v.

        Args:
            u (str): Name of the source node.
            v (str): Name of the destination node.
        """
        self.__remove_directed_edge(u, v)
        if not self.__is_directed:
            self.__remove_directed_edge(v, u)
    

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
            return any(node == v for node, _ in self.__list[u])
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
            for (node, weight) in self.__list[u]:
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
        if self.has_node(u) and self.__is_directed:
            return self.indegree(u) + self.outdegree(u)
        elif self.has_node(u) and not self.__is_directed:
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
            return len(self.__list[u])
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
            for node, edges in self.__list.items():
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
    

    # Give the diameter of the graph
    def diameter(self) -> tuple[tuple[str], float] | None:
        """
        Give the diameter of the graph.

        Returns:
            tuple[tuple[str], float] | None: Tuple containing the diameter path and its length.
        """
        max_diameter_path = None
        max_diameter_cost = -np.inf

        for node in self.nodes():
            for cur_node in self.nodes():
                path, path_cost = self.dijkstra(node, cur_node)
                if path_cost > max_diameter_cost and not np.isinf(path_cost):
                    max_diameter_path = path
                    max_diameter_cost = path_cost
        
        return (tuple(max_diameter_path), max_diameter_cost) if max_diameter_path else None


    # Check if the graph is a connected Graph
    def is_connected(self) -> bool:
        """
        Check if the graph is a connected graph.

        Returns:
            bool: True if the graph is connected, otherwise False.
        """
        # Check if for any node the reachable nodes are all nodes
        for node in self.nodes():
            if len(self.deepfirst_search(node)) != self.get_order():
                return False
        return True
    

    # Check if the graph is a Eulerian graph
    def is_eulerian(self) -> bool:
        """
        Check if the graph is a Eulerian graph.

        Returns:
            bool: True if the graph is Eulerian, otherwise False.
        """
        # Check if any node have different values for outdegree and indegree
        is_degrees_valid = True
        for node in self.nodes():
            if self.outdegree != self.indegree(node):
                is_degrees_valid = False
                break

        # Check for the sufficient conditions to determine if it's a Eulerian graph
        if self.is_connected() and is_degrees_valid:
            return True
        else:
            return False


    # Check if the graph is a Hamiltonian graph
    def is_hamiltonian(self) -> bool:
        """
        Check if the graph is a Hamiltonian graph.

        Returns:
            bool: True if the graph is Hamiltonian, otherwise False.
        """
        # Check if all nodes have a Hamiltonian cycle
        for node in self.nodes():
            if not self.__is_node_hamiltonian([node], [node]):
                return False
        return True


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
        if not self.has_node(u) or not self.has_node(v):
            return None

        pending = [(0, u)]
        visited = dict([(node, False) for node in self.nodes()])
        paths = dict([(node, (np.inf, None)) for node in self.nodes()])

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
            for adj_node, weight in self.adjacencies_nodes(cur_node):
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
    

    # Find the longest path from a start node to an end node, considering weights.
    def longest_path(self, u:str, v:str) -> tuple[tuple[str], float] | None:
        """
        Perform Deep-First Search to find the longest path between u and v.

        Args:
            u (str): Name of the source node.
            v (str): Name of the destination node.

        Returns:
            tuple[tuple[str], float] | None: Tuple containing the longest path and its length if it exists, otherwise None.
        """
        if not self.has_node(u) or not self.has_node(v):
            return None

        result = self.__longest_path_recursively(u, v)
        return tuple(result[0]), result[1]
    

    # Perform depth-first search from u to v using iterative or recursive method
    def deepfirst_search(self, u:str, v:str|None=None, distance:int=np.inf, method:_SEARCH_METHODS="iterative") -> tuple[str]|None:
        """
        Perform depth-first search from u to v using iterative or recursive method.

        Args:
            u (str): Name of the source node.
            v (str|None, optional): Name of the destination node. Defaults to None.
            distance (int, optional): Maximum distance to search. Defaults to np.inf.
            method (Literal["iterative", "recursive"], optional): Search method to use. Defaults to "iterative".

        Returns:
            tuple[str] | None: Tuple containing the visited nodes if the search is successful, otherwise None.
        """
        # Validate the node u
        if not self.has_node(u):
            return None
        
        # Validate the node v
        if not self.has_node(v):
            v = None
        
        if method == "iterative":
            pending = list()  # LIFO Stack
            visited = list()

            # Adds source node to pending
            pending.append((u, distance))

            # Executes while pending nodes exists and if the destination node has not been reached
            while len(pending) > 0 and not v in visited:
                # Takes the top node pending
                cur_node, cur_distance = pending.pop()

                # Adds current node to visited
                if not cur_node in visited:
                    visited.append(cur_node)

                # Adds all non-visited adjacencies nodes to pending if maximum distance is not reached
                for adj_node, weight in sorted(self.adjacencies_nodes(cur_node), reverse=True):
                    if not adj_node in visited and cur_distance - weight >= 0:
                        pending.append((adj_node, cur_distance - weight))
        
        elif method == "recursive":
            visited = self.__deepfirst_search_recursively(u, v, distance)
        
        else:
            visited = None
        
        return tuple(visited) if visited and (not v or v in visited) else None
    

    # Perform breadth-first search from u to v using iterative method
    def breadthfirst_search(self, u:str, v:str|None=None, distance:int=np.inf) -> tuple[str]|None:
        """
        Perform breadth-first search from u to v using iterative method

        Args:
            u (str): Name of the source node.
            v (str | None, optional): Name of the destination node. Defaults to None.
            distance (int, optional): Maximum distance to search. Defaults to np.inf.

        Returns:
            tuple[str] | None: Tuple containing the visited nodes if the search is successful, otherwise None.
        """
        # Validate the node u
        if not self.has_node(u):
            return None
        
        # Validate the node v
        if not self.has_node(v):
            v = None

        pending = list()  # FIFO Queue
        visited = list()

        # Adds source node to pending
        pending.append((u, distance))

        # Executes while pending nodes exists and if the destination node has not been reached
        while len(pending) > 0 and not v in visited:
            # Takes the bottom node pending
            cur_node, cur_distance = pending.pop(0)

            # Adds current node to visited
            if not cur_node in visited:
                visited.append(cur_node)

            # Adds all non-visited adjacencies nodes to pending if maximum distance is not reached
            for adj_node, weight in sorted(self.adjacencies_nodes(cur_node), reverse=False):
                if not adj_node in visited and cur_distance - weight >= 0:
                    pending.append((adj_node, cur_distance - weight))
        
        return tuple(visited) if visited and (not v or v in visited) else None
    

    # Print the graph
    def print(self) -> None:
        """
        Print the graph.
        """
        print(self)


    # Add a directed edge from u to v with an optional weight
    def __add_directed_edge(self, u:str, v:str, weight:float=1.) -> None:
        """
        Add a directed edge from u to v with an optional weight.

        Args:
            u (str): Name of the source node.
            v (str): Name of the destination node.
            weight (float, optional): Weight of the edge. Defaults to 1.
        """
        if not self.__is_weighted:
            weight = 1.
        
        self.add_node(u)
        self.add_node(v)

        if self.has_edge(u, v):  # Update the old edge if it exists
            self.__list[u] = list(map(lambda x: (v, weight) if x[0] == v else x, self.__list[u]))
        else:
            self.__list[u].append((v, weight))
            self.__size += 1
    
    
    # Remove a directed edge from u to v
    def __remove_directed_edge(self, u:str, v:str) -> None:
        """
        Remove a directed edge from u to v.

        Args:
            u (str): Name of the source node.
            v (str): Name of the destination node.
        """
        if self.has_edge(u, v):
            self.__list[u] = list(filter(lambda x: x[0] == v, self.__list[u]))
            self.__size -= 1
    

    # Check if a node has a Hamiltonian cycle
    def __is_node_hamiltonian(self, path:list[str], visited:list[str]) -> bool:
        """
        Check if a node has a Hamiltonian cycle.

        Args:
            u (str): Name of the node.

        Returns:
            bool: True if the node has a Hamiltonian cycle, otherwise False.
        """
        last_node = path[-1]

        # Returns if the path is a cycle if all nodes have been visited successfully
        if len(path) == self.get_order():
            # Path is a cycle if the last node is connected to the first one
            return last_node in self.adjacencies_nodes(path[0])
        
        # For all adjacencies nodes, try to close a Hamiltonian cycle (not considering already visited nodes)
        for adj_node, _ in self.adjacencies_nodes(last_node):
            if adj_node not in visited and self.__is_node_hamiltonian([*path, adj_node], [*visited, adj_node]):
                return True
        return False
    

    # Perform Deep-First Search to find the longest path between u and v
    def __longest_path_recursively(self, u:str, v:str, path:list[str]|None=None, path_cost:float=0.) -> tuple[list[str], float] | None:
        """
        Perform Deep-First Search to find the longest path between u and v recursively.

        Args:
            u (str): Name of the source node.
            v (str): Name of the destination node.
            path (list[str]|None): Current path from the original node to the node u. Defaults to None.
            path_cost (float|None): Cost of the current path. Defaults to -np.inf.

        Returns:
            tuple[tuple[str], float] | None: Tuple containing the longest path and its length if it exists, otherwise None.
        """
        if not path:
            path = list()

        path.append(u)

        # Stop condition
        if u == v:
            return path, path_cost

        longest_path = None
        longest_path_cost = -np.inf

        # Do a Deep-First Search to find the longest path
        for node, weight in self.adjacencies_nodes(u):
            
            if node not in path:
                new_path, new_path_cost = self.__longest_path_recursively(node, v, path[:], weight + path_cost)

                # After getting the path, check if it have a bigger cost
                if new_path_cost > longest_path_cost:
                    longest_path = new_path
                    longest_path_cost = new_path_cost
        
        return longest_path, longest_path_cost


    # Perform depth-first search from u to v using recursive method
    def __deepfirst_search_recursively(self, u:str, v:str|None=None, distance:int=np.inf, visited:list[str]|None=None) -> tuple[str]|None:
        """
        Perform depth-first search from u to v using recursive method.

        Args:
            u (str): Name of the source node.
            v (str|None, optional): Name of the destination node. Defaults to None.
            distance (int, optional): Maximum distance to search. Defaults to np.inf.
            visited (list[str]|None, optional): List of visited nodes. Defaults to None.
            method (Literal["iterative", "recursive"], optional): Search method to use. Defaults to "iterative".

        Returns:
            tuple[str] | None: Tuple containing the visited nodes if the search is successful, otherwise None.
        """
        # Creates visited if first execution
        if not visited:
            visited = list()

        # Adds source node to visited 
        visited.append(u)

        # Stop condition: destination node or maximum distance has been reached
        if u == v or distance <= 0:
            return visited
        
        # Executes the function recursively across all adjacent nodes if maximum distance is not reached
        for adj_node, weight in sorted(self.adjacencies_nodes(u), reverse=False):
            if not adj_node in visited and distance - weight >= 0:
                visited = self.__deepfirst_search_recursively(adj_node, v, distance - weight, visited)
            
            # Ends the search if v is found
            if v in visited:
                break
        
        return visited if visited else None


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

    print(g.longest_path("0", "4"))
    print()

    print(g.diameter())
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

    print(g.deepfirst_search(u="S", distance=2, method="iterative"))
    print()

    print(g.deepfirst_search(u="S", v="C", method="recursive"))
    print()

    print(g.deepfirst_search(u="S", distance=2, method="recursive"))
    print()

    print(g.breadthfirst_search(u="S", v="C"))
    print()

    print(g.breadthfirst_search(u="S", distance=2))
    print()

    print(g.nodes())
    print()

    print(g.edges())
    print()

    print(g.is_connected())
    print()

    print(g.is_eulerian())
    print()

    print(g.is_hamiltonian())
    print()
