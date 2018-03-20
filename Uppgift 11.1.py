import math
import queue
import collections

class Node:
    def __init__(self, prio, data):
        self.prio = prio
        self.data = data
    def __lt__(self, other):
        return self.prio < other.prio
    def __str__(self):
        if type(self.data) == int:
            return "{} {}".format(self.data, self.prio)
            
def makeHisto(byteArr):
    hist = [0] * 255
    for char in byteArr:
        hist[char] += 1
    return hist

def makeProb(histo):
    total = 0
    for amount in histo:
        total += amount
    prob = [0] *255
    for i in range(len(histo)):
        prob[i] = (histo[i] / total)
    return prob

def makeTree(histList):
    tree = queue.PriorityQueue()
    for i in range(len(histList)):
        if histList[i] > 0:                # Ta bort alla som förekommer 0 gånger
            tree.put(Node(histList[i], i))
    while tree.qsize() > 1:
        t1, t2 = tree.get(), tree.get()
        tree.put(Node(t1.prio + t2.prio, (t1, t2))) 
    return tree

def printTree(tree):
    if type(tree.data) == int:
        print(tree)
        return
    else:
        printTree(tree.data[0])
        printTree(tree.data[1])

def treeHeight(tree, h = 0):
    if type(tree.data) == int:
        return 0
    else:
        h1 = treeHeight(tree.data[0]) + 1
        h2 = treeHeight(tree.data[1]) + 1
        return h1 if h2 < h1 else h2
    
def fillTable(node, binary = ""):
    if type(node.data) == int:
        char = ""
        if 32 <= node.data <= 127:
            char = chr(node.data)
        binCode = binary
        numbBin = len(binCode)
        ideCode = math.log2(1 / probTable[node.data])
        table[node.data] = [char, binCode, numbBin, ideCode]
    else:
        fillTable(node.data[0], "{}0".format(binary))
        fillTable(node.data[1], "{}1".format(binary))


txt = open("exempeltext.txt", "r").read()
textByteArr = bytearray(txt, "UTF-8")
table = {}
probTable = makeProb(makeHisto(textByteArr))

PQ = makeTree(makeHisto(textByteArr))
rootNode = PQ.get()

#printTree(rootNode)

fillTable(rootNode)
sortedTable = collections.OrderedDict(sorted(table.items()))

totalTreeHeight = 0
print("ASCII".ljust(7) + "Char".ljust(6) + "Bit-Array".ljust(18) + "BitLen".ljust(9) + "Ideal code-length")
for key in sortedTable:
    print(str(key).ljust(7) + str(sortedTable[key][0]).ljust(6) + str(sortedTable[key][1]).ljust(18) + str(sortedTable[key][2]).ljust(9) + str(sortedTable[key][3]))
    totalTreeHeight += sortedTable[key][2]

print("Tree height: {}".format(treeHeight(rootNode)))
print("Avrage Tree height: {}".format((totalTreeHeight / len(sortedTable))))
