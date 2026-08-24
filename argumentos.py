"""
este modulo es un comentario  
Author: Astorga Gaona jesus Francisco
Date: 2024-08-17
"""

import argparse

def main():
    """Este modulo es un comentario
    Python argumentos.py -n klaatu -s 55
    Python argumentos.py --name celes -- 100
    """
    parser = argparse.ArgumentParser(description="parse command-line arguments and options.")
    #add arguments
    parser.add_argument('-n','--name', type=str, required=True, help='Full name of student')
    parser.add_argument('-s','--score of student')
    args = parser.parser_args()
    # Print the parsed arguments
    Print(f"Name: {args.name}")
    Print(f"Score: {args.score}")

if __name__ == "__main__":
    main()
