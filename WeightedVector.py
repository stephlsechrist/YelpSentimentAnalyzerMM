import json
from TextParser import TextParser

class WeightedVector:

    def __init__(self):
        self.compareVector = {}

    def eval(self, review):
        pReview = TextParser(review).sortByAlphaNGram(2)
        total = 0
        for terms in pReview:
            if (terms[0][0] + " " + terms[0][1]) in self.compareVector:
                total += (self.compareVector[(terms[0][0] + " " + terms[0][1])] * terms[1])

        return total

    def displayTable(self, table, stars):
        for key in table:
            print(key, end='')
            print(" : " + str(table[key]))

    def displayVector(self):
        for key in self.compareVector:
            if abs(self.compareVector[key]) > 5:
                print(key, end='')
                print(" : " + str(self.compareVector[key]))

    def updateVector(self, table, stars):

        for key in table:
            if stars > 0:
                if table[key] not in self.compareVector:
                    self.compareVector[key] = (table[key] * stars)
                elif table[key] in self.compareVector:
                    self.compareVector[key] += (table[key] * stars)
            else:
                if table[key] not in self.compareVector:
                    self.compareVector[key] = (table[key] * stars)
                elif table[key] in self.compareVector:
                    self.compareVector[key] += (table[key] * stars)

    def loadVector(self):
        with open('weighted_vector.json') as json_file:
            self.compareVector = json.load(json_file)

    def saveVector(self):
        with open('weighted_vector.json', 'w') as json_file:
            json.dump(self.compareVector, json_file)
