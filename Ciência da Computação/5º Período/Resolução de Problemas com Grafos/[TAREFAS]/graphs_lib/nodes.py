# External imports
from abc import ABC
from typing import Generator, Iterable


# Abstract class representing a node
class ComponentNode(ABC):
    """
    Class representing a node.
    """

    # Block the initialization of the abstract component node
    def __init__(self) -> None:
        """
        Block the initialization of the abstract component node.
        """
        raise RuntimeError("Cannot initialize the abstract class ComponentNode.")


    # Return a string representation of the node
    def __repr__(self) -> str:
        """
        Return a string representation of the node.

        Returns:
            str: String representation of the node.
        """
        return self.__str__()


    # Return a hash value for the node
    def __hash__(self) -> int:
        """
        Return a hash value for the node.

        Returns:
            int: Hash value for the node.
        """
        return hash(self.__str__())
    

    # Do "equality" comparison with other object
    def __eq__(self, other:any) -> bool:
        """
        Do "equality" comparison with other object.

        Args:
            other (any): Another object to compare with.

        Returns:
            bool: True if both objects have the same string representation, False otherwise.
        """
        return str(self) == str(other)
    
    
    # Do "less than" comparison with other object
    def __lt__(self, other:any) -> bool:
        """
        Do "less than" comparison with other object

        Args:
            other (any): Another object to compare with.

        Returns:
            bool: True if the string representation of this object precedes the other, False otherwise.
        """
        return str(self) < str(other)
    
    
    # Do "greater than" comparison with other object
    def __gt__(self, other:any) -> bool:
        """
        Do "greater than" comparison with other object

        Args:
            other (any): Another object to compare with.

        Returns:
            bool: True if the string representation of this object procedes the other, False otherwise.
        """
        return str(self) > str(other)


    @staticmethod
    # Check if the given object is a node.
    def is_node(x: any) -> bool:
        """
        Check if the given object is a node.

        Args:
            x (any): The object to be checked.

        Returns:
            bool: True if the object is a node, False otherwise.
        """
        return isinstance(x, ComponentNode)


# Class representing a unitary node
class Node(ComponentNode):
    """
    Class representing a unitary node.

    Attributes:
        __data (any): The data to store in the node.
    """

    # Initialize the node
    def __init__(self, data:any) -> None:
        """
        Initialize the node.

        Args:
            data (any): The data to store in the node.
        """
        self.__data = data

    
    # Return a string representation of the node
    def __str__(self) -> str:
        """
        Return a string representation of the node.

        Returns:
            str: String representation of the node.
        """
        return self.__data.__str__()


    @property
    # Give the data of the node
    def data(self) -> any:
        """
        Give the data of the node.

        Returns:
            any: The data stored in the node.
        """
        return self.__data


    # Update the data of the node
    def update(self, data:any) -> None:
        """
        Update the data of the node.

        Args:
            data (any): The new data to be stored in the node.
        """
        self.__data = data


# Class representing a collection of nodes
class CompositeNode(ComponentNode):
    """
    Class representing a collection of nodes.

    Attributes:
        __nodes (list[Node]): List of nodes.
    """


    # Initialize the composite node
    def __init__(self, nodes:Iterable[Node]=None):
        """
        Initialize the composite node.

        Args:
            nodes (Iterable[Node], optional): An iterable of Node objects. Defaults to None.
        """
        if nodes is None:
            nodes = list()
        self.__nodes = list(nodes)

    
    # Return a string representation of the composite node
    def __str__(self) -> str:
        """
        Return a string representation of the composite node.

        Returns:
            str: String representation of the composite node.
        """
        return ", ".join(sorted([str(node) for node in self.__nodes]))
    
    
    # Return an iterator over the nodes in the composite node
    def __iter__(self) -> Generator[Node, None, None]:
        """
        Return an iterator over the nodes in the composite node.

        Yields:
            Node: The next node.
        """
        for node in self.__nodes:
            yield node

    
    # Get a node by index in the composite node
    def __getitem__(self, index:int) -> Node:
        """
        Get a node by index in the composite node.

        Args:
            index (int): The index of the node to be gotten.

        Returns:
            Node: The node at the specified index.
        """
        return self.__nodes[index]
    

    # Check if the given node is present in the composite node
    def __contains__(self, node:Node) -> bool:
        """
        Check if the given node is present in the composite node.

        Args:
            node (Node): The node to check for.

        Returns:
            bool: True if the node is present, False otherwise.
        """
        return node in self.__nodes


    # Get the number of nodes registered in the composite node
    def __len__(self) -> int:
        """
        Get the number of nodes registered in the composite node.

        Returns:
            int: The number of nodes registered in the composite node.
        """
        return len(self.__nodes)
    

    @property
    # Get a list of nodes registered in the composite node
    def nodes(self) -> tuple[Node]:
        """
        Get a list of nodes registered in the composite node.

        Returns:
            tuple: A list of nodes registered in the composite node.
        """
        return tuple(self.__nodes)
    

    # Insert a node in the composite node at the specified index
    def insert(self, node:Node, index:int=-1) -> None:
        """
        Insert a node in the composite node at the specified index.

        Args:
            node (Node): The node to be inserted.
            index (int, optional): The index at which to insert the node. Defaults to -1 (append).

        Raises:
            ValueError: If the object is not a Node instance.
        """
        if not isinstance(node, node):
            raise ValueError("Invalid node object found.")
        self.__nodes.insert(index, node)


    # Append a node to the composite node
    def append(self, node:Node) -> None:
        """
        Append a node to the composite node.

        Args:
            node (Node): The node to be appended.

        Raises:
            ValueError: If the object is not a Node instance.
        """
        self.insert(node)
    

    # Extend the composite node with multiple nodes
    def extend(self, nodes:Iterable[Node]) -> None:
        """
        Extend the composite node with multiple nodes.

        Args:
            nodes (Iterable[Node]): An iterable of Node objects.

        Raises:
            ValueError: If the object is not a Node instance.
        """
        for node in nodes:
            self.insert(node)
    

    # Remove a node in the composite node
    def remove(self, node:Node) -> None:
        """
        Remove a node in the composite node.

        Args:
            node (Node): The node to be removed.
        """
        self.__nodes.remove(node)
    

    # Pop a node by index in the composite node
    def pop(self, index:int=-1) -> Node:
        """
        Pop a node by index in the composite node.

        Args:
            index (int, optional): The index of the node to be popped. Defaults to -1 (last node).

        Returns:
            Node: The popped node.
        """
        return self.__nodes.pop(index)
    

    # Get the index of a node in the composite node
    def index(self, node:Node) -> None:
        """
        Get the index of a node in the composite node.

        Args:
            node (Node): The node to be found.

        Returns:
            int: The index of the node in the composite node.
        """
        self.__nodes.index(node)
    

    # Remove all nodes in the composite node
    def clear(self) -> None:
        """
        Remove all nodes in the composite node.
        """
        self.__nodes.clear()


# Entry point for running the script
if __name__ == "__main__":
    # Code for testing the node class and the composite node class
    composite = CompositeNode([Node("Lucas"), Node("Pedro"), Node("Ricardo")])
    for node in composite:
        print(node)

    print(composite)
    print(list(composite))
