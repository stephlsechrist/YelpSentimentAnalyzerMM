import json
from TextParser import TextParser
import math

class WeightedVector:

    def __init__(self):
        self.compareVector = {}

    def eval(self, review):
        pReview = TextParser(review).sortByAlphaNGram(2)
        total = 0
        for terms in pReview:
            if (terms[0][0] + " " + terms[0][1]) in self.compareVector:
                temp = 0
                if (self.compareVector[(terms[0][0] + " " + terms[0][1])]) < 0:
                    temp = (self.compareVector[(terms[0][0] + " " + terms[0][1])] * -1) ** (1. / 3)
                    temp = temp * -1
                else:
                    temp = (self.compareVector[(terms[0][0] + " " + terms[0][1])]) ** (1. / 3)
                total += (temp * terms[1])

        return (total / len(pReview) ** (1. / 3))

    def displayTable(self, table, stars):
        for key in table:
            print(key, end='')
            print(" : " + str(table[key]))

    def displayVector(self):
        for key in sorted(self.compareVector):
            if abs(self.compareVector[key]) > 50:
                print(key, end='')
                print(" : " + str(self.compareVector[key]))

    def updateVector(self, table, mod):

        for key in sorted(table):
            if mod < 0:
                if key not in self.compareVector:
                    self.compareVector[key] = (table[key] * mod)
                else:
                    self.compareVector[key] += (table[key] * mod)
            else:
                if key not in self.compareVector:
                    self.compareVector[key] = (table[key] * mod)
                else:
                    self.compareVector[key] += (table[key] * mod)

    def loadVector(self):
        with open('weighted_vector.json') as json_file:
            self.compareVector = json.load(json_file)

    def saveVector(self):
        with open('weighted_vector.json', 'w') as json_file:
            json.dump(self.compareVector, json_file)
