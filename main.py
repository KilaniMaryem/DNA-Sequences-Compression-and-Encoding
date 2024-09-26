import sys
import os
from encoder import FullEncoder
from decoder import FullDecoder
from sequence import Sequence

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [encode|decode|generate] [file_path or length]")
        return

    operation = sys.argv[1]

    # Handle DNA sequence generation
    if operation == "generate":
        if len(sys.argv) != 3:
            print("Usage: python main.py generate [length]")
            return
        
        length = int(sys.argv[2])
        random_sequence = Sequence.generate(length)
        file_path = 'random_sequence.txt'

        # Write the generated sequence to a file
        Sequence(file_path).write(random_sequence)
        print(f"Generated random sequence of length {length}:")
        print(random_sequence)

        # Encode the random sequence
        encoder = FullEncoder(file_path)
        encoder.compress_and_encode()
        print("\nEncoded sequence saved to file.\n")

        # Decode the encoded sequence
       
        decoder = FullDecoder(file_path)
       
        decoder.decode_and_decompress()
       
        decoded_sequence = Sequence(file_path).read()
        print("\nDecoded sequence:")
        print(decoded_sequence)

        # Check if the original and decoded sequences match
        if random_sequence == decoded_sequence:
            print("\nSuccess: The original and decoded sequences match.")
        else:
            print("\nError: The original and decoded sequences do not match.")
    #-------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------#
    # Handle encoding and decoding as before
    elif operation == "encode":
        if len(sys.argv) != 3:
            print("Usage: python main.py encode [file_path]")
            return

        file_path = sys.argv[2]
        print(f"Encoding file: {file_path}")
        encoder = FullEncoder(file_path)
        encoder.compress_and_encode()
        print("Encoding complete.")
    #-------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------#
    elif operation == "decode":
        if len(sys.argv) != 3:
            print("Usage: python main.py decode [file_path]")
            return

        file_path = sys.argv[2]
        print(f"Decoding file: {file_path}")
        decoder = FullDecoder(file_path)
        decoder.decode_and_decompress()
        print("Decoding complete.")

    else:
        print("Invalid operation. Use 'encode', 'decode', or 'generate'.")

if __name__ == "__main__":
    main()
