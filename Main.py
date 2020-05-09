
from WeightedVector import WeightedVector
from TextParser import TextParser
from TermFrequencyTable import TermFrequencyTable
import json
import gui
import tkinter as tk

# ***********************************************
# Unused code but saving for future

# data = [json.loads(line) for line in open('yelp_academic_dataset_review.json', 'r', encoding="utf8")]

# with open('sample_reviews_1000.json', 'w') as json_file:
#     json.dump(review_list, json_file)

# for key in tft1.getTable():
#     if tft1.termFreqTable[key] > 5:
#         print(key, end='')
#         print(" : " + str(tft1.termFreqTable[key]))


# for review in review_list:
#     tft.addList(TextParser(review).sortByAlphaNGram(2))
#
# tft.formatTable()
# # tft.displayTermList()
# # tft.displayList()
# tft.displayVert()
# ***********************************************

# tft1 = TermFrequencyTable()
# tft2 = TermFrequencyTable()
# tft3 = TermFrequencyTable()
# tft4 = TermFrequencyTable()
# tft5 = TermFrequencyTable()
#

# w = WeightedVector()
# w.loadVector()
# w.displayVector()
# review_list = []
#
# with open('sample_reviews_10000_1.json', 'r', encoding="utf8") as f1:
#     data = json.load(f1)
#
# for i in range(5000):
#     tft1.addList(TextParser(data[i]['text']).sortByAlphaNGram(2))
#
# with open('sample_reviews_10000_2.json', 'r', encoding="utf8") as f2:
#     data = json.load(f2)
#
# for i in range(5000):
#     tft2.addList(TextParser(data[i]['text']).sortByAlphaNGram(2))
# #
# with open('sample_reviews_10000_4.json', 'r', encoding="utf8") as f4:
#     data = json.load(f4)
#
# for i in range(5000):
#     tft4.addList(TextParser(data[i]['text']).sortByAlphaNGram(2))
#
# with open('sample_reviews_10000_5.json', 'r', encoding="utf8") as f5:
#     data = json.load(f5)
#
# for i in range(5000):
#     tft5.addList(TextParser(data[i]['text']).sortByAlphaNGram(2))
#
#
# tft1.formatTable()
# tft2.formatTable()
# tft4.formatTable()
# tft5.formatTable()
#
# w.updateVector(tft1.getTable(), -2)
# w.updateVector(tft2.getTable(), -1)
# w.updateVector(tft4.getTable(), 1)
# w.updateVector(tft5.getTable(), 2)
#
# w.saveVector()

#    if data[i]['stars'] == 1:
#         tft1.addList(TextParser(data[i]['text']).sortByAlphaNGram(2))
#         # review_list.append(data[i]['text'])
#     elif data[i]['stars'] == 2:
#         tft2.addList(TextParser(data[i]['text']).sortByAlphaNGram(2))
#
#     elif data[i]['stars'] == 3:
#         tft3.addList(TextParser(data[i]['text']).sortByAlphaNGram(2))
#
#     elif data[i]['stars'] == 4:
#         tft4.addList(TextParser(data[i]['text']).sortByAlphaNGram(2))
#
#     elif data[i]['stars'] == 5:
#         tft5.addList(TextParser(data[i]['text']).sortByAlphaNGram(2))
#

# w.loadVector()

# testNum = 10
#
# print(data[testNum]['text'])
# print(data[testNum]['stars'])
# print(w.eval(data[testNum]['text']))

# for key in sorted(w.compareVector):
#     if abs(w.compareVector[key]) > 4:
#         print(key, w.compareVector[key])



window = tk.Tk()
window.title("Yelp Sentiment Analyzer")
gui = gui.MainApplication(window)
gui.grid(row=0, column=0)
tk.mainloop()
