"""TDE5 - Análise de Redes Complexas"""


"""##Imports"""

import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
import time

from collections import defaultdict
from copy import deepcopy
from heapq import heappop, heappush
from itertools import chain, permutations
from typing import Literal


"""##Database"""

# Carrega o dataset (substitua 'nome_do_dataset.csv' pelo nome correto do arquivo dentro do zip)
dataset_path = 'C:/Users/ladsw/OneDrive/Desktop/netflix_amazon_disney_titles.csv'  # Substitua pelo nome correto

# Carrega o arquivo CSV em um DataFrame do pandas
df = pd.read_csv(dataset_path)

# Formata o DataFrame do pandas com "strip" e "upper"
df = df.map(lambda x: x.strip().upper() if isinstance(x, str) else x) # Formatação inicial


"""## Grafo"""

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


    def load_list(self, l:defaultdict):
      self.__list = l
      self.__order = len(l)
      self.__size = 0
      for _, edges in tuple(l.items()):
        self.__size += len(edges)
        for v, _ in edges:
          if not v in l.keys():
            l[v] = []


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
    # Get the maximum number of edges for the graph
    def maximum_edges(self) -> int:
        """
        Get the maximum number of edges for the graph.

        Returns:
            int: Maximum number of edges for the graph.
        """
        return np.power(self.order, 2) - self.order if self.is_directed else (np.power(self.order, 2) - self.order) // 2


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

        # for node in nodes:
        #     if isinstance(node, tuple):
        #         print(node)
        return tuple(nodes)#sorted(nodes))


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
            return tuple([node for node, _ in self.__list[u]])
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
            return tuple(in_edges)
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

        return tuple(edges)


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
            return tuple([(u, node, weight) for node, weight in self.__list[u]])
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
            return tuple(in_edges)
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
    def connected_components(self):
        """
        Perform Kosaraju's Algorithm to get a graph with all connected components.

        Returns:
            Self: Graph where each node represents a strongly connected component.
        """
        if self.is_directed:
            # 1. Stack containing the initial and the final steps for each node
            finished = list()  # LIFO Stack

            # 2. Deep-first search with steps marked for each node
            pending = [node for node in self.nodes()]

            stepmarkers = {node: [None, None] for node in self.nodes()}
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
                for out_node in self.out_nodes(u):
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
                    for out_node in self.in_nodes(cur_node):
                        if not out_node in visited:
                            appendeds.append(out_node)

                    component.extend(appendeds)
                    pending.extend(appendeds)

                # Stores the new component
                components.append(component)

            return components

        else:
            def my_dfs(u):
                pending = list()  # LIFO Stack
                visited = list()

                pending.append(u)

                while len(pending) > 0:
                    cur_node = pending.pop()

                    if not cur_node in visited:
                        visited.append(cur_node)

                    for _, adj_node, _ in self.out_edges(cur_node):
                        if not adj_node in visited:
                            pending.append(adj_node)
                
                return visited
            
            components = list()
            visited = list()
            for node in self.nodes():
                if node in visited:
                    continue
                component = my_dfs(node)
                visited.extend(component)
                components.append(component)

            return components


    def prim(self, graph=None):

        if(graph != None):
          self.graph = graph

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
    
    def degree_histogram(self) -> None:

      """
      Displays the a histogram with de centrality distribution.
      """

      degrees = []
      for node in self.nodes():
        degrees.append(self.degree(node))

      average = np.mean(degrees)

      n_bins  = int(self.order/10)

      plt.figure(figsize=(5,2))
      plt.hist(degrees, bins=30, color="skyblue", edgecolor="black")
      plt.axvline(x=average, color='red', linestyle='dashed', label=f"Average = {average}")
      plt.xlabel('Degree')
      plt.ylabel('Frequency')
      plt.legend()
      plt.show()

      return

    def degree_centrality(self, u:str) -> tuple[str, float]:

      """
      Calculate the degree centrality of a node in the graph.

      Args:
          node (str): Name of the node.

      Returns:
          node (str): Name of the node.
          float: Degree centrality of the node.
      """

      return u, self.degree(u)/(self.order-1)

    def betweeness_centrality(self, u:str) -> tuple[str, float]:
        """
        Calculate the betweeness centrality of a node in the graph.
        Uses modified dijkstra algorithm.

        Args:
            node (str): Name of the node.

        Returns:
            node (str): Name of the node.
            float: Betweeness centrality of the node.
        """

        betweeness = 0


        for s in self.nodes():
            if s == u:
                continue

            pending = [(0, s)]
            visited = {node: False for node in self.nodes()}
            paths = {node: (np.inf, []) for node in self.nodes()}

            paths[s] = (0, [None])

            while pending:

                cur_path_cost, cur_node = heappop(pending)

                # Skips if visited
                if visited[cur_node]:
                    continue
                else:
                    visited[cur_node] = True

                # Loops for adjacent nodes looking for better paths
                for _, adj_node, weight in self.out_edges(cur_node):
                    new_path_cost = cur_path_cost + weight

                    if new_path_cost < paths[adj_node][0]:
                        paths[adj_node] = (new_path_cost, [cur_node])
                        heappush(pending, (new_path_cost, adj_node))

                    elif new_path_cost == paths[adj_node][0]:
                        paths[adj_node][1].append(cur_node)

            best_paths = dict()

            # Reconstructing paths to all nodes found
            def construct_paths(node, path):
                if node is None:
                    return [path]
                all_paths = []
                for predecessor in paths[node][1]:
                    all_paths.extend(construct_paths(predecessor, [node] + path))
                return all_paths

            for node in paths.keys():
                if paths[node][0] == np.inf:
                    best_paths[node] = ([], np.inf)
                else:
                    best_paths[node] = (tuple(construct_paths(node, [])), paths[node][0])

            for paths in best_paths.values():

                path_passes_through_interest = 0
                total_best_paths = 0

                for path in paths[0]:

                    total_best_paths += 1

                    print(path)

                    if u == path[-1] :
                        continue

                    if u in path:
                        path_passes_through_interest += 1

                    betweeness += path_passes_through_interest/total_best_paths

        return u, betweeness/2


    def closeness_centrality(self, u:str) -> tuple[str, float]:

      """
      Calculate the closeness centrality of a node in the graph.
      Uses modified dijkstra algorithm.

      Args:
          node (str): Name of the node.

      Returns:
          node (str): Name of the node.
          float: Closeness centrality of the node.
      """

      pending = [(0, u)]
      visited = dict([(node, False) for node in self.nodes()])
      paths = dict([(node, (np.inf, None)) for node in self.nodes()])

      paths[u] = (0, None)  # Default path for source node

      dijkstra_sum = 0 #Sum of the cost of all best paths

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

                  #If new best path: remove older cost, add new cost
                  if paths[adj_node][0] != np.inf:
                    dijkstra_sum = dijkstra_sum - paths[adj_node][0];

                  dijkstra_sum = dijkstra_sum + new_path_cost;

                  paths[adj_node] = (new_path_cost, cur_node)
                  heappush(pending, (new_path_cost, adj_node))

      if dijkstra_sum == 0:
        return u, 0

      best_paths = dict()

      # Reconstructing paths to all nodes found
      for node in paths.keys():
          best_path = []
          cur_node = node
          while cur_node != None:
              best_path.insert(0, cur_node)
              cur_node = paths[best_path[0]][1]

          best_paths[node] = tuple(best_path), paths[node][0]

      if graph.is_directed:
        return u, dijkstra_sum/(self.order-1)
      else:
        return u, (self.order-1)/dijkstra_sum


    def display_top_10_nodes(self, centrality_type:str) -> None:
      #List(str, float)
      top_10_nodes = []

      for node in self.nodes():

        if(centrality_type == "closeness"):
          top_10_nodes.append(self.closeness_centrality(node))

        elif(centrality_type == "degree"):
          top_10_nodes.append(self.degree_centrality(node))
        else:
          print("Invalid centrality type. Use 'closeness' or 'degree'.")
          return

      #Sort by centrality degree
      top_10_nodes = sorted(top_10_nodes, key=lambda x: x[1],reverse=True)[:10]
      #top_10_nodes = top_10_nodes[:10]

      nodes = [item[0] for item in top_10_nodes]
      values = [item[1] for item in top_10_nodes]

      # Creating the bar graph with customizations
      plt.bar(range(len(values)), values, color=['skyblue'], edgecolor='black')
      plt.xticks(range(len(nodes)), nodes, rotation=45)

      plt.title('Top 10 Nodes')
      plt.xlabel('Nodes')
      plt.ylabel('Centrality')

      plt.grid(axis='y', linestyle='--', linewidth=0.7)

      plt.show()

      for index, node in enumerate(top_10_nodes):
        print(f"{index+1}. {node[0]}: {node[1]:.4f}")

      return


