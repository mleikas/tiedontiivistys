"""
LZ78 algoritmi
"""
import codecs


def lz_koodaus(data, tulostus):
    """
    lz78 pakkausalgoritmi

    Arg:
    data: tekstitiedoston polku
    tulostus: lz78_algoritmillä koodatun tuloksen polku
    """
    sanakirja = {}
    kohta = 1
    buf = ""

    with codecs.open(data, "r", encoding="utf-8") as datatiedosto, codecs.open(tulostus, \
    "w", encoding="utf-8") as tulostustiedosto:
        while True:
            seuraava = datatiedosto.read(1)
            if seuraava is None or len(seuraava) == 0:
                break
            if buf + seuraava not in sanakirja:
                sanakirja[buf + seuraava] = kohta
                kohta += 1
                if len(buf) == 0:
                    kirjoita_tiedostoon(0, seuraava, tulostustiedosto)
                else:
                    kirjain = buf
                    indeksi = sanakirja[kirjain]
                    kirjoita_tiedostoon(indeksi, seuraava, tulostustiedosto)
                buf = ""
            else:
                buf += seuraava

def lz_dekoodaus(data):
    """
    lz78 tiedostojen purkaminen

    Arg:
    data: lz78 koodauksella pakattu data
    """
    lista = []
    with codecs.open(data, encoding='utf-8', mode='r') as avattu_data:
        while True:
            bitti = avattu_data.read(1)
            if bitti is None or len(bitti) == 0:
                break

            indeksi = ord(bitti)
            kirjain = avattu_data.read(1)

            if indeksi == 0:
                lista.append(kirjain)
            else:
                prefiksi = lista[indeksi-1]
                lista.append(prefiksi+kirjain)
    merkkijono = "".join(lista)

    with codecs.open(str(data) + "_purettu-lz.txt", encoding='utf-8', mode='w') as tulostus:
        tulostus.write(merkkijono)

def kirjoita_tiedostoon(indeksi, kirjain, tulostustiedosto):
    """
    lz78 pakkaus apufunktio tiedostoon kirjoittamiseen

    Arg:
    indeksi: koodattu kohta
    kirjain: kirjain tiedostoon
    tulostustiedosto: minne kirjoitetaan
    """
    indeksi = chr(indeksi).encode('utf-8', 'replace').decode('utf-8')
    tulostustiedosto.write(indeksi)
    tulostustiedosto.write(kirjain)
