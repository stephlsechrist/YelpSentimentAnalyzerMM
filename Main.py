
from TextParser import TextParser
from TermFrequencyTable import TermFrequencyTable
from SampleReviews import SampleReviews

tft = TermFrequencyTable()
sample = SampleReviews()

# testList = [1, 2, 3, 4, 5, 6, 7]
#
# for i, num in enumerate(testList):
#     if i < len(testList) - 1:
#         print(num, testList[i + 1])



# print(TextParser(sample.listOfReviews[0]).sortByAlphaNGram(2))

for review in SampleReviews().listOfReviews:
    tft.addList(TextParser(review).sortByAlphaNGram(2))

tft.formatTable()
tft.displayVert()
