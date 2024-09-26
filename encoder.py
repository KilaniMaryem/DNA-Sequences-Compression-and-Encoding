import os
from sequence import Sequence
from burros_wheeler import BurrosWheeler
from huffman import HuffmanTree

class BWEncoder:
    def __init__(self: object, path: str):
        self.path = os.path.splitext(path)[0]
        self.seq = Sequence(path)
        self.bwt_output = self.path + '_bwt.txt'
        self.rotations = None
        self.bwm = None
        self.bwt = None
    #------------------------------------------------------------------------------------------------#
    def encode(self: object):
        self.rotations = list(BurrosWheeler.string_rotations(self.seq.read()))
        self.bwm = BurrosWheeler.construct_bwm_matrix(self.rotations[-1])
        self.bwt = BurrosWheeler.get_bwt_encoding(self.bwm)
        Sequence(self.bwt_output).write(self.bwt)
#-------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------#
class HuffEncoder:
    def __init__(self: object, path: str):
        self.path = os.path.splitext(path)[0]#path of the file to be compressed
        self.seq = Sequence(path)
        self.huff_output = self.path + '_compressed.txt'
        self.binary = None
        self.header = None
        self.unicode = None
        self.compressed = None
    #------------------------------------------------------------------------------------------------#
    def encode(self: object):
        tree = HuffmanTree(self.seq.read())
        tree.code(tree.root)
        self.binary = tree.from_sequence_to_binary_string()
        self.unicode = HuffmanTree.from_binary_string_to_UTF8unicode(self.binary)
        self.header = tree.write_codes_to_header()
        #self.compressed =  self.header + self.unicode
        self.compressed =  self.header + self.binary
        Sequence(self.huff_output).write_bytes(self.compressed)

#-------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------#
class FullEncoder:
    def __init__(self: object, path: str):
        self.path = path #path of the file to be compressed with BWT + Huffman
        self.bw_encoder = None
        self.huff_encoder = None
    #------------------------------------------------------------------------------------------------#
    def compress_and_encode(self: object):
        self.bw_encoder = BWEncoder(self.path)
        self.bw_encoder.encode()
        
        self.huff_encoder = HuffEncoder(self.bw_encoder.bwt_output)
        self.huff_encoder.encode()
