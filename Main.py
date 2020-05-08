
from TextParser import TextParser
from TermFrequencyTable import TermFrequencyTable
import json

# data = [json.loads(line) for line in open('yelp_academic_dataset_review.json', 'r', encoding="utf8")]

tft = TermFrequencyTable()

review_list = []

with open('sample_reviews_1000.json', 'r', encoding="utf8") as f:
    data = json.load(f)

for i in range(len(data)):
    review_list.append(data[i])

print(len(review_list))

# with open('sample_reviews_1000.json', 'w') as json_file:
#     json.dump(review_list, json_file)

# for i in range(len(data)):
#     if data[i]['stars'] > 3:
#         review_list.append(data[i]['text'])

# for review in review_list:
#     tft.addList(TextParser(review).sortByAlphaNGram(2))
#
# tft.formatTable()
# # tft.displayTermList()
# # tft.displayList()
# tft.displayVert()
