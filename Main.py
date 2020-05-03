
from TextParser import TextParser
from TermFrequencyTable import TermFrequencyTable
from SampleReviews import SampleReviews

sample = SampleReviews()
tft = TermFrequencyTable()

for review in sample.listOfReviews:
    parsedReview = TextParser(review)
    tft.addList(parsedReview.sortByAlpha())

tft.formatTable()
tft.displayVert()
