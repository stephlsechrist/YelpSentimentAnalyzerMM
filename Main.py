
from TextParser import TextParser
from TermFrequencyTable import TermFrequencyTable
from SampleReviews import SampleReviews
import json
import ast

tft = TermFrequencyTable()
# sample = SampleReviews()

review_list = []

# with open('yelp_academic_dataset_business.json', 'r', encoding="utf8") as f:
#     data = json.load(f)
# print(data)

data = [json.loads(line) for line in open('yelp_academic_dataset_review.json', 'r', encoding="utf8")]

for i in range(50):
    if data[i]['stars'] < 2:
        review_list.append(data[i]['text'])

for review in review_list:
    tft.addList(TextParser(review).sortByAlphaNGram(2))

tft.formatTable()
# tft.displayTermList()
# tft.displayList()
tft.displayVert()
