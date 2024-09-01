from graphs.utils import huffman_decoder, huffman_encoder


if __name__ == "__main__":
    from os import system
    from sys import getsizeof

    strings = [
        "Lucas Azevedo Dias",
        "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAooooooooooooooooooooooooo",
        "ABCdefGHIjklMNOpqrstuVWXyz"
    ]

    for string in strings:

        system("cls")

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

        input("<Press any key to continue>")
