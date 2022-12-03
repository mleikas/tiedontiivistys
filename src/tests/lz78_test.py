import unittest
import lz78


class TestLZ78(unittest.TestCase):
    def setUp(self):
        self.testitiedostonpolku = "src/tests/testaus.txt"
        self.testitiedostonpolku2 = "src/tests/tulostus.txt"

    def test_pakkaus_lz78(self):
        lz78.lz_koodaus(self.testitiedostonpolku, self.testitiedostonpolku2)
        pakattu = open(self.testitiedostonpolku2,"r")
        self.assertEqual(pakattu.read(), '\x00a\x00s\x00d\x00f\x00\n\x00')

    def test_purkaminen_lz78(self):
        lz78.lz_koodaus(self.testitiedostonpolku, self.testitiedostonpolku2)
        lz78.lz_dekoodaus(self.testitiedostonpolku2)
        purettu = open("src/tests/tulostus.txt_purettu-lz.txt","r")
        self.assertEqual(purettu.read(), 'asdf\n')
