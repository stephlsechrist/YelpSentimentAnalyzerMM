import re
import Stem
from operator import itemgetter
from StopList import StopList

class TermFrequencyTable:

    def __init__(self):
        self.count = 1
        self.termFreqTable = []

    def addList(self, newList):
        # self.termFreqTable.append(self.count)
        self.termFreqTable.append(newList)
        self.count += 1

    def display(self):
        termList = []
        for currList in self.termFreqTable:
            for currItem in currList:
                if currItem[0] not in termList:
                    termList.append(currItem[0])

        for term in termList:
            print(term + " ", end='')
        print()

        for currList in self.termFreqTable:
            tempList = []
            flag = False
            for term in termList:
                for currItem in currList:
                    if term == currItem[0]:
                        tempList.append(currItem[1])
                        flag = True
                if flag == False:
                    tempList.append("0")
                flag = False

            for num in tempList:
                print(num, end='')
                print(" ", end='')
            print()

        # for currList in self.termFreqTable:
        #     for currItem in currList:
        #         if currItem[0] in termList:
        #             print(currItem[1], end='')
        #             print(" ", end='')
        #         else:
        #             print("0 ", end='')
        #     print()

    def sortByTotal(self):
        listText = self.formatText()
        return sorted(listText, key = itemgetter(1), reverse = True)

    def sortByAlpha(self):
        listText = self.formatText()
        return sorted(listText, key = itemgetter(0))

    def getText(self):
        return self.text

    # def __str__(self):
    #     return "<Text: %s>" % self.getText()

    # def __repr__(self):
    #     return str(self)