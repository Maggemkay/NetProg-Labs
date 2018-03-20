import math
import queue

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


# def treeTotalNodes(tree, h = 0):
#     if type(tree.data) == int:
#         return 0
#     else:
#         h1 = avgTreeLen(tree.data[0]) + 1
#         h2 = avgTreeLen(tree.data[1]) + 1
#         return h1 if h2 < h1 else h2
    
def fillTable(node, binary = ""):
    if type(node.data) == int:
        char = ""
        if 32 <= node.data <= 127:
            char = chr(node.data)
        binCode = binary
        numbBin = len(binCode)
        ideCode = math.log2(1 / node.prio)

        table[node.data] = [char, binCode, numbBin, ideCode]
    else:
        fillTable(node.data[0], "{}0".format(binary))
        fillTable(node.data[1], "{}1".format(binary))


txt = open("exempeltext.txt", "r").read()
textByteArr = bytearray(txt, "UTF-8")

table = {}

print("Chars: {}".format(len(txt)))
print("textByteArr size: {}".format(len(textByteArr)))

PQ = makeTree(makeHisto(textByteArr))
rootNode = PQ.get()

printTree(rootNode)

print("Tree height: {}".format(treeHeight(rootNode)))

fillTable(rootNode)
for key in table:
    print(table[key])

