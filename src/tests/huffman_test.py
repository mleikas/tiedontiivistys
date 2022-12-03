import unittest
import huffman


class TestHuffman(unittest.TestCase):
    def setUp(self):
        self.testitiedostonpolku = "src/tests/testaus.txt"
        with open(self.testitiedostonpolku, "r", encoding="utf-8") as tekstitiedosto:
                self.data = tekstitiedosto.read()
    def test_huffman_pakkaus_biteiksi(self):
        binaarikoodi, puu = huffman.huffman_koodaus(self.data)
        self.assertEqual(puu, b'0001s1a1\n01f1d_')
        self.assertEqual(binaarikoodi,b"\x04#\t")
        
    
    def test_huffman_purkaminen_stringiksi(self):
        binaarikoodi, puu = huffman.huffman_koodaus(self.data)
        with open("src/tests/testaus.txt_pakattu-huffman.txt", "wb") as binaaritiedosto:
            binaaritiedosto.write(puu)
            binaaritiedosto.write(binaarikoodi)

        with open("src/tests/testaus.txt_pakattu-huffman.txt", "rb") as koodattutiedosto:
            data = koodattutiedosto.read()
        string = huffman.huffman_dekoodaus(data)
        self.assertEqual(string, "asdf\n")
