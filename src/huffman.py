"""
Huffman algoritmi
"""
puun_solmut = []
class Solmu:
    """
    Luokka Huffmanin puun solmuille
    """
    def __init__(self, tod, symboli, vasen=None, oikea=None):
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

    def __str__(self):
        return self.__class__.__name__
    def hae_osoitin(self):
        """ Apufunktio, joka tuo osoittimen arvon """
        return self.osoitin
    def lisaa_osoittimeen(self):
        """ Apufunktio, joka nostaa osoitinta yhdellä """
        self.osoitin+=1

    def tavuista_puuksi(self,data):
        """ Apufunktio, jolla tavuista saadaan puu """
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
    """ Luokan funktio, joka muuttaa solmut toiseen tavuiksi """

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
    """ Apufunktio printtaamaan symbolien koodit menemällä Huffman puun läpi """
    # huffman koodi nykyiselle solmulle
    uusi_arvo = arvo + str(solmu.koodi)

    if solmu.vasen:
        laske_koodit(solmu.vasen, uusi_arvo)
    if solmu.oikea:
        laske_koodit(solmu.oikea, uusi_arvo)

    if not solmu.vasen and not solmu.oikea:
        koodit[solmu.symboli] = uusi_arvo

    return koodit

def laske_tod(data):
    """ Apufunktio laskemaan symbolien todennäköisyydet annetussa datassa"""
    symbolit = {}
    for elementti in data:
        if symbolit.get(elementti) is None:
            symbolit[elementti] = 1
        else:
            symbolit[elementti] += 1
    return symbolit

def tulos_koodattu(data, koodaus):
    """ Apufunktio, joka antaa enkoodatun tulostuksen"""
    koodaus_tulos = []
    for bitti in data:
        koodaus_tulos.append(koodaus[bitti])

    string = ''.join([str(item) for item in koodaus_tulos])
    return string


def huffman_koodaus(data):
    """
    Huffman pakkaus
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
    return bytes(koodattu_tulos, encoding='utf-8'), pakattu_puu


def huffman_dekoodaus(koodattu_data):
    """
    Huffman purku
    """
    koodattu_data=koodattu_data.decode('utf-8','strict')
    indeksi = koodattu_data.index("_",0)
    teksti = koodattu_data[indeksi+1:]
    puu_tavuina = koodattu_data[:indeksi]
    huffman_puu = Solmu.tavuista_puuksi(Solmu(0,"0"), puu_tavuina)
    puu_head = huffman_puu
    dekoodattu_tulos = []
    for i in teksti:
        if i == '1':
            huffman_puu = huffman_puu.oikea
        elif i == '0':
            huffman_puu = huffman_puu.vasen
        try:
            if huffman_puu.vasen.symboli is None and huffman_puu.oikea.symboli is None:
                pass
        except AttributeError:
            dekoodattu_tulos.append(huffman_puu.symboli)
            huffman_puu = puu_head

    tulos = ''.join([str(item) for item in dekoodattu_tulos])
    return tulos
