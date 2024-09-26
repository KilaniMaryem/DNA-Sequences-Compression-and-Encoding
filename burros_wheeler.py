from typing import List, Tuple

class BurrosWheeler:
    @staticmethod
    def pprint(mat: List[str]) -> None:
        for line in mat:
            print(*line, sep="") 
    #------------------------------------------------------------------------------------------------#
    @staticmethod
    def string_rotations(seq: str) :
        seq += '$'
        double_seq = seq * 2
        all_rotations = []

        for i in range(0, len(seq), 1):

            rot = double_seq[i:i+len(seq)]
            all_rotations.append(rot)

            yield [rot for rot in all_rotations]
    #------------------------------------------------------------------------------------------------#
    @staticmethod
    def construct_bwm_matrix(rotations: List[str]) -> List[str]:
        return sorted(rotations)
    #------------------------------------------------------------------------------------------------#
    @staticmethod
    def get_original_sequence_from_bwm_matrix(matrix: List[str]) -> str:
        """Burrows-Wheeler Matrix-->original sequence"""

        seq = ""
        for line in matrix: 
            if line[-1] == "$":
                seq += line
        return seq[:-1] 
    #------------------------------------------------------------------------------------------------#
    @staticmethod
    def get_bwt_encoding(matrix: List[str]) -> str:
        last_column = [line[-1] for line in matrix]
        transformed_seq = ''.join(last_column)
        return transformed_seq
    #------------------------------------------------------------------------------------------------#
    @staticmethod
    def get_bwm_matrix_from_transform(bwt: str) :
        """Burros-Wheeler Transform--> Matrix"""
        bwm = []
        for _ in range(0, len(bwt), 1):
            bwm.append('')

        for _ in range(0, len(bwt), 1):

            for i in range(0, len(bwt), 1):
                bwm[i] = bwt[i] + bwm[i]
 
            yield [line for line in bwm]
            bwm.sort()
            yield [line for line in bwm]
    #------------------------------------------------------------------------------------------------#
    @staticmethod
    def suffix_array(sequence: str) -> List[Tuple[str, int]]:
        sequence += '$'
        suff_arr = []
        for i in range(0, len(sequence), 1):
            suff_arr.append((sequence[i:], i))

        return sorted(suff_arr)
    #------------------------------------------------------------------------------------------------#
    @staticmethod
    def bwt_advanced(sequence: str) -> str:
        """Advanced Burrows-Wheeler Transform (uses suffix_array )"""
        bwt = []
        for suff in BurrosWheeler.suffix_array(sequence):
            i = suff[1] 
            if i == 0:
                bwt.append('$')
            else:
                bwt.append(sequence[i - 1])

        return ''.join(bwt)
