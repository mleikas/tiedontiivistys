# Algoritmi on tehty tämän pohjalta:
# https://towardsdatascience.com/huffman-encoding-python-implementation-8448c3654328
# Huffman Puun Solmu
"""
Huffman algoritmi
"""
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

    def __str__(self):
        return self.__class__.__name__

    def puu_tekstiksi(self):
        """ Luokan funktio, joka muuttaa solmut toiseen muotoon """

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

def total_gain(data, koodaus):
    """ Apufunktio tilan eron laskemiseen pakatun ja ei-pakatun datan välillä """
    ennen_pakkausta = len(data) * 8
    jalkeen_pakkauksen = 0
    symbolit = koodaus.keys()
    for symboli in symbolit:
        count = data.count(symboli)
        jalkeen_pakkauksen += count * len(koodaus[symboli])
    print("Tilan käyttö ennen pakkausta (biteissä):", ennen_pakkausta)
    print("Tilan käyttö pakkauksen jälkeen(biteissä):",  jalkeen_pakkauksen)

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
    total_gain(data, huffman_koodi)
    koodattu_tulos = tulos_koodattu(data,huffman_koodi)
    solmut = str(solmut)
    return bytes(koodattu_tulos, encoding='utf8'), bytes(solmut, encoding='utf8')


def huffman_dekoodaus(koodattu_data, huffman_puu):
    """
    Huffman purku
    """
    puu_head = huffman_puu
    dekoodattu_tulos = []
    for i in koodattu_data:
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

    string = ''.join([str(item) for item in dekoodattu_tulos])
    return string
