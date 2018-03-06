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


# a = Card(2, 13)
# print(a)
#testing dododoodo


class CardDeck:
    def __init__(self):
        self._cardList = {}    

    def shuffle(self):
        pass

    def getCard(self):
        pass

    def size(self):
        pass

    def reset(self):
        pass


