import unittest
import huffman
import tempfile
import os

class TestHuffman(unittest.TestCase):
    def setUp(self):
        self.testitiedostonpolku = "src/tests/testaus.txt"
        with open(self.testitiedostonpolku, "r", encoding="utf-8") as tekstitiedosto:
            self.data = tekstitiedosto.read()
        self.koodattu_tulos = b'010101'
        self.solmu = huffman.Solmu(0, "A")

    def test_huffman_pakkaus_biteiksi(self):
        binaarikoodi, puu = huffman.huffman_koodaus(self.data)
        self.assertEqual(puu, b'0001f1\n01h1b001g1d01s1a_')
        self.assertEqual(binaarikoodi,b"\x05\xfa\x88\xc2\x01")

    def test_huffman_purkaminen_stringiksi(self):
        with tempfile.TemporaryDirectory() as tempdir:
            binaarikoodi, puu = huffman.huffman_koodaus(self.data)
            with open(os.path.join(tempdir, "testaus.txt_pakattu-huffman.txt"),
            "wb") as binaaritiedosto:
                binaaritiedosto.write(puu)
                binaaritiedosto.write(binaarikoodi)

            with open(os.path.join(tempdir, "testaus.txt_pakattu-huffman.txt"),
            "rb") as koodattutiedosto:
                data = koodattutiedosto.read()
            string = huffman.huffman_dekoodaus(data)
            self.assertEqual(string, "asdfgbfh\n")

    def test_huffman_bitit_byteiksi(self):
        tavuja = huffman.bititbyteiksi(self.koodattu_tulos)
        bytelista = [2, 21]
        self.assertEqual(tavuja, bytelista)

    def test_laske_tod_empty_input(self):
        data = ""
        odotettu_tulos = {}
        self.assertEqual(huffman.laske_tod(data), odotettu_tulos)

    def test_single_element(self):
        data = "a"
        odotettu_tulos = {"a": 1}
        self.assertEqual(huffman.laske_tod(data), odotettu_tulos)

    def test_existing_element(self):
        data = "aa"
        odotettu_tulos = {"a": 2}
        self.assertEqual(huffman.laske_tod(data), odotettu_tulos)
