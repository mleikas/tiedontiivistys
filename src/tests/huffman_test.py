import unittest
import huffman


class TestHuffman(unittest.TestCase):
    def setUp(self):
        pass
    def test_huffman_pakkaus_biteiksi(self):
        binaarikoodi, puu = huffman.huffman_koodaus("ABC")
        self.assertEqual(binaarikoodi,b"01001")
