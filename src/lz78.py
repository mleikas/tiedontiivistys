"""
LZ78 algoritmi
"""

def lz_koodaus(data, tulostus):
    """
    lz78 pakkausalgoritmi

    Arg:
    data: tekstitiedoston polku
    tulostus: lz78_algoritmillä koodatun tuloksen polku
    """
    sanakirja = {}
    position = 1
    buf = ""

    with open(data, encoding='utf-8', mode='r') as datatiedosto:
        with open(tulostus, encoding='utf-8', mode='w') as tulostustiedosto:
            def kirjoita_tiedostoon(indeksi, kirjain):
                indeksi = chr(indeksi).encode('utf-8', 'replace').decode('utf-8')
                tulostustiedosto.write(indeksi)
                tulostustiedosto.write(kirjain)
            while True:
                seuraava = datatiedosto.read(1)
                buf += seuraava
                if buf not in sanakirja:
                    sanakirja[buf] = position
                    position += 1
                    if len(buf) == 1:
                        kirjoita_tiedostoon(0, buf)
                    elif len(buf) == 0:
                        kirjoita_tiedostoon(0, '')
                    else:
                        kirjain = buf[:-1]
                        pos = sanakirja[kirjain]
                        kirjoita_tiedostoon(pos, buf[-1])
                    buf = ""

                if seuraava is None or len(seuraava) == 0:
                    break

def lz_dekoodaus(data):
    """
    lz78 tiedostojen purkaminen

    Arg:
    data: lz78 koodauksella pakattu data
    """
    lista = []
    with open(data, encoding='utf-8', mode='r') as avattu_data:
        while True:
            bitti = avattu_data.read(1)
            if bitti is None or len(bitti) == 0:
                break

            index = ord(bitti)
            letter = avattu_data.read(1)

            if index == 0:
                lista.append(letter)
            else:
                prefix = lista[index-1]
                lista.append(prefix+letter)
    string = "".join(lista)

    with open(str(data) + "_purettu-lz.txt", encoding='utf-8', mode='w') as tulostus:
        tulostus.write(string)
