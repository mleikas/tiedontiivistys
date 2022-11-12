# Algoritmi on tehty tämän pohjalta:
# https://towardsdatascience.com/huffman-encoding-python-implementation-8448c3654328
# Huffman Puun Solmu
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

""" Apufunktio printtaamaan symbolien koodit menemällä Huffman puun läpi """
koodit = dict()

def Laske_Koodit(solmu, arvo=''):
    # huffman koodi nykyiselle solmulle
    uusiArvo = arvo + str(solmu.koodi)

    if solmu.vasen:
        Laske_Koodit(solmu.vasen, uusiArvo)
    if solmu.oikea:
        Laske_Koodit(solmu.oikea, uusiArvo)

    if not solmu.vasen and not solmu.oikea:
        koodit[solmu.symboli] = uusiArvo

    return koodit        

""" Apufunktio laskemaan symbolien todennäköisyydet annetussa datassa"""
def Laske_Tod(data):
    symbolit = dict()
    for elementti in data:
        if symbolit.get(elementti) == None:
            symbolit[elementti] = 1
        else: 
            symbolit[elementti] += 1
    return symbolit

""" Apufunktio, joka antaa enkoodatun tulostuksen"""
def Tulos_Koodattu(data, koodaus):
    koodaus_tulos = []
    for c in data:
        koodaus_tulos.append(koodaus[c])

    string = ''.join([str(item) for item in koodaus_tulos])    
    return string
 
""" Apufunktio tilan eron laskemiseen pakatun ja ei-pakatun datan välillä """
def Total_Gain(data, koodaus):
    ennen_tiivistysta = len(data) * 8
    jalkeen_tiivistyksen = 0
    symbolit = koodaus.keys()
    for symboli in symbolit:
        count = data.count(symboli)
        jalkeen_tiivistyksen += count * len(koodaus[symboli])
    print("Tilan käyttö ennen tiivistystä (biteissä):", ennen_tiivistysta)
    print("Tilan käyttö tiivistyksen jälkeen(biteissä):",  jalkeen_tiivistyksen)

def Huffman_Koodaus(data):
    """
    Huffman pakkaus
    """
    symboli_todennakoisyyksilla = Laske_Tod(data)
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

        uusiSolmu = Solmu(vasen.tod+oikea.tod, vasen.symboli+oikea.symboli, vasen, oikea)

        solmut.remove(vasen)
        solmut.remove(oikea)
        solmut.append(uusiSolmu)

    huffman_koodaus = Laske_Koodit(solmut[0])
    Total_Gain(data, huffman_koodaus)
    koodattu_tulos = Tulos_Koodattu(data,huffman_koodaus)
    return koodattu_tulos, solmut[0]  


def Huffman_Dekoodaus(koodattu_data, huffman_puu):
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
            if huffman_puu.vasen.symboli == None and huffman_puu.oikea.symboli == None:
                pass
        except AttributeError:
            dekoodattu_tulos.append(huffman_puu.symboli)
            huffman_puu = puu_head

    string = ''.join([str(item) for item in dekoodattu_tulos])
    return string        
