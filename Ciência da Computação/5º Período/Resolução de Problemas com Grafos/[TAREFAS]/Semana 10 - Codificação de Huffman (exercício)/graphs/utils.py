from graphs import graphs


def huffman_encoder(string:str) -> tuple[graphs.adj_list_graph, bytes]:
    # 1. Counting the occurrences of each caracter
    char_occurs = {char: 0 for char in string}
    for char in string:
        char_occurs[char] += 1

    # 2. Creating the key graph (Huffman Tree) to encode the string
    key = graphs.adj_list_graph(is_weighted=False)
    occurs_items = []
    for char, occurs in char_occurs.items():
        key.add_node(char)
        occurs_items.append((occurs, char))
    
    # 3. Building the key graph
    while len(occurs_items) > 1:
        # Reorder the occurrences
        occurs_items.sort()

        # Take the two first elements
        first_elem = occurs_items.pop(0)
        second_elem = occurs_items.pop(0)

        # Combine the two elements and put the combination back to the list
        new_elem = (first_elem[0] + second_elem[0], first_elem[1] + second_elem[1])
        occurs_items.append(new_elem)

        # Add a new node with edges to the previous two elements' nodes to the key graph
        key.add_edge(new_elem[1], first_elem[1])
        key.add_edge(new_elem[1], second_elem[1])
    
    # 4. Get root node based on the last element
    key_root = occurs_items[0][1]
    
    # 5. Create a dictionary with the new codes for each caracter based on the key graph
    encoded_chars = {char: "" for char in string}
    for char in encoded_chars.keys():
        path = key.dijkstra(key_root, char)[0]  # Get the path from the key root to the leaf node
        encoded_path = ""
        for i in range(len(path) - 1):
            adj_nodes = key.out_nodes(path[i]) # Get the outgoing nodes from the current node
            if len(adj_nodes) <= 0:
                continue
            elif path[i + 1] == sorted(adj_nodes)[0]:  # Next node is the left node
                encoded_path += "0"
            else:  # Next node is the right node
                encoded_path += "1"
        encoded_chars[char] = encoded_path
    
    # 6. Encode the string based on the key graph
    encoded_string = bytearray()
    # Adds the encoded chars to the buffer (and add a new most significant digit for identifying the start)
    buffer = "1" + "".join([encoded_chars[char] for char in string])

    # Consume the buffer in groups of 7 bits (compatible with ASCII)
    while len(buffer) > 0:
        encoded_char = chr(int(buffer[-7:], 2))
        encoded_string = bytes(encoded_char, encoding="ascii") + encoded_string
        buffer = buffer[:-7]  # Removes the last bits (already consumed)
    
    return key, bytes(encoded_string)


def huffman_decoder(key:graphs.adj_list_graph, encoded_string:bytes) -> str:
    # 1. Convert the bytes into a sequence of bits
    bit_sequence = ""
    for byte in encoded_string:
        bit_sequence += bin(byte)[2:].zfill(7)

    # Remove up to the most significant digit (it only identified the start of the sequence)
    bit_sequence = bit_sequence[bit_sequence.find("1") + 1:]

    # 2. Get the key graph root (only node with no ingoing nodes)
    key_root = None
    for node in key.nodes():
        if len(key.in_nodes(node)) <= 0:
            key_root = node
            break
    if not key_root:
        raise ValueError("No root identified in key graph")

    # 3. Follow key graph based on the bit sequence and decode the bytes
    decoded_string = ""
    cur_node = key_root
    cur_bit = 0
    while cur_bit < len(bit_sequence):
        adj_nodes = key.out_nodes(cur_node) # Get the outgoing nodes from the current node
        if len(adj_nodes) <= 0:  # Leaf node found
            decoded_string += cur_node
            cur_node = key_root
            continue  # Skip jumping to next bit
        elif bit_sequence[cur_bit] == "0":  # Follow the left node
            cur_node = sorted(adj_nodes)[0]
        elif bit_sequence[cur_bit] == "1":  # Follow the right node
            cur_node = sorted(adj_nodes)[1]
        cur_bit += 1
    decoded_string += cur_node

    return decoded_string


if __name__ == "__main__":
    from sys import getsizeof

    print()

    string = "Lucas Azevedo Dias"
    print(f"Original string: {string} ({getsizeof(string)}B)")

    key, encoded_string = huffman_encoder(string)
    print(f"Encoded string: {encoded_string} ({getsizeof(encoded_string)}B)")
    print(f"Key:\n{key} ({getsizeof(key)}B)")

    print()

    print(f"Was it able to reconstruct the original string?: {'SIM' if string == huffman_decoder(key, encoded_string) else 'NÃO'}")

    print()

    print(f"Compression ratio: {100 * (getsizeof(encoded_string) / getsizeof(string)):.2f}%")
    print(f"Compression ratio with key: {100 * ((getsizeof(key) + getsizeof(encoded_string)) / getsizeof(string)):.2f}%")

    print()
