"""
LZ78 algoritmi
"""
import codecs


def lz_koodaus(data, tulostus):
    """
    lz78 pakkausalgoritmi
    """
    sanakirja = {}
    position = 1
    buf = ""

    datatiedosto = codecs.open(data, encoding='utf-8', mode='r')
    tulostustiedosto = codecs.open(tulostus, encoding='utf-8', mode='w')
    def kirjoita_tiedostoon(index, letter):
        tulostustiedosto.write(chr(index))
        tulostustiedosto.write(letter)
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
    """
    lista = []
    avattu_data = codecs.open(data, encoding='utf-8', mode='r')

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

    string = ""
    for i in lista:
        string += i

    tulostus = codecs.open(str(data) + "_purettu-lz.txt", encoding='utf-8', mode='w')

    tulostus.write(string)
