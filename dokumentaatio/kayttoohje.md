# Käyttöohje

## Asennus

Tarvitset Poetryä ohjelman käyttämiseen. Lataa kirjastot komennolla:

```bash
poetry install
```

## Suoritus

Ohjelma suoritetaan komennolla

```bash
poetry run invoke start
```

## Käyttö

Ohjelma ensin kysyy, mitä haluat tehdä (Huffman pakaaminen: PAINA 1, Huffman purkaminen: PAINA 2, LZ78 pakkaaminen: PAINA 3, LZ78 purkaminen: PAINA 4)

Jokaisen toiminnon jälkeen sinun täytyy antaa polku tiedostolle, jolle toiminto tehdään (esim. Linuxilla se voisi olla muotoa /home/kayttaja/tiedontiivistys/src/testiteksti.txt).

Tämän jälkeen tiedosto tulee polkuun, missä teit toiminnon.

## Testaus

Testit saadaan tehtyä komennolla

```bash
poetry run invoke test
```

## Testikattavuusraportti

Testikattavuusraportin saa htmlcov kansioon komennolla:

```bash
poetry run invoke coverage-report
```

## Pylint

Tiedoston [.pylintrc](./.pylintrc) tarkastukset tehdään komennolla:

```bash
poetry run invoke lint
```
