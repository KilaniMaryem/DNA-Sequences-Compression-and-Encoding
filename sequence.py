import random

class Sequence:
    def __init__(self: object, path: str) -> None:
        self.path = path

    def __str__(self: object) -> str:
        return ""

    def __repr__(self: object) -> str:
        return "Sequence(%s)" % self.path
    #------------------------------------------------------------------------------------------------#
    def read(self: object) -> str:
        seq = ""
        with open(self.path, 'r') as file:
            for line in file:
                seq += line.strip("\n")
        return seq
    def write(self: object, content: str):
        with open(self.path, 'w') as file:
            file.writelines(content)
    #------------------------------------------------------------------------------------------------#
    def read_bytes(self: object) -> str:
        """This method is used to read a file that has been written in bytes,
        it will be useful when reading files that has been compressed with
        Huffman coding"""
        seq = ""
        with open(self.path, 'rb') as file:
            for line in file:
                seq += line.decode("utf-8")
        return seq
    def write_bytes(self: object, content: str) -> None:
        """Used when we want to write out the contents of the
        Huffman compression to a file."""
        with open(self.path, 'wb') as file:
            file.write(content.encode("utf-8"))
    #------------------------------------------------------------------------------------------------#
    @staticmethod
    def generate(length: int) -> str:
        return ''.join([random.choice('ATCGN') for _ in range(0, length, 1)])
