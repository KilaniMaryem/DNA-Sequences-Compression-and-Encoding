import os
from sequence import Sequence
from burros_wheeler import BurrosWheeler
from huffman import HuffmanTree

class HuffDecoder:
    def __init__(self: object, path: str):
        p=os.path.splitext(path)[0]
        if '_bwt_compressed.txt' not in path:
         self.path = p + '_bwt_compressed.txt'
        else:
         self.path = path
        self.seq = Sequence(self.path)
        self.dehuffman_output = p + '_dehuff.txt'
        self.binary = None
        self.header = None
        self.unicode = None
        self.decompressed = None
    #------------------------------------------------------------------------------------------------#
    def decode(self: object) :
        seq = self.seq.read_bytes()
        self.header = seq[:seq.index('+')]
        self.unicode = seq[seq.index('+')+1:]
        codes = HuffmanTree.get_codes_from_header(self.header)
        #binary = HuffmanTree.from_UTF8unicode_to_binary_string(self.unicode)
        binary=self.unicode
        padding = int(codes['pad'])
        self.binary = HuffmanTree.remove_padding(binary, padding)
        self.decompressed = HuffmanTree.binary_string_to_sequence(self.binary,codes)
        Sequence(self.dehuffman_output).write(self.decompressed)

#-------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------#
class BWDecoder:
    def __init__(self: object, path: str):
        self.path = os.path.splitext(path)[0]
        self.seq = Sequence(self.path+'.txt')
        self.debwt_output = self.path + '_debwt.txt'
        self.bwm = None
        self.original = None
    #------------------------------------------------------------------------------------------------#    
    def decode(self: object):
        self.bwm = list(BurrosWheeler.get_bwm_matrix_from_transform(self.seq.read()))
        self.original = BurrosWheeler.get_original_sequence_from_bwm_matrix(self.bwm[-1])
        Sequence(self.debwt_output).write(self.original)
#-------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------#
class FullDecoder:
    def __init__(self: object, path: str):
        self.path = path
        self.huff_decoder = None
        self.bw_decoder = None
        
    def decode_and_decompress(self: object):
        #Decode the sequence with Huffman decompression
        self.huff_decoder = HuffDecoder(self.path)
        self.huff_decoder.decode()
        #obtain the original sequence by doing the Inverse of Burros-Wheeler transform on the decompressed seq
        self.bw_decoder = BWDecoder(self.huff_decoder.dehuffman_output)
        self.bw_decoder.decode()
