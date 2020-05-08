import re
import Stem
from operator import itemgetter
from StopList import StopList

class TermFrequencyTable:

    def __init__(self):
        self.termFreqTable = []
        self.listOfReviews = []
        self.termList = []

    def addList(self, newList):
        self.listOfReviews.append(newList)

    def displayList(self):
        print(self.listOfReviews)

    def displayTermList(self):
        print(self.termList)

    def formatTable(self):

        self.termList = []
        for currList in self.listOfReviews:
            for currItem in currList:
                if currItem[0] not in self.termList:
                    self.termList.append(currItem[0])

        self.termList.sort()

        for currList in self.listOfReviews:
            tempList = []
            flag = False
            for term in self.termList:
                for currItem in currList:
                    if term == currItem[0]:
                        tempList.append(currItem[1])
                        flag = True
                if flag == False:
                    tempList.append("0")
                flag = False

            self.termFreqTable.append(tempList)

    def display(self):

        for term in self.termList:
            print(term + " ", end='')
        print()

        for tempList in self.termFreqTable:
            for num in tempList:
                print(num, end='')
                print(" ", end='')
            print()

    def displayVert(self):

        count = 0
        for term in self.termList:
            total = 0
            tempList = []
            tempList.append(term)

            for listNum in self.termFreqTable:
                # tempList.append(listNum[count])
                total += int(listNum[count])
            count += 1

            if total > 9:
                print(tempList[0], end='')
                # for num in tempList:
                #     print(num, end='')
                #     print(" ", end='')
                print("\t\ttotal: " + str(total))

