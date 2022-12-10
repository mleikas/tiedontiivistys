"""
Huffman algoritmi
"""

puun_solmut = []
class Solmu:
    """
    Luokka Huffmanin puun solmuille
    """
    def __init__(self, tod, symboli, vasen=None, oikea=None):
        """
        Luokan konstruktori
        """
        # Symbolin todennäköisyys
        self.tod = tod

        # symboli
        self.symboli = symboli

        # vasen solmu
        self.vasen = vasen

        # oikea solmu
        self.oikea = oikea

        # puun suunta (0 tai 1)
        self.koodi = ''
        self.osoitin = 0

    def hae_osoitin(self):
        """ Apufunktio, joka tuo osoittimen arvon
        Return:
        self.osoitin: Antaa luokassa olevan osoittimen arvon
        """
        return self.osoitin
    def lisaa_osoittimeen(self):
        """ Apufunktio, joka nostaa osoitinta yhdellä
        """
        self.osoitin+=1

    def tavuista_puuksi(self,data):
        """ Apufunktio, jolla tavuista saadaan puu
        Arg:
        data: tiedostosta saatu data tavuina

        Return:
        uusi_solmu: Huffman puun data
        """
        if data[Solmu.hae_osoitin(self)] == "1":
            Solmu.lisaa_osoittimeen(self)
            uusi_solmu = Solmu(0, data[Solmu.hae_osoitin(self)])
            puun_solmut.append(uusi_solmu)
            return uusi_solmu

        Solmu.lisaa_osoittimeen(self)
        vasen_puoli = Solmu.tavuista_puuksi(self,data)

        Solmu.lisaa_osoittimeen(self)
        oikea_puoli = Solmu.tavuista_puuksi(self,data)

        uusi_solmu = Solmu(0, "0", vasen_puoli, oikea_puoli)
        puun_solmut.append(uusi_solmu)
        return uusi_solmu


puu_bytes = []
def puu_tavuiksi(solmussa):
    """ Luokan funktio, joka muuttaa solmut toiseen tavuiksi
    Arg:
    solmu: Huffman puun solmu

    Return:
    puu_tavuina: puu tavumuodossa
    """

    if solmussa.oikea is None and solmussa.vasen is None:
        puu_bytes.append(1)
        puu_bytes.append(solmussa.symboli)
    else:
        puu_bytes.append(0)
        puu_tavuiksi(solmussa.vasen)
        puu_tavuiksi(solmussa.oikea)

    puu_tavuina = ''.join([str(byte) for byte in puu_bytes]) + "_"

    return bytes(puu_tavuina, 'utf-8')

koodit = {}

def laske_koodit(solmu, arvo=''):
    """ Apufunktio printtaamaan symbolien koodit menemällä Huffman puun läpi

    Arg:
    solmu: Huffman puun solmu
    arvo: Huffman koodin arvot
    Return:
    koodit: koodattu tulos binäärinä
    """
    uusi_arvo = arvo + str(solmu.koodi)

    if solmu.vasen:
        laske_koodit(solmu.vasen, uusi_arvo)
    if solmu.oikea:
        laske_koodit(solmu.oikea, uusi_arvo)

    if not solmu.vasen and not solmu.oikea:
        koodit[solmu.symboli] = uusi_arvo

    return koodit

def laske_tod(data):
    """ Apufunktio laskemaan symbolien todennäköisyydet annetussa datassa

    Arg:
    data: tiedostosta saatu teksti

    Return:
    symbolit: dict todennäköisimmistä symboleista
    """
    symbolit = {}
    for elementti in data:
        if symbolit.get(elementti) is None:
            symbolit[elementti] = 1
        else:
            symbolit[elementti] += 1
    return symbolit

def tulos_koodattu(data, koodaus):
    """
    Apufunktio, joka antaa enkoodatun tulostuksen

    Arg:
    data: tiedostosta saatu teksti
    koodaus: huffman koodi saatu tehdystä puusta

    Return:
    string: tulos koodattuna binääriksi
    """
    koodaus_tulos = []
    for bitti in data:
        koodaus_tulos.append(koodaus[bitti])

    string = ''.join([str(item) for item in koodaus_tulos])
    return string


def huffman_koodaus(data):
    """
    Huffman pakkaus

    Arg:
    data: tiedostosta saatu teksti

    Return:
    tulos_byteina: data muutettuna tavuiksi
    pakattu_puu: puu muutettuna tavuiksi
    """
    symboli_todennakoisyyksilla = laske_tod(data)
    symbolit = symboli_todennakoisyyksilla.keys()

    solmut = []
    for symboli in symbolit:
        solmut.append(Solmu(symboli_todennakoisyyksilla.get(symboli), symboli))

    while len(solmut) > 1:
        solmut = sorted(solmut, key=lambda i: i.tod)

        oikea = solmut[0]
        vasen = solmut[1]

        vasen.koodi = 0
        oikea.koodi = 1

        uusi_solmu = Solmu(vasen.tod+oikea.tod, vasen.symboli+oikea.symboli, vasen, oikea)

        solmut.remove(vasen)
        solmut.remove(oikea)
        solmut.append(uusi_solmu)

    huffman_koodi = laske_koodit(solmut[0])
    koodattu_tulos = tulos_koodattu(data,huffman_koodi)
    pakattu_puu = puu_tavuiksi(solmut[0])
    tulos_byteina = bititbyteiksi(koodattu_tulos)

    return bytes(tulos_byteina), pakattu_puu

def bititbyteiksi(koodattu_tulos):
    """
    Funktio bittien muuttamiseen byteiksi

    Arg:
    koodattu_tulos: binääriksi muutettu tiedoston sisältö

    Return:
    bytelista: bitit muutettuina tavuiksi
    """
    bytelista = bytearray()
    bufferbitit = 8-(len(koodattu_tulos)%8)
    for i in range(0,len(koodattu_tulos),8):
        bytelista.append(int(koodattu_tulos[i:i+8], 2))
    bytelista.insert(0, bufferbitit)
    return bytelista

def huffman_dekoodaus(koodattu_data):
    """
    Huffman purku

    Arg:
    koodattu_data: pakatusta tiedostosta luettu data

    Return:
    tulos: tiedoston sisältö tekstinä
    """
    puu_tavuina, valmiit_bitit = data_biteiksi(koodattu_data)

    huffman_puu = Solmu.tavuista_puuksi(Solmu(0,"0"), puu_tavuina)
    puun_eka = huffman_puu
    dekoodattu_tulos = []
    for i in valmiit_bitit:
        if i == '1':
            huffman_puu = huffman_puu.oikea
        elif i == '0':
            huffman_puu = huffman_puu.vasen
        try:
            if huffman_puu.vasen.symboli is None and huffman_puu.oikea.symboli is None:
                pass
        except AttributeError:
            dekoodattu_tulos.append(huffman_puu.symboli)
            huffman_puu = puun_eka

    tulos = ''.join([str(item) for item in dekoodattu_tulos])
    return tulos

def data_biteiksi(koodattu_data):
    '''
    Apufunktio dekoodaukselle, jossa saadusta datasta tehdään binääristring

    Arg:
    koodattu_data: pakatusta tiedostosta luettu data

    Return:
    puu_tavuina: puun data binäärinä
    valmit_bitit: tiedoston tekstin binääri
    '''
    indeksi = 0
    puu_tavuina = ""
    for i in koodattu_data:
        i = koodattu_data[indeksi:indeksi+1].decode('utf-8')
        indeksi += 1
        if i == "_":
            break
        puu_tavuina += i
    tavut = koodattu_data[indeksi:]
    lista = []
    bitit = ''.join(format(tavu, '08b') for tavu in tavut[1:])
    buffer_bitit = tavut[0]
    indeksi = buffer_bitit
    while indeksi > 0:
        lista.append(bitit[-indeksi])
        indeksi -= 1
    lopputeksti = ''.join(lista)
    for bitti in lopputeksti:
        if bitti == '1':
            lopputeksti = lopputeksti[lopputeksti.index(bitti):]
            break
    poistuvat = buffer_bitit + len(lopputeksti)
    ilman_buf_bitteja = bitit[:-poistuvat]
    valmiit_bitit = ilman_buf_bitteja + lopputeksti
    return puu_tavuina, valmiit_bitit
