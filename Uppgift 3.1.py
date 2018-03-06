from random import shuffle

class Card:
    
    suiteStr = { 1: "Härter", 
                2: "Ruter",
                3: "Spader",
                4: "Klöver"
                }

    valueStr = {
                1: "Äss",
                2: "Två",
                3: "Tre",
                4: "Fyra",
                5: "Fem",
                6: "Sex",
                7: "Sju",
                8: "Åtta",
                9: "Nio",
                10: "Tio",
                11: "Knekt",
                12: "Dam",
                13: "Kung"
                }

    def __init__(self, suite, value):
        assert 1 <= suite <= 4 and 1 <= value <= 13
        self._suite = suite
        self._value = value

    def getValue(self):
        return self._value

    def getSuite(self):
        return self._suite
        
    def __str__(self):
        return self.suiteStr[self._suite] + " " + self.valueStr[self._value]


class CardDeck:
    def __init__(self):
        self.reset()

    def shuffle(self):
        shuffle(self._cardList)

    def getCard(self):
        a = self._cardList[len(self._cardList) - 1]
        self._cardList.pop()
        return a

    def size(self):
        return len(self._cardList)

    def reset(self):
        self._cardList = list()
        for i in range(1, 5):
            for j in range(1, 14):
                self._cardList.append(Card(i, j))
        shuffle(self._cardList)


# Testkod
deck = CardDeck()
deck.shuffle()
while deck.size() > 0:
    card = deck.getCard()
    print("Kortet {} har värdet {}".format(card.getSuite(), card.getValue()))
