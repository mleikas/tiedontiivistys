# Testausdokumentti
## Yksikkötestaus
Pytestiä käyttämällä testataan ohjelman toimintaa.

Testeille on tehty omat tiedostot: https://github.com/mleikas/tiedontiivistys/tree/main/src/tests


huffman_test: testaa huffman algoritmin toimintaa
Sille annetaan string muotoinen syöte "asdf" ja ohjelma muodostaa sille tavu muodossa olevan stringin.
Tämä tarkistetaan halutun tavun kanssa.

Purkaminen myös testataan siten, että aluksi tehdään pakattu tiedosto samaan tapaan kuin äskeisessä testissä ja sitten tämä puretaan, jotta saadaan takaisin string "asdf"

lz78_test: testaa LZ78 algoritmin toimintaa
Sille annetaan polut kahteen tiedostoon: datatiedosto, tulostustiedosto
Datatiedostossa on tekstiä ja tulostustiedostoon tulee pakattu versio ohjelman.
Tulostustiedostosta katsotaan onko se halutussa muodossa.

Purkaminen testataan siten, että ensin tehdään pakattu tiedosto samaan tapaan kuin äskeisessä testissä ja sitten pakattu tiedosto puretaan, jotta saadaan takaisin string "asdf".

Näitä voi testata tekemällä tiedontiivistys repositorion sisällä komento:
'''bash
poetry run invoke test
'''

## Testikattavuus
![Testikattavuuden kuva](https://github.com/mleikas/tiedontiivistys/blob/main/dokumentaatio/coverage_raportti.png)


## Empiirinen testaus
### Huffman algoritmin ja LZ78 algoritmin pakatun tiedoston koon vertailu alkuperäiseen ja toisiinsa
![Huffman vs LZ78 koko vertailu](https://github.com/mleikas/tiedontiivistys/blob/main/dokumentaatio/huffman_vs_lz78_koko.png)

Sininen on alkuperäinen koko, oranssi on Huffman algoritmin tuottama tiedoston koko ja harmaa LZ78 algoritmin tuottama tiedoston koko.

Vertailussa huomataan, että pienillä tiedostoilla tulostetiedostojen koko kasvaa, joten niitä ei kannata siis pakata.
Muuten suuremmilla tekstitiedostoilla Huffman algoritmi pakkaa tulostetiedoston aina noin 50%-60% kokoiseksi.
Tulostetiedosto, joka tulee LZ78 algoritmiltä pienenee verrattuna alkuperäiseen tasaisesti, mitä isompi tekstitiedosto on.

### Huffman algoritmin ja LZ78 algoritmin pakkauksen ajan vertailu toisiinsa
![Huffman vs LZ78 pakkausaika vertailu](https://github.com/mleikas/tiedontiivistys/blob/main/dokumentaatio/huffman_vs_lz78_pakkausaika.png)

Sininen on Huffman pakkauksen aika ja oranssi on LZ78 pakkauksen aika.

Vertailussa huomataan, että mitä isompi tiedosto on, sitä kauemmin LZ78 kestää verrattuna Huffman pakkaukseen. Pienillä tai keskiverto tekstitiedostoilla kannattaa siis käyttää mielummin LZ78 algoritmiä ja suuremmilla tekstitiedostoilla kannattaa käyttää Huffman algoritmiä (ajan suhteen).

### Huffman algoritmin ja LZ78 algoritmin purun ajan vertailu toisiinsa
![Huffman vs LZ78 pakkausaika vertailu](https://github.com/mleikas/tiedontiivistys/blob/main/dokumentaatio/huffman_vs_lz78_purkuaika.png)

Sininen on Huffman purun aika ja oranssi on LZ78 purun aika.

Vertailussa huomataan, että Huffman purku kestää aina pidempään, vaikka mitä pienempi tiedosto on, sitä lähempänä ajat ovat. Myös mitä suurempi tiedosto on, sitä nopeampi LZ78 purku on Huffman purkuun verrattuna.
