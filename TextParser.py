import re
import Stem
from operator import itemgetter
from StopList import StopList

class TextParser:

    def __init__(self, text):
        self.text = text
        self.stopList = StopList()

    def formatText(self):
        listText = []
        stemmedList = Stem.stem(self.text.split())

        for newText in stemmedList:
            flag = False
            count = 0
            fText = re.sub(r'[\W_]+', '', newText)
            newEntry = [fText.lower(), 1]

            for stopText in self.stopList.list:
                if newEntry[0] == stopText and flag == False:
                    flag = True

            for testText in listText:
                if newEntry[0] == testText[0] and flag == False:
                    listText[count][1] = listText[count][1] + 1
                    flag = True

                count = count + 1
            if flag == False:
                listText.append(newEntry)

        return listText

    def sortByTotal(self):
        listText = self.formatText()
        return sorted(listText, key = itemgetter(1), reverse = True)

    def sortByAlpha(self):
        listText = self.formatText()
        return sorted(listText, key = itemgetter(0))

    def getText(self):
        return self.text

    def __str__(self):
        return "<Text: %s>" % self.getText()

    def __repr__(self):
        return str(self)