# Make Detecção de ciclos e componentes, Prim e tentar Kruskal sem verificar ciclos (apenas se estou ligando dois nós já visitados)
# Make class Node (apenas retorna o __str__ do objeto colocado dentro)

# https://graph-tool.skewed.de/static/doc/quickstart.html#quickstart

# class Node:

#     def __init__(self, object):
#         self.__data = object
    
#     def __str__(self):
#         return self.__data.__str__()

#     def __eq__(self, other):
#         if Node.is_node(other):
#             return self.get_data() == other.get_data()
#         else:
#             return NotImplemented
    
#     def __lt__(self, other):
#         if Node.is_node(other):
#             return self.get_data() < other.get_data()
#         else:
#             return NotImplemented
    
#     def __gt__(self, other):
#         if Node.is_node(other):
#             return self.get_data() > other.get_data()
#         else:
#             return NotImplemented
    
#     def get_data(self):
#         return self.__data
    
#     @staticmethod
#     def is_node(x: any):
#         return isinstance(x, Node)


# ADD PROPRIEDADES TOPOLOGICAS

# FAZER CLASSE COMPONENTE (COMO UM ITERADOR DE NóS) -> E ADD NO CONNECTED_COMPONENTS
#   -> E COLOCAR ESSA CLASSE DENTRO DAS CLASSES DE NÓS

# TERMINAR spanning_arborescence (EDMOND's ALGORITHM) -> https://wendy-xiao.github.io/posts/2020-07-10-chuliuemdond_algorithm/


import numpy as np

from collections import defaultdict
from copy import deepcopy
from functools import reduce
from heapq import heappop, heappush
from itertools import chain
from typing import Literal, Self


# Literal type for specifying search method
_SEARCH_METHODS = Literal["iterative", "recursive"]


# Class representing an adjacency list graph
class graph:
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
            for u, edges in sorted(self.__list.items()):
                text += f"{u}: "
                for (v, weight) in edges:
                    text += f"({v}, {weight}) > " if self.is_weighted else f"({v}) > "
                text = text.removesuffix(" > ")
                text += "\n"
        else:
            text = "<Empty graph>"
        return text.removesuffix("\n")


    @property
    # Get the number of nodes in the graph
    def order(self) -> int:
        """
        Get the number of nodes in the graph.

        Returns:
            int: Number of nodes in the graph.
        """
        return self.__order


    @property
    # Get the number of edges in the graph
    def size(self) -> int:
        """
        Get the number of edges in the graph.

        Returns:
            int: Number of edges in the graph.
        """
        if self.is_directed:
            return self.__size
        else:
            return int(self.__size / 2)


    @property
    # Get a deepcopy of the adjacency list
    def data_list(self) -> defaultdict:
        """
        Get a deepcopy of the adjacency list.

        Returns:
            defaultdict: Deepcopy of the adjacency list.
        """
        return deepcopy(self.__list)


    @property
    # Get the adjacency matrix representation of the graph
    def data_matrix(self) -> tuple[dict, np.ndarray]:
        """
        Get the adjacency matrix representation of the graph.

        Returns:
            tuple[dict, np.ndarray]: Adjacency matrix representation of the graph.
        """
        matrix = np.ones((self.order, self.order)) * np.inf
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
    

    @property
    # Get the maximum number of edges for the graph
    def maximum_edges(self) -> int:
        """
        Get the maximum number of edges for the graph.

        Returns:
            int: Maximum number of edges for the graph.
        """
        return np.power(self.order, 2) - self.order if self.is_directed else (np.power(self.order, 2) - self.order) // 2
    

    @property
    # Give the diameter of the graph
    def diameter(self) -> tuple[tuple[str], float] | None:
        """
        Give the diameter of the graph.

        Returns:
            tuple[tuple[str], float] | None: Tuple containing the diameter path and its length.
        """
        max_diameter_path = None
        max_diameter_cost = -np.inf

        # Search for every combination of nodes (skip repeated nodes combinations)
        for node in self.nodes():
            # TODO SOME TAKE 4.2 OTHERS 0.01 -> check that and correct the 4.2 (investigate the reason)
            paths = self.shortest_paths(node)

            path, path_cost = max(paths.values(), key=lambda x: x[1] if not np.isinf(x[1]) else -np.inf)

            # Update the greatest dijkstra path found
            if path_cost > max_diameter_cost and not np.isinf(path_cost):
                max_diameter_path = path
                max_diameter_cost = path_cost
        
        return (tuple(max_diameter_path), max_diameter_cost) if max_diameter_path else None
    

    @property
    # Check if the graph is directed
    def is_directed(self) -> bool:
        """
        Check if the graph is directed.

        Returns:
            bool: True if the graph is directed, otherwise False.
        """
        return self.__is_directed
    

    @property
    # Check if the graph is weighted
    def is_weighted(self) -> bool:
        """
        Check if the graph is weighted.

        Returns:
            bool: True if the graph is weighted, otherwise False.
        """
        return self.__is_weighted
    

    @property
    # Check if the graph is a strongly connected graph
    def is_connected(self) -> bool:
        """
        Check if the graph is a strongly connected graph.

        Returns:
            bool: True if the graph is strongly connected, otherwise False.
        """
        # Check if for any node the directly reachable nodes are all the nodes
        for node in self.nodes():
            if len(self.breadthfirst_search(node)) != self.order:
                return False
        return True


    @property
    # Check if the graph is a weakly connected graph
    def is_weakly_connected(self) -> bool:
        """
        Check if the graph is a weakly connected graph.

        Returns:
            bool: True if the graph is weakly connected, otherwise False.
        """
        # Check if for any node the undirectly reachable nodes are all nodes
        for node in self.nodes():
            if len(self.breadthfirst_search(node, ignore_direction=True)) != self.order:
                return False
        return True
    

    @property
    # Check if the graph is a cyclic graph
    def is_cyclic(self) -> bool:
        """
        Check if the graph is a cyclic graph.

        Returns:
            bool: True if the graph is cyclic, otherwise False.
        """
        return self.topological_sort() == None


    @property
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
        if self.is_connected and is_degrees_valid:
            return True
        else:
            return False


    @property
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
    

    # Return a list of nodes registered in the graph or the neighbors of a specific node if u is provided
    def nodes(self, u:str|None=None) -> tuple[str] | None:
        """
        Return a list of nodes registered in the graph or the neighbors of a specific node if u is provided.

        Args:
            u (str, optional): Name of the node. If provided, returns edges linked to this node. Defaults to None.

        Returns:
            tuple[str] | None: Nodes of the graph or, if u is provided, neighboring nodes if node exists, otherwise None.
        """
        if u:  # If a node is provided
            if not self.has_node(u):
                return None

            nodes = set(chain(self.out_nodes(u), self.in_nodes(u)))
        
        else:  # If a node is not provided
            nodes = self.__list.keys()
        
        return tuple(sorted(nodes))
    
    
    # Get the outgoing neighbors of a node
    def out_nodes(self, u:str) -> tuple[str] | None:
        """
        Get the outgoing neighbors of a node.

        Args:
            u (str): Name of the node.

        Returns:
            tuple[str] | None: Outgoing neighbors of the node if it exists, otherwise None.
        """
        if self.has_node(u):
            return tuple(sorted([node for node, _ in self.__list[u]]))
        else:
            return None


    # Get the ingoing neighbors of a node
    def in_nodes(self, u:str) -> tuple[str] | None:
        """
        Get the ingoing neighbors of a node.

        Args:
            u (str): Name of the node.

        Returns:
            tuple[str] | None: Ingoing neighbors of the node if it exists, otherwise None.
        """
        if self.has_node(u):
            in_edges = list()
            for node, edges in self.__list.items():
                for cur_node, _ in edges:
                    if cur_node == u:
                        in_edges.append(node)
                        break
            return tuple(sorted(in_edges))
        else:
            return None


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
    

    # Return a list of edges registered in the graph or edges linked to a specific node if u is provided
    def edges(self, u:str|None=None) -> tuple[tuple[str, str, float]] | None:
        """
        Return a list of edges registered in the graph or edges linked to a specific node if u is provided.

        Args:
            u (str, optional): Name of the node. If provided, returns edges linked to this node. Defaults to None.

        Returns:
            tuple[tuple[str, str, float]] | None: Edges of the graph or, if u is provided, edges of the node if node exists, otherwise None.
        """
        if u:  # If a node is provided
            if not self.has_node(u):
                return None

            edges = set(chain(self.out_edges(u), self.in_edges(u)))

        else:  # If a node is not provided
            edges = list()
            for cur_node in self.nodes():
                for (node, weight) in self.__list[cur_node]:
                    edges.append((cur_node, node, weight))
        
        return tuple(sorted(edges))


    # Get the outgoing edges of a node
    def out_edges(self, u:str) -> tuple[tuple[str, str, float]] | None:
        """
        Get the outgoing edges of a node.

        Args:
            u (str): Name of the node.

        Returns:
            tuple[tuple[str, str, float]] | None: Outgoing edges of the node if it exists, otherwise None.
        """
        if self.has_node(u):
            return tuple(sorted([(u, node, weight) for node, weight in self.__list[u]]))
        else:
            return None


    # Get the ingoing edges of a node
    def in_edges(self, u:str) -> tuple[tuple[str, str, float]] | None:
        """
        Get the ingoing edges of a node.

        Args:
            u (str): Name of the node.

        Returns:
            tuple[tuple[str, str, float]] | None: ingoing edges of the node if it exists, otherwise None.
        """
        if self.has_node(u):
            in_edges = list()
            for node, edges in self.__list.items():
                for cur_node, weight in edges:
                    if cur_node == u:
                        in_edges.append((node, u, weight))
            return tuple(sorted(in_edges))
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
        self.__add_directed_edge(u, v, weight)
        if not self.is_directed:
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
        if not self.is_directed:
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
        if self.has_node(u):
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
    

    # Invert the direction of the edge between nodes u and v
    def invert_edge(self, u:str, v:str) -> None:
        """
        Invert the direction of the edge between nodes u and v.

        Args:
            u (str): Name of the source node.
            v (str): Name of the destination node.
        """
        if self.has_edge(u, v):
            self.add_edge(v, u, self.edge_weight(u, v))
            self.remove_edge(u, v)

    
    # Get the degree of a node
    def degree(self, u:str) -> int | None:
        """
        Get the degree of a node.

        Args:
            u (str): Name of the node.

        Returns:
            int | None: Degree of the node if it exists, otherwise None.
        """
        if self.has_node(u) and self.is_directed:
            return self.indegree(u) + self.outdegree(u)
        elif self.has_node(u) and not self.is_directed:
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
            for _, edges in self.__list.items():
                for node, _ in edges:
                    if node == u:
                        indegree += 1
            return indegree
        else:
            return None
    

    # Perform depth-first search from u to v using iterative or recursive method
    def deepfirst_search(self, u:str, v:str|None=None, distance:int=np.inf, ignore_direction:bool=False, method:_SEARCH_METHODS="iterative") -> tuple[str]|None:
        """
        Perform depth-first search from u to v using iterative or recursive method.

        Args:
            u (str): Name of the source node.
            v (str|None, optional): Name of the destination node. Defaults to None.
            distance (int, optional): Maximum distance to search. Defaults to np.inf.
            ignore_direction (bool, optional): Ignore direction of edges during search. Defaults to False.
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
        
        if not ignore_direction:
            # Function to get the adjacent nodes only considers the outgoing edges
            get_adjacent_nodes = self.out_edges
        else:
            # Function to get the adjacent nodes considers all edges connected to the node (outgoing edges and ingoing edges)
            get_adjacent_nodes = self.edges
        
        # Choose the search method
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
                
                # Filter only the relevants nodes (ignore the current node in the edges)
                adj_edges = sorted(map(lambda x: (x[1], x[2]) if x[1] != cur_node else (x[0], x[2]), get_adjacent_nodes(cur_node)), reverse=True)

                # Adds all non-visited adjacencies nodes to pending if maximum distance is not reached
                for adj_node, weight in adj_edges:
                    if not adj_node in visited and cur_distance - weight >= 0:
                        pending.append((adj_node, cur_distance - weight))
        
        elif method == "recursive":
            visited = self.__deepfirst_search_recursively(u, v, distance, get_adjacent_nodes)
        
        else:
            visited = None
        
        return tuple(visited) if visited and (not v or v in visited) else None
    

    # Perform breadth-first search from u to v using iterative method
    def breadthfirst_search(self, u:str, v:str|None=None, distance:int=np.inf, ignore_direction:bool=False) -> tuple[str]|None:
        """
        Perform breadth-first search from u to v using iterative method.

        Args:
            u (str): Name of the source node.
            v (str | None, optional): Name of the destination node. Defaults to None.
            distance (int, optional): Maximum distance to search. Defaults to np.inf.
            ignore_direction (bool, optional): Ignore direction of edges during search. Defaults to False.

        Returns:
            tuple[str] | None: Tuple containing the visited nodes if the search is successful, otherwise None.
        """
        # Validate the node u
        if not self.has_node(u):
            return None
        
        # Validate the node v
        if not self.has_node(v):
            v = None
        
        if not ignore_direction:
            # Function to get the adjacent nodes only considers the outgoing edges
            get_adjacent_nodes = self.out_edges
        else:
            # Function to get the adjacent nodes considers all edges connected to the node (outgoing edges and ingoing edges)
            get_adjacent_nodes = self.edges

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

            # Filter only the relevants nodes (ignore the current node in the edges)
            adj_edges = sorted(map(lambda x: (x[1], x[2]) if x[1] != cur_node else (x[0], x[2]), get_adjacent_nodes(cur_node)), reverse=False)
            
            # Adds all non-visited adjacencies nodes to pending if maximum distance is not reached
            for adj_node, weight in adj_edges:
                if not adj_node in visited and cur_distance - weight >= 0:
                    pending.append((adj_node, cur_distance - weight))
        
        return tuple(visited) if visited and (not v or v in visited) else None


    # Perform Warshall's Algorithm to find transitive closure
    def transitive_closure(self) -> np.ndarray:
        """
        Perform Warshall's algorithm to find transitive closure.

        Returns:
            np.ndarray: Transitive closure for the graph.
        """
        matrix = self.data_matrix
        warshall = np.zeros((self.order, self.order))
        warshall[matrix != np.inf] = 1

        for n in range(self.order):
            for i in range(self.order):
                for j in range(self.order):
                    warshall[i][j] = warshall[i][j] or (warshall[i][n] and warshall[n][j])
        return warshall


    # Perform Dijkstra's Algorithm to find the shortest path between u and all nodes
    def shortest_paths(self, u:str) -> dict[str, tuple[tuple[str], float]] | None:
        """
        Perform Dijkstra's algorithm to find the shortest path between u and all nodes.

        Args:
            u (str): Name of the source node.

        Returns:
            dict[str, tuple[tuple[str], float]] | None: A dictionary containing shortest paths from the source node to all other nodes, where keys are destination nodes and values are tuples containing the shortest path and its length. Returns None if the source node is not in the graph.
        """
        if not self.has_node(u):
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

            # Loops for adjacencies nodes looking for better paths
            for _, adj_node, weight in self.out_edges(cur_node):
                new_path_cost = cur_path_cost + weight
                if new_path_cost < paths[adj_node][0]:
                    paths[adj_node] = (new_path_cost, cur_node)
                    heappush(pending, (new_path_cost, adj_node))

        best_paths = dict()

        # Reconstructing paths to all nodes found
        for node in paths.keys():
            best_path = []
            cur_node = node
            while cur_node != None:
                best_path.insert(0, cur_node)
                cur_node = paths[best_path[0]][1]
            
            best_paths[node] = tuple(best_path), paths[node][0]
        
        return best_paths
    

    # Perform Dijkstra's Algorithm to find shortest path between u and v
    def shortest_path(self, u:str, v:str) -> tuple[tuple[str], float] | None:
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

        paths = self.shortest_paths(u)
            
        if not v in paths.keys():
            return None

        return paths[v]
    

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
    

    # Perform Tarjan's Algorithm to get a topological sort of the graph
    def topological_sort(self) -> tuple[str]|None:
        """
        Perform Tarjan's Algorithm to get a topological sort of the graph.

        Returns:
            tuple[str]|None: Tuple containing the nodes in topologically sorted order if a cycle is not detected, otherwise None.
        """
        pending = [node for node in self.nodes()]
        visiting = list()
        visited = list()

        # Function to visit a node (returns True to continue the search and False if the execution must halt due to a cycle detected)
        def visit(u:str) -> bool:
            # Ignores visit if node is visited
            if u in visited:
                return True
            
            # Stop condition: Cycle detected
            if u in visiting:
                return False
            
            # Passes the node from pending to visiting
            pending.remove(u)
            visiting.append(u)

            # Visits all outgoing nodes
            for out_node in self.out_nodes(u):
                has_cycle = visit(out_node)

                # Stop condition: Cycle detected
                if not has_cycle:
                    return None
            
            # Passes the node from visiting to visited
            visiting.remove(u)
            visited.insert(0, u)

            return True

        # While not visited all nodes, continue to search
        while pending:
            has_cycle = visit(pending[0])

            # Stop condition: Cycle detected
            if not has_cycle:
                return None

        return tuple(visited)


    # Perform Kosaraju's Algorithm to get a graph with all connected components
    def connected_components(self) -> Self:
        """
        Perform Kosaraju's Algorithm to get a graph with all connected components.

        Returns:
            Self: Graph where each node represents a strongly connected component.
        """
        my_graph = deepcopy(self)
        
        # 1. Stack containing the initial and the final steps for each node
        finished = list()  # LIFO Stack
        
        # 2. Deep-first search with steps marked for each node
        pending = [node for node in my_graph.nodes()]

        stepmarkers = {node: [None, None] for node in my_graph.nodes()}
        step = 0  # Indicates when a step occured

        # Function to visit and mark all nodes with steps
        def visit_marking(u:str, step:int) -> None:
            # Ignores visit if node is visited
            if not u in pending:
                return step
            
            # Removes the node from pending
            pending.remove(u)

            stepmarkers[u][0] = step
            step += 1

            # Visits all outgoing nodes
            for out_node in my_graph.out_nodes(u):
                if not stepmarkers[out_node][0]:
                    step = visit_marking(out_node, step)
            
            # Marks the node as visited
            stepmarkers[u][1] = step
            step += 1

            finished.append(u)

            return step

        # While not visited all nodes, continue to search and mark
        while pending:
            step = visit_marking(pending[0], step)

        # 3. Poping from the stack and doing a new deep-first search and discovering all components
        pending = list()
        visited = list()
        components = list()

        # While not removed all nodes from the stack, continue to search (in inverted direction) and cluster components
        while finished:
            # Removes the current node from the stack (ignores if already visited)
            stack_node = finished.pop()
            if stack_node in visited:
                continue

            component = [stack_node]  # New component
            pending = [stack_node]

            # Deep-first search for each node from the stack
            while pending:
                # Removes the node from pending
                cur_node = pending.pop()

                # Adds the node to visited
                visited.append(cur_node)

                # For all ingoing nodes, append it to the components
                appendeds = []
                for out_node in my_graph.in_nodes(cur_node):
                    if not out_node in visited:
                        appendeds.append(out_node)
                
                component.extend(appendeds)
                pending.extend(appendeds)
            
            # Stores the new component
            components.append(tuple(component))

        # 4. Reconstruct the graph clustering all components
        for component in components:
            component_node = ", ".join(component)  # Component node name
            my_graph.add_node(component_node)  # Adds the new component node

            # For each node in the graph, readds its edges to the component node if it is an edge linked with an external node
            for node in component:
                edges = my_graph.edges(node)
                my_graph.remove_node(node)
                for u, v, weight in edges:
                    if not u in component:
                        my_graph.add_edge(u, component_node, weight)
                    elif not v in component:
                        my_graph.add_edge(component_node, v, weight)

        return my_graph


    # Perform Edmonds' Algorithm to get the minimum or the maximum spanning arborescence
    def spanning_arborescence(self, u:str|None=None) -> Self:
        """
        Perform Edmonds' Algorithm to get the minimum or the maximum spanning arborescence.

        Args:
            u (str | None, optional): The root of the arborescence. Defaults to None.

        Returns:
            Self: Graph representing the minimum or the maximum spanning arborescence.
        """
        my_graph = deepcopy(self)

        # 1. If no valid node is passed, then calculates the root for the arborescence
        if not u or not my_graph.has_node(u):
            # The root node is decided based on the node with the biggest sum of all outgoing edges weights
            nodes_out_edges_weights = [
                (
                    node,
                    reduce(lambda x, y: (None, None, x[2] + y[2]), my_graph.out_edges(node))[2] if my_graph.out_edges(node) else -np.inf
                ) for node in my_graph.nodes()
            ]  # Calculates the sum of all outgoing edges weights for each node
            u = max(nodes_out_edges_weights, key=lambda x: x[1])[0]
        
        # 2. Remove all ingoing edges to te root node
        for node, _, _ in my_graph.in_edges(u):
            my_graph.remove_edge(node, u)
        
        # TODO TERMINAR FUNÇÃO
        
        # 3. Adds
        # TALVEZ CRIAR GRAFO NOVO AO INVES
        # SERIA DEIXAR APENAS AS ARRESTAS COM OS MAIORES WEIGHT (SENDO QUE SAO INGOING E IGNORA A RAIZ) PARA CADA NODE

        return my_graph
    

    def prim(self):
        start = self.nodes()[0]

        pending = [(0, start)]
        visited = dict([(node, False) for node in self.nodes()])
        paths = dict([(node, (np.inf, None)) for node in self.nodes()])

        paths[start] = (0, None)  # Default path for source node

        while pending:
            # Chooses the current node based on the best path
            _, cur_node = heappop(pending)

            # Skips if visited
            if visited[cur_node]:
                continue
            else:
                visited[cur_node] = True

            # Loops for adjacencies nodes looking for better paths
            for _, adj_node, weight in self.out_edges(cur_node):
                heappush(pending, (weight, adj_node))
                if weight < paths[adj_node][0] and not visited[adj_node]:
                    paths[adj_node] = (weight, cur_node)

        my_graph = graph(is_directed=self.is_directed, is_weighted=self.is_weighted)

        # Reconstructing paths to all nodes found
        for node in paths.keys():
            if paths[node][1]:
                my_graph.add_edge(node, paths[node][1], paths[node][0])

        return my_graph 


    # Print the graph
    def display(self) -> None:
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
        if not self.is_weighted:
            weight = 1.
        
        # Update the old edge if it exists
        if self.has_edge(u, v):
            self.__list[u] = list(map(lambda x: (v, weight) if x[0] == v else x, self.__list[u]))
            return
        
        self.add_node(u)
        self.add_node(v)
        
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
            self.__list[u] = list(filter(lambda x: x[0] != v, self.__list[u]))
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
        if len(path) == self.order:
            # Path is a cycle if the last node is connected to the first one
            return last_node in self.out_nodes(path[0])
        
        # For all adjacencies nodes, try to close a Hamiltonian cycle (not considering already visited nodes)
        for adj_node in self.out_nodes(last_node):
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
        for _, node, weight in self.out_edges(u):
            
            if node not in path:
                new_path, new_path_cost = self.__longest_path_recursively(node, v, path[:], weight + path_cost)

                # After getting the path, check if it have a bigger cost
                if new_path_cost > longest_path_cost:
                    longest_path = new_path
                    longest_path_cost = new_path_cost
        
        return longest_path, longest_path_cost


    # Perform depth-first search from u to v using recursive method
    def __deepfirst_search_recursively(self, u:str, v:str|None=None, distance:int=np.inf, ignore_direction:bool=False, visited:list[str]|None=None) -> tuple[str]|None:
        """
        Perform depth-first search from u to v using recursive method.

        Args:
            u (str): Name of the source node.
            v (str|None, optional): Name of the destination node. Defaults to None.
            distance (int, optional): Maximum distance to search. Defaults to np.inf.
            ignore_direction (bool, optional): Ignore direction of edges during search. Defaults to False.
            visited (list[str]|None, optional): List of visited nodes. Defaults to None.

        Returns:
            tuple[str] | None: Tuple containing the visited nodes if the search is successful, otherwise None.
        """
        if not ignore_direction:
            # Function to get the adjacent nodes only considers the outgoing edges
            get_adjacent_nodes = self.out_edges
        else:
            # Function to get the adjacent nodes considers all edges connected to the node (outgoing edges and ingoing edges)
            get_adjacent_nodes = self.edges
        
        # Creates visited if first execution
        if not visited:
            visited = list()

        # Adds source node to visited 
        visited.append(u)

        # Stop condition: destination node or maximum distance has been reached
        if u == v or distance <= 0:
            return visited
        
        # Filter only the relevants nodes (ignore the current node in the edges)
        adj_edges = sorted(map(lambda x: (x[1], x[2]) if x[1] != u else (x[0], x[2]), get_adjacent_nodes(u)), reverse=False)
    
        # Executes the function recursively across all adjacent nodes if maximum distance is not reached
        for adj_node, weight in adj_edges:
            if not adj_node in visited and distance - weight >= 0:
                visited = self.__deepfirst_search_recursively(adj_node, v, distance - weight, ignore_direction, visited)
            
            # Ends the search if v is found
            if v in visited:
                break
        
        return visited if visited else None


# Entry point for running the script
if __name__ == "__main__":
    # Code for testing the graph class
    g = graph(is_directed=False)
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

    print(g.data_matrix)
    print()

    print(g.transitive_closure())
    print()

    print(g.has_edge("Pedro", "Lucas"))
    print(g.edge_weight("Lucas", "Lucas"))
    print()

    print(g.nodes())
    print(g.nodes("Lucas"))
    print(g.out_nodes("Lucas"))
    print(g.in_nodes("Lucas"))
    print()

    print(g.edges())
    print(g.edges("Lucas"))
    print(g.out_edges("Lucas"))
    print(g.in_edges("Lucas"))
    print()

    print(g.degree("Lucas"))
    print(g.outdegree("Lucas"))
    print(g.indegree("Lucas"))
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

    print(g.order)
    print(g.size)
    print()
    
    print(g.data_matrix)
    print()

    g = graph(is_directed=False)
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
    
    print(g.maximum_edges)
    print()

    print(g.shortest_path("0", "4"))
    print()

    print(g.longest_path("0", "4"))
    print()

    print(g.diameter)
    print()

    g = graph(is_weighted=False)
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

    print(g.is_connected)
    print()

    print(g.is_weakly_connected)
    print()

    print(g.is_eulerian)
    print()

    print(g.is_hamiltonian)
    print()

    g = graph(is_directed=True)
    g.add_edge("A", "B")
    g.add_edge("A", "F")
    g.add_edge("B", "H")
    g.add_edge("D", "C")
    g.add_edge("D", "E")
    g.add_edge("E", "I")
    g.add_edge("G", "A")
    g.add_edge("G", "B")
    g.add_edge("G", "C")
    g.add_edge("I", "C")
    g.add_edge("J", "E")

    print(g.topological_sort())
    print(g.is_cyclic)
    print()

    g.add_edge("H", "G")
    
    print(g.topological_sort())
    print(g.is_cyclic)
    print()

    g = graph(is_directed=True)
    g.add_edge("0", "1")
    g.add_edge("1", "2")
    g.add_edge("2", "3")
    g.add_edge("2", "4")
    g.add_edge("3", "0")
    g.add_edge("4", "5")
    g.add_edge("5", "6")
    g.add_edge("6", "4")
    g.add_edge("7", "6")
    g.add_edge("7", "8")

    print(g.connected_components().nodes())
    print(g.connected_components())
    print()

    g = graph(is_directed=True, is_weighted=True)
    g.add_edge("1", "2", 10)
    g.add_edge("1", "3", 4)
    g.add_edge("1", "4", 9)
    g.add_edge("2", "1", 8)
    g.add_edge("2", "3", 10)
    g.add_edge("2", "4", 3)
    g.add_edge("3", "1", 2)
    g.add_edge("3", "2", 12)
    g.add_edge("3", "4", 7)
    g.add_edge("4", "1", 11)
    g.add_edge("4", "2", 2)
    g.add_edge("4", "3", 6)

    print(g.spanning_arborescence())
    print()

    g = graph(is_directed=False, is_weighted=True)
    g.add_edge("A", "B", 10)
    g.add_edge("A", "C", 12)
    g.add_edge("B", "C", 9)
    g.add_edge("B", "D", 8)
    g.add_edge("C", "E", 3)
    g.add_edge("C", "F", 1)
    g.add_edge("D", "E", 7)
    g.add_edge("D", "G", 8)
    g.add_edge("D", "H", 5)
    g.add_edge("E", "F", 3)
    g.add_edge("F", "H", 6)
    g.add_edge("G", "H", 9)
    g.add_edge("G", "I", 2)
    g.add_edge("H", "I", 11)
    print(g.prim())
