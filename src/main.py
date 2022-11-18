"""
Pääohjelma
"""

import os
import huffman

def main():
    """
    Käynnistää algoritmit
    """
    tekeminen = input("Huffman pakkaaminen: PAINA 1 \nHuffman purkaminen: PAINA 2\n")
    if str(tekeminen) == "1":
        polku = input("Anna polku tiedostolle, joka pakataan: ")
        with open(polku, "r", encoding="utf-8") as tekstitiedosto:
            data = tekstitiedosto.read()

        binaarikoodi, puu = huffman.huffman_koodaus(data)
        polku_huffman_tiedosto = f"{os.path.basename(os.path.normpath(polku))}.txt"

        with open(polku_huffman_tiedosto, "wb") as binaaritiedosto:
            binaaritiedosto.write(puu)
            binaaritiedosto.write(binaarikoodi)

        print(f"Pakattu tiedosto on polussa: {polku_huffman_tiedosto}")

    elif str(tekeminen) == "2":
        polku = input("Anna polku tiedostolle, joka puretaan: ")
        with open(polku, "rb") as koodattutiedosto:
            data = koodattutiedosto.read()
        puu = "Ei vielä mikään"
        purettu = huffman.huffman_dekoodaus(data, puu)
        polku_huffman_purettu = f"{os.path.basename(os.path.normpath(polku))}.txt"
        with open(polku_huffman_purettu, "wb") as tekstitiedosto:
            tekstitiedosto.write(purettu)

    else:
        main()

if __name__ == "__main__":
    main()
