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