"""## Exercício 1"""

start_time = time.time()

###1. GRAFO PONDERADO DIRECIONADO ATOR/DIRETOR

df1 = df.dropna(subset=['director', 'cast']) # Remove NaN
df1 = df1.assign(cast=df1['cast'].str.split(',')).explode('cast') # Transforma 'cast' em lista e abre os resultados (relação unitária para diretor e ator)
df1['director'] = df1['director'].str.strip().str.upper() # Formata 'director'
df1['cast'] = df1['cast'].str.strip().str.upper() # Formata 'cast'
df1 = df1.reset_index(drop=True) # Recalcula índices
df1 = df1.groupby(['director', 'cast']).size().reset_index(name='count') # Contar quantidade de ator por diretor
df1 = df1.groupby('director').apply(lambda x: list(zip(x['cast'], x['count']))).reset_index(name='cast_counts') # Para cada diretor, faz uma lista com (ator, quantidade)
print(df1.head())
print(df1.count())

# Montando grafo
ator_diretor_graph = graph(is_directed=True, is_weighted=True)

# Monta uma lista para as arrestas do grafo
l = defaultdict()
for _, row in df1.iterrows(): # Para cada diretor
  if not row['director'] in l.keys(): # Add nó do diretor caso não exista
    l[row['director']] = []
  for col in row['cast_counts']: # Para cada ator
    if not col[0] in l.keys(): # Add nó do ator caso não exista
      l[col[0]] = []
    l[col[0]].append((row['director'], col[1])) # Add aresta Ator -> Diretor (com peso)

