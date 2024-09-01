import os
import sys

from graphs import adj_list_graph
from io import TextIOWrapper
from pathlib import Path


class contacts_analyzer:

    # Initialize the contacts analyzer
    def __init__(self) -> None:
        self.__graph = adj_list_graph(is_directed=True, is_weighted=True)


    # Return the graph as a string representing the contacts analyzer
    def __str__(self) -> str:
        return self.__graph.__str__()


    # Build the inner data based on a given folder with valid data
    def build_data(self, path:str) -> None:
        # Format the path
        path = path.strip("/\\")
        pathf = Path(os.path.dirname(sys.argv[0]), path)

        file_counter = [0, 0]  # Counter of total files searched and files searched in the current folder
        invalid_files = 0  # Counter of the invalid files

        # For each mail folder in the sample
        for mail_folder in pathf.glob(pattern="*/*"):
            # print(os.path.basename(mail_folder), len(list(Path(mail_folder).glob(pattern="*"))))
            
            # For each mail file, add an edge to the graph based on sender and receiver
            for mail_file in Path(mail_folder).rglob(pattern="*"):
                # Update counter of files searched in the current folder
                file_counter[1] += 1
                print(*file_counter)

                try:
                    # Verify if is a file (to avoid any error when reading)
                    if mail_file.is_file():
                        # Try to open the file found
                        with open(mail_file, "r") as file:
                            # Try to find the sender and the receiver based on a prefix
                            sender = contacts_analyzer.__get_line_with_prefix(file, "From:")
                            file.seek(0)
                            receivers = contacts_analyzer.__get_line_with_prefix(file, "To:", ", ")

                            # Only add a edge if both, sender and receivers, were found
                            if sender and receivers:
                                # Format the sender and the receivers
                                sender = sender.removeprefix("From: ").replace("\n", "")
                                receivers = receivers.removeprefix("To: ").replace("\n", "").replace("\t", "")

                                # For each receiver, add/update edge in the graph
                                for receiver in receivers.split(", "):
                                    # Add a edge from the sender to the receiver or update the weight of the existing edge
                                    weight = self.__graph.edge_weight(sender, receiver) + 1 if self.__graph.has_edge(sender, receiver) else 1
                                    self.__graph.add_edge(sender, receiver, weight)
                            elif sender:
                                # Format the sender
                                sender = sender.removeprefix("From: ").replace("\n", "")

                                # Add a node in the graph for the sender
                                self.__graph.add_node(sender)
                            elif receivers:
                                # Format the receivers
                                receivers = receivers.removeprefix("To: ").replace("\n", "").replace("\t", "")

                                # For each receiver, add a node in the graph
                                for receiver in receivers.split(", "):
                                    self.__graph.add_node(receiver)
                            else:
                                # Count the total invalid files
                                invalid_files += 1
                            file.close()
                except Exception as error:
                    print(f"File \"{mail_file}\" skipped due to error.", str(error).upper())
            
            # Update counter of total files searched
            file_counter[0] += file_counter[1]
            file_counter[1] = 0
        
        print(f"{file_counter[0]} total files searched.")
        print(f"{invalid_files} invalid files were ignored.")
        print("Data built sucessfully.")


    # Return the amount of contacts registered
    def amount_contacts(self) -> int:
        return self.__graph.get_order()


    # Return the amount of messages exchanged
    def amount_messages(self) -> int:
        return self.__graph.get_size()


    # Return the biggest senders of messages
    def biggest_senders(self, amount:int=0, unique_receivers=False) -> tuple[str, int]:
        senders = dict([(node, int(0)) for node in self.__graph.nodes()])

        # For each sender in the graph, calculates the amount of sent messages
        for sender, _, weight in self.__graph.edges():
            senders[sender] +=  1 if unique_receivers else int(weight)
        
        # Sort data by decreasing order
        senders = sorted(senders.items(), key=lambda x: x[1], reverse=True)
        
        # Return the amount passed of senders
        if amount > 0:
            return tuple(senders[:amount])
        else:
            # Return all if amount <= 0
            return tuple(senders)


    # Return the biggest receivers of messages
    def biggest_receivers(self, amount:int=1, unique_senders=False) -> tuple[str]:
        receivers = dict([(node, int(0)) for node in self.__graph.nodes()])

        # For each receiver in the graph, calculates the amount of received messages
        for _, receiver, weight in self.__graph.edges():
            receivers[receiver] += 1 if unique_senders else int(weight)
        
        # Sort data by decreasing order
        receivers = sorted(receivers.items(), key=lambda x: x[1], reverse=True)
        
        # Return the amount passed of receivers
        if amount > 0:
            return tuple(receivers[:amount])
        else:
            # Return all if amount <= 0
            return tuple(receivers)


    # Check if the contacts graph is a Eulerian graph and returns the reason
    def is_contacts_graph_eulerian(self) -> tuple[bool, tuple[str]]:
        if self.__graph.is_eulerian():
            return (True, tuple())
        else:
            reasons = list()
            for node in self.__graph.nodes():
                if self.__graph.outdegree != self.__graph.indegree(node):
                    reasons.append("\tTem pelo menos um nó com grau de saída diferente do grau de entrada")
                    break
            if not self.__graph.is_connected():
                reasons.append("\tGrafo desconectado")
            return (False, tuple(reasons))
    

    # Return a path from one contact to another if possible
    def get_path_between_contacts(self, contact_start:str, contact_end:str) -> tuple[str]|None:
        return self.__graph.breadthfirst_search(contact_start, contact_end)

    
    # Return near contacts based on a distance passed
    def get_near_contacts(self, contact:str, distance:int):
        return self.__graph.breadthfirst_search(contact, distance=distance)
    

    # Return the diameter
    def get_diameter(self) -> tuple[tuple[str], float]|None:
        return self.__graph.diameter()


    # Return the first line with the prefix in the TextIOWrapper
    @staticmethod
    def __get_line_with_prefix(text_io:TextIOWrapper, prefix:str, unwrap_sufix:str|None=None) -> str|None:
        # While prefix doesn't match, skip line
        line = text_io.readline()
        while not line.startswith(prefix):
            line = text_io.readline()

            # If no left line, return None
            if not line:
                return None
        
        # If a valid sufix is given
        if unwrap_sufix:
            # If line ends with the valid sufix, continue to unwrap lines and adding them together
            while line.endswith(unwrap_sufix + "\n"):
                line += text_io.readline()
        
        return line


# Output some data into a file
def output(data:str, path:str=".", filename:str="output.txt") -> None:
    # Format the path
    path = path.strip("/\\")
    pathf = Path(os.path.dirname(sys.argv[0]), path, filename)

    # Try to save the data on the file passed
    try:
        with open(pathf.as_posix(), mode=("x" if not pathf.is_file() else "w"), encoding="UTF-8") as file:
            file.write(data.__str__() + "\n")
            file.close()
    except Exception as error:
        print("Failed to output data.", str(error).upper())
