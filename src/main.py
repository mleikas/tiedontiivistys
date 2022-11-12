"""
Pääohjelma
"""

import huffman

def main():
    """
    Käynnistää algoritmit
    """
    print("Anna tiedosto, joka pakataan: ")
    tekstitiedosto = open("testiteksti.txt", "r")

    data = tekstitiedosto.read()
    print(data)
    huffman.Huffman_Encoding(data)

if __name__ == "__main__":
    main()
