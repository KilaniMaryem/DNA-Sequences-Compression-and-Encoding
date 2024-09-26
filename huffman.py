from typing import Dict

class HuffmanNode:
    def __init__(self: object, char: str, freq: int, left: object=None, right: object=None) -> None:
 
        self.char = char
        self.freq = freq
        self.__left_child = left
        self.__right_child = right
        self.dir = '' #path of the current node in the Huffman tree (binary string)
    #------------------------------------------------------------------------------------------------#
    @property
    def right_child(self: object) -> object:
        return self.__right_child
    @property
    def left_child(self: object) -> object:
        return self.__left_child
    @right_child.setter
    def right_child(self: object, right_child: object) -> None:
        self.__right_child = right_child
    @left_child.setter
    def left_child(self: object, left_child: object) -> None:
        self.__left_child = left_child
    #------------------------------------------------------------------------------------------------#
    def __str__(self: object) -> str:
        return ""

    def __repr__(self: object) -> str:
        return "Node(%s, freq=%s, right=%s, left=%s)"%(self.char,self.freq,self.right_child,self.left_child)
    

#-------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------#
class HuffmanTree:
    def __init__(self: object, sequence: str) -> None:
        self.sequence = sequence #the Burros-Wheeler transform of the sequence to be encoded
        self.frequency = HuffmanTree.freq_dict(self.sequence)#A dict to store : the char as a key and its freq as a value.
        self.root = self.create_tree()
        self.codes = {}#The Huffman codes for a given sequence: The char as a key and its tree path as a value

    @staticmethod
    def freq_dict(sequence: str) -> Dict[str, int]:
        f_dict = {}
        for char in sequence:
            if char in f_dict.keys():
                f_dict[char] += 1
            else:
                f_dict[char] = 1
        return f_dict
    #------------------------------------------------------------------------------------------------#
    def create_tree(self: object) -> HuffmanNode:
        leafs = [] 
        for char, freq in self.frequency.items():
            leafs.append(HuffmanNode(char, freq))

        while len(leafs) > 1: 

            leafs = sorted(leafs, key=lambda x: x.freq) 
            left = leafs.pop(0) 
            left.dir = "0" 
            right = leafs.pop(0) 
            right.dir = "1" 
            new_char = left.char + right.char
            new_freq = left.freq + right.freq 
            new_node = HuffmanNode(new_char, new_freq, left, right) 
            leafs.append(new_node)
        return leafs[0]
    #------------------------------------------------------------------------------------------------#
    def code(self: object, node: HuffmanNode, val: str='') -> None:
        curr_path = val + node.dir # the current path in the recursion
        if node.left_child:
            self.code(node.left_child, curr_path)
        if node.right_child:
            self.code(node.right_child, curr_path)

        if not node.left_child and not node.right_child:
            self.codes[node.char] = curr_path

    #------------------------------------------------------------------------------------------------#
    def from_sequence_to_binary_string(self: object) -> str:
        """Adds a padding to the end of the binary sequence (a variable
        number of zeroes, when sequence is divisible by 8 then add 8 zeroes
        by default). The binary sequence will be coded in 8-bits later.
        """
        bin_str = ""
        for char in self.sequence:
            bin_str += self.codes[char]

        pad = 8 - len(bin_str) % 8
        if pad != 0:
            for _ in range(0, pad, 1):
                bin_str += '0'

        self.codes['pad'] = str(pad) 
        return bin_str
    #------------------------------------------------------------------------------------------------#
    @staticmethod
    def from_binary_string_to_UTF8unicode(bin_str: str) -> str:
        unicode = ""
        for bit in range(0, len(bin_str), 8): 
            eight_bits = bin_str[bit:bit+8]
            code = int(eight_bits, 2)
            unicode += chr(code)
        return unicode
    #------------------------------------------------------------------------------------------------#
    @staticmethod
    def from_UTF8unicode_to_binary_string(unicode: str) -> str:
        bin_str = ""
        for uni in unicode:
            code = ord(uni)
            bin_str += '{:08b}'.format(code)

        return bin_str
    #------------------------------------------------------------------------------------------------#
    @staticmethod
    def remove_padding(bin_str: str, pad: int) -> str:
        return bin_str[:-pad] 
    #------------------------------------------------------------------------------------------------#
    @staticmethod
    def binary_string_to_sequence(bin_str: str, codes: Dict[str, str]) -> str:
        original_seq,reading_stream = "",""
        for num in bin_str:
            reading_stream += num
            for char, path in codes.items():
                if path == reading_stream:
                    original_seq += char
                    reading_stream = ""
                    break

        return original_seq
    #------------------------------------------------------------------------------------------------#
    def write_codes_to_header(self: object) -> str:
        header = ""
        for char, path in self.codes.items():
            header += char + "," + path + ";"

        return header + "+"
    #------------------------------------------------------------------------------------------------#
    @staticmethod
    def get_codes_from_header(header: str) -> Dict[str, str]:
        reconstructed_codes = {}
        for code in header.split(";")[:-1]:
            char, path = code.split(",")
            reconstructed_codes[char] = path
        return reconstructed_codes
