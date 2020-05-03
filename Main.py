
from TextParser import TextParser
from TermFrequencyTable import TermFrequencyTable
from SampleReviews import SampleReviews

tft = TermFrequencyTable()

for review in SampleReviews().listOfReviews:
    tft.addList(TextParser(review).sortByAlpha())

tft.formatTable()
tft.displayVert()
