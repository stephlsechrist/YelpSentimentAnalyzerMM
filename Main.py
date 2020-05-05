
from TextParser import TextParser
from TermFrequencyTable import TermFrequencyTable
from SampleReviews import SampleReviews

tft = TermFrequencyTable()
sample = SampleReviews()

for review in SampleReviews().listOfReviews:
    tft.addList(TextParser(review).sortByAlphaNGram(2))

tft.formatTable()

# tft.displayTermList()
# tft.displayList()
# tft.displayVert()
