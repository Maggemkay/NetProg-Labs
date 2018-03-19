import math
import random
import zlib

txt = open("exempeltext.txt", "r").read()
textByteArr = bytearray(txt, "UTF-8")

print("Uppgift 1: ")
print("Chars: {}".format(len(txt)))
print("textByteArr size: {}".format(len(textByteArr)))

####################################################################
print("__________________________")
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
print("Entropy: {}".format(d))
print("Expected compression: {}".format((len(txt) * d) / 8 ))

####################################################################
print("__________________________")
print("\nUppgift 3: ")

theCopy = textByteArr[:]
#print(theCopy.decode())
random.shuffle(theCopy)
#print(textByteArr.decode())
#print(theCopy.decode())

####################################################################
print("__________________________")
print("\nUppgift 4: ")

zipCopy = zlib.compress(theCopy)
zipText = zlib.compress(textByteArr)
print("theCopy byte-array size: {}".format(len(theCopy)))
print("theCopy bit-array size: {}".format((len(theCopy) * 8)))
print("")
print("ZipCopy byte-array size: {}".format(len(zipCopy)))
print("ZipCopy bit-array size: {}".format((len(zipCopy) * 8)))
print("Bit per byte (zipCopy/theCopy): {}".format((len(zipCopy) * 8) / len(theCopy)))
print("")
print("zipByteArr byte-array size: {}".format(len(zipText)))
print("zipByteArr bit-array size: {}".format((len(zipText) * 8)))
print("Bit per byte (zipByteArr/textByteArr): {}".format((len(zipText) * 8) / len(textByteArr)))

####################################################################
print("__________________________")
print("\nUppgift 5: ")

T1 = "Hoppas att denna laboration aldrig tar slut för nu börjar ett mycket intressant experiment!"
T10 = T1*10

zipT1 = zlib.compress(T1.encode())
zipT10 = zlib.compress(T10.encode())

print("zipT1 byte-array size: {}".format(len(zipT1)))
print("zipT10 byte-array size: {}".format(len(zipT10)))




