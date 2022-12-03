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
