"""
Pääohjelma
"""

import os
import codecs

import huffman
import lz78

def main():
    """
    Käynnistää algoritmit
    """
    while True:
        tekeminen = input("Huffman pakkaaminen: PAINA 1 \n"
        "Huffman purkaminen: PAINA 2\nLZ78 pakkaaminen PAINA 3"
        "\nLZ78 purkaminen PAINA 4\nOhjelma kiinni PAINA JOTAIN MUUTA\n")

        if str(tekeminen) == "1":
            huffman_pakkaus()

        elif str(tekeminen) == "2":
            huffman_purku()

        elif str(tekeminen) == "3":
            lz78_pakkaus()

        elif str(tekeminen) == "4":
            lz78_purku()

        else:
            break


def huffman_pakkaus():
    """
    Funktio huffman pakkaamiseen
    """
    polku = input("Anna polku tiedostolle, joka pakataan: ")
    with codecs.open(polku, "r", encoding="utf-8") as tekstitiedosto:
        data = tekstitiedosto.read()

    binaarikoodi, puu = huffman.huffman_koodaus(data)
    polku_huffman_tiedosto = \
        f"{os.path.basename(os.path.normpath(polku))}_pakattu-huffman.txt"

    with codecs.open(polku_huffman_tiedosto, "wb") as binaaritiedosto:
        binaaritiedosto.write(puu)
        binaaritiedosto.write(binaarikoodi)
    alkuperainen_koko = os.path.getsize(polku)
    tulostuksen_koko = os.path.getsize(polku_huffman_tiedosto)
    print(f"Koko alussa: {alkuperainen_koko} biteissä)\n"
    f"Koko lopussa: {tulostuksen_koko} (biteissä)")

    print(f"Pakattu tiedosto on polussa: {polku}")

def huffman_purku():
    """
    Funktio huffman purkamiseen
    """
    polku = input("Anna polku tiedostolle, joka puretaan: ")
    with open(polku, "rb") as koodattutiedosto:
        data = koodattutiedosto.read()
    purettu = huffman.huffman_dekoodaus(data)
    polku_huffman_purettu = \
        f"{os.path.basename(os.path.normpath(polku))}_purettu-huffman.txt"

    with open(polku_huffman_purettu, "w", encoding="utf-8") as tekstitiedosto:
        tekstitiedosto.write(purettu)

    print(f"Purettu tiedosto on polussa: {polku}")

def lz78_pakkaus():
    """
    Funktio LZ78 pakkaamiseen
    """
    polku = input("Anna polku tiedostolle, joka pakataan: ")
    tulostuspolku = f"{os.path.basename(os.path.normpath(polku))}_pakattu-lz.txt"
    alkuperainen_koko = os.path.getsize(polku)

    lz78.lz_koodaus(polku, tulostuspolku)
    tulostuksen_koko = os.path.getsize(tulostuspolku)
    print(f"Koko alussa: {alkuperainen_koko} (biteissä)\n"
    f"Koko lopussa: {tulostuksen_koko} (biteissä)")
    print(f"Pakattu tiedosto on polussa: {polku}")

def lz78_purku():
    """
    Funktio LZ78 purkamiseen
    """
    polku = input("Anna polku tiedostolle, joka pakataan: ")
    tulostuspolku = f"{os.path.basename(os.path.normpath(polku))}_purettu-lz.txt"
    lz78.lz_dekoodaus(polku)

    print(f"Purettu tiedosto on polussa: {tulostuspolku}")

if __name__ == "__main__":
    main()
