import re
from operator import itemgetter

class TextParser:

    def __init__(self, text):
        """
            name: Name of the fruit shop

            fruitPrices: Dictionary with keys as fruit
            strings and prices for values e.g.
            {'apples':2.00, 'oranges': 1.50, 'pears': 1.75}
        """
        self.text = text
#        print('Welcome to %s fruit shop' % (name))

    def formatText(self):
        listText = []
        for newText in self.text.split():
            flag = False
            count = 0
            fText = re.sub(r'[\W_]+', '', newText)
            newEntry = [fText.lower(), 1]

            for testText in listText:
                if newEntry[0] == testText[0]:
                    listText[count][1] = listText[count][1] + 1
                    flag = True

                count = count + 1
            if flag == False:
                listText.append(newEntry)

        return sorted(listText, key = itemgetter(0))

    def sortByTotal(self):
        return sorted(listGiven, key = itemgetter(1))


    def getText(self):
        return self.text

    def __str__(self):
        return "<Text: %s>" % self.getText()

    def __repr__(self):
        return str(self)