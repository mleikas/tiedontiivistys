# Tämä on pohjasta muotoiltu:
# https://github.com/YCAyca/Data-Structures-and-Algorithms-with-Python/
# blob/main/Huffman_Encoding/huffman.py
# Huffman Puu Node
class Node:
    def __init__(self, prob, symboli, vasen=None, oikea=None):
        # probability of symbol
        self.prob = prob

        # symbol 
        self.symboli = symboli

        # left node
        self.vasen = vasen

        # right node
        self.oikea = oikea

        # tree direction (0/1)
        self.code = ''

""" A helper function to print the codes of symbols by traveling Huffman Tree"""
codes = dict()

def Calculate_Codes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.code)

    if(node.vasen):
        Calculate_Codes(node.vasen, newVal)
    if(node.right):
        Calculate_Codes(node.oikea, newVal)

    if(not node.vasen and not node.oikea):
        codes[node.symboli] = newVal
         
    return codes        

""" A helper function to calculate the probabilities of symbols in given data"""
def Calculate_Probability(data):
    symbolit = dict()
    for elementti in data:
        if symbolit.get(elementti) == None:
            symbolit[elementti] = 1
        else: 
            symbolit[elementti] += 1     
    return symbolit

""" A helper function to obtain the encoded output"""
def Output_Encoded(data, coding):
    encoding_output = []
    for c in data:
        encoding_output.append(coding[c])
        
    string = ''.join([str(item) for item in encoding_output])    
    return string
        
""" A helper function to calculate the space difference between compressed and non compressed data"""    
def Total_Gain(data, coding):
    ennen_tiivistysta = len(data) * 8 # total bit space to stor the data before compression
    jalkeen_tiivistysta = 0
    symbolit = coding.keys()
    for symboli in symbolit:
        count = data.count(symboli)
        jalkeen_tiivistysta += count * len(coding[symboli]) #calculate how many bit is required for that symbol in total
    print("Space usage before compression (in bits):", ennen_tiivistysta)    
    print("Space usage after compression (in bits):",  jalkeen_tiivistysta)           

def Huffman_Encoding(data):
    symboli_with_probs = Calculate_Probability(data)
    symbolit = symboli_with_probs.keys()
    probabilities = symboli_with_probs.values()
    print("symbols: ", symbolit)
    print("probabilities: ", probabilities)
    
    nodes = []
    
    # converting symbols and probabilities into huffman tree nodes
    for symboli in symbolit:
        nodes.append(Node(symboli_with_probs.get(symboli), symboli))
    
    while len(nodes) > 1:
        # sort all the nodes in ascending order based on their probability
        nodes = sorted(nodes, key=lambda x: x.prob)
        # for node in nodes:  
        #      print(node.symbol, node.prob)
    
        # pick 2 smallest nodes
        oikea = nodes[0]
        vasen = nodes[1]
    
        vasen.code = 0
        oikea.code = 1
    
        # combine the 2 smallest nodes to create new node
        newNode = Node(vasen.prob+oikea.prob, vasen.symboli+oikea.symboli, vasen, oikea)
    
        nodes.remove(vasen)
        nodes.remove(oikea)
        nodes.append(newNode)
            
    huffman_encoding = Calculate_Codes(nodes[0])
    print("symbols with codes", huffman_encoding)
    Total_Gain(data, huffman_encoding)
    encoded_output = Output_Encoded(data,huffman_encoding)
    return encoded_output, nodes[0]  
    
 
def Huffman_Decoding(encoded_data, huffman_tree):
    tree_head = huffman_tree
    decoded_output = []
    for x in encoded_data:
        if x == '1':
            huffman_tree = huffman_tree.oikea  
        elif x == '0':
            huffman_tree = huffman_tree.vasen
        try:
            if huffman_tree.vasen.symboli == None and huffman_tree.oikea.symboli == None:
                pass
        except AttributeError:
            decoded_output.append(huffman_tree.symboli)
            huffman_tree = tree_head
        
    string = ''.join([str(item) for item in decoded_output])
    return string        


""" First Test """
data = "AAAAAAABCCCCCCDDEEEEE"
print(data)
encoding, tree = Huffman_Encoding(data)
print("Encoded output", encoding)
print("Decoded Output", Huffman_Decoding(encoding,tree))


""" Second Test """

# f = open("demofile.txt", "r")

# data = f.read()
# print(data)
# Huffman_Encoding(data)