ator_diretor_graph.load_list(l)

print(ator_diretor_graph.order, ator_diretor_graph.size)

###2. GRAFO PONDERADO NÃO-DIRECIONADO ATOR/ATOR

df2 = df.dropna(subset=['cast'])
df2 = df2.assign(cast=df2['cast'].str.strip().str.split(',')) # Separa atores em uma lista
df2['cast'] = df2['cast'].apply(lambda x: [actor.strip().upper() for actor in x]) # Formata 'cast'
df2['cast'] = df2['cast'].apply(lambda x: list(filter(lambda x: x != "", x))) # Filtra vazios em 'cast'
df2['cast'] = df2['cast'].apply(lambda x: list(permutations(sorted(x), 2))) # Gera as permutações entre os atores (já conseiderando os dois sentidos)
df2 = df2.explode('cast')
df2 = df2.reset_index(drop=True)
df2 = df2.groupby(['cast']).size().reset_index(name='count')
df2 = df2.groupby('cast').apply(lambda x: list(zip(x['cast'], x['count']))).reset_index(name='cast_counts').explode('cast_counts')
print(df2.head()['cast_counts'])
print(df2.count())

# Montando grafo
ator_ator_graph = graph(is_directed=False, is_weighted=True)

# Monta uma lista para as arrestas do grafo
l = defaultdict()
for _, row in df2.iterrows():
  col = row['cast_counts']
  if not col[0][0] in l.keys():
    l[col[0][0]] = []
  if not col[0][1]in l.keys():
    l[col[0][1]] = []
  l[col[0][0]].append((col[0][1], col[1]))

ator_ator_graph.load_list(l)

print(ator_ator_graph.order, ator_ator_graph.size)


end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time Ex1: {execution_time:.4f} seconds")


"""## Exercício 2"""

start_time = time.time()

sys.setrecursionlimit(1_000_000)
ad_comp = ator_diretor_graph.connected_components()
aa_comp = ator_ator_graph.connected_components()
print(len(ad_comp))
print(len(aa_comp))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time Ex2: {execution_time:.4f} seconds")


"""##Exercício 3"""

start_time = time.time()

def prim_for_components(node, g:graph, components):
    for comp in components:
        if node in comp:
            g_new = deepcopy(g)
            for origin, dest, _ in g.edges():
                if not (origin in comp and dest in comp):
                    g_new.remove_edge(origin, dest)
            break
    return g_new.prim()

print(prim_for_components("JONATHAN MALEN", ator_diretor_graph, ad_comp))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time Ex3: {execution_time:.4f} seconds")


"""##Exercício 4"""

print("Here 4")
start_time = time.time()

node_degree_centrality = ator_diretor_graph.degree_centrality("GILBERT CHAN")
print(f"Degree Centrality of {node_degree_centrality[0]}: {node_degree_centrality[1]}")

ator_diretor_graph.degree_histogram()

node_degree_centrality = ator_ator_graph.degree_centrality("CELSO FRATESCHI")
print(f"Degree Centrality of {node_degree_centrality[0]}: {node_degree_centrality[1]}")

ator_ator_graph.degree_histogram()

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time Ex4: {execution_time:.4f} seconds")


"""##Exercício 5"""

print("Here 5")
start_time = time.time()

print("Ator -> Director Graph")
ator_diretor_graph.degree_centrality("GILBERT CHAN")
ator_diretor_graph.display_top_10_nodes("degree")
print()
print("Ator -> Ator Graph")
ator_ator_graph.degree_centrality("CELSO FRATESCHI")
ator_ator_graph.display_top_10_nodes("degree")

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time Ex5: {execution_time:.4f} seconds")


"""##Exercício 6"""

start_time = time.time()
ator_diretor_graph.display_top_10_nodes("betweeness", "BetweenessTop10_Ator_Diretor")
end_time = time.time()
execution_time = end_time - start_time
print(f"Ex 6 (Ator -> Ator) tempo de execucao: {execution_time:.4f} seconds")

start_time = time.time()
ator_ator_graph.display_top_10_nodes("betweeness", "BetweenessTop10_Ator_Ator")
end_time = time.time()
execution_time = end_time - start_time
print(f"Ex 6 (Ator -> Ator) tempo de execucao: {execution_time:.4f} seconds")


"""##Exercício 7"""

print("Here 7")
start_time = time.time()

print("Ator -> Director Graph")
ator_diretor_graph.display_top_10_nodes("closeness")
print()
print("Ator -> Ator Graph")
ator_ator_graph.display_top_10_nodes("closeness")

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time Ex7: {execution_time:.4f} seconds")
