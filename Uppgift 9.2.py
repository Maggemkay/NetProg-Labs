import math

txt = open("exempeltext.txt", "r").read()
textByteArr = bytearray(txt, "UTF-8")

print("Uppgift 1: ")
print("Chars: {}".format(len(txt)))
print("ByteArray size: {}".format(len(textByteArr)))

print("\nUppgift 2: ")

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
    for item in histo:
        prob.append(item / total)
    return prob

def entropi(prob):
    ent = 0
    for item in prob:
        if item != 0:
            ent += item * math.log2(1/item)
    return ent

#print(makeHisto(textByteArr))
a = textByteArr
b = makeHisto(a)
c = makeProb(b)
d = entropi(c)
print( (len(txt) * d) / 8 )

print("\nUppgift 3: ")

        