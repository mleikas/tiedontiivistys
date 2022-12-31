# Toteutusraportti

## Ohjelman yleisrakenne

Ohjelma aloitetaan main.py:llä, josta voidaan valita Huffman pakkaus/purkaminen ja LZ78 pakkaus/purkaminen. Näille kummallekkin on omat python tiedostonsa, joista ne haetaan main tiedostoon.

## Suorituskyky- ja O-analyysivertailu

Huffman toimii aikavaativuudella O(n log n) ja LZ78 toimii aikavaativuudella O(n). Ohjelmassani kuitenkin esimerkiksi tiedostojen avaaminen hidastavat varsinkin LZ78 ohjelmaa.

Tilan sain pakattua isommilla tiedostoilla haluttuun kokoon (40%-60%) ja useimmiten sama alkuperäinen teksti saadaan purettua tästä. (Tästä enemmän puutteissa)

## Työn mahdolliset puutteet ja parannusehdotukset

Tällä hetkellä Huffman koodauksessa on pieni bugi, jonka takia ohjelma pakkauksen ja purkamisen jälkeen syöttää pari merkkiä roskaa loppuun.

LZ78 ohjelma ei toimi optiminopeudella, koska joudun käyttämään "codecs.open" kirjastoa perus "open" kirjaston sijaan, koska utf-8 muuttaa esimerkiksi merkkiyhdistelmän "ol" kirjaimeksi "u". Muuten LZ78 ohjelma toimii oikein.

Jatkokehityksenä korjaisin Huffman algoritmin bugin ja käyttäisin jotain toista kirjastoa LZ78 ohjelmassa tiedostojen avaamista varten.

## Lähteet
https://towardsdatascience.com/huffman-encoding-python-implementation-8448c3654328

https://towardsdatascience.com/huffman-decoding-cca770065bab

https://stackoverflow.com/questions/15081300/storing-and-reconstruction-of-huffman-tree

https://en.wikipedia.org/wiki/LZ77_and_LZ78

https://medium.com/swlh/how-data-compression-works-exploring-lz78-e97e539138
