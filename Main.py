
from WeightedVector import WeightedVector
from TextParser import TextParser
from TermFrequencyTable import TermFrequencyTable
import json
import gui
import tkinter as tk

# tft1 = TermFrequencyTable()
# tft2 = TermFrequencyTable()
# tft3 = TermFrequencyTable()
# tft4 = TermFrequencyTable()
# tft5 = TermFrequencyTable()

w = WeightedVector()
w.loadVector()

# print(len(w.compareVector))

# review_list1 = []
# review_list2 = []
# review_list4 = []
# review_list5 = []
# count1 = 0
# count2 = 0
# count4 = 0
# count5 = 0

# print(len(w.compareVector))

# 670275
# 695434
# 742724
# 790096
# 836070
# 881863
# 926446
# 969821
# 1010581
# 1052111
# 1092878
# 1153710
# 1230720
# 1308077

# ***********************
# this is for cutting the massive reviewfile
# ***********************

# data = [json.loads(line) for line in open('yelp_academic_dataset_review.json', 'r', encoding="utf8")]
#
# for i in range(len(data)):
#     if data[i]['stars'] == 1:
#         count1 += 1
#         if 25000 > count1 >= 10000:
#             review_list1.append(data[i])
#     elif data[i]['stars'] == 2:
#         count2 += 1
#         if 25000 > count2 >= 10000:
#             review_list2.append(data[i])
#     elif data[i]['stars'] == 4:
#         count4 += 1
#         if 25000 > count4 >= 10000:
#             review_list4.append(data[i])
#     elif data[i]['stars'] == 5:
#         count5 += 1
#         if 25000 > count5 >= 10000:
#             review_list5.append(data[i])


# with open('sample_reviews_10000_25000_1.json', 'w') as json_file:
#     json.dump(review_list1, json_file)
#
# with open('sample_reviews_10000_25000_2.json', 'w') as json_file:
#     json.dump(review_list2, json_file)
#
# with open('sample_reviews_10000_25000_4.json', 'w') as json_file:
#     json.dump(review_list4, json_file)
#
# with open('sample_reviews_10000_25000_5.json', 'w') as json_file:
#     json.dump(review_list5, json_file)




# *************************************
# This is to text averages
# *************************************

# with open('sample_reviews_10000_25000_1.json', 'r', encoding="utf8") as f:
#     data = json.load(f)
#
# average = 0
# count = 2000
# high = -10000
# low = 10000
# for i in range(count):
#     average += w.eval(data[i]['text'])
#     if w.eval(data[i]['text']) > high:
#         high = w.eval(data[i]['text'])
#     if w.eval(data[i]['text']) < low:
#         low = w.eval(data[i]['text'])
#
# print(average / count)
# print(low)
# print(high)

#                           average                   min                       max
# 5star -             3.204176265824693      -13.028643924917958        16.88578222214421
# 4star -             1.986488533999484      -17.01176984015702         14.129129977512243
# 2star -            -9.19865360868044       -34.297560069624424        3.1208862013592356
# 1star -            -12.6266329264273       -46.05009804491635         0.9829178989403702



# *************************************
# This is to add terms to the weighted vector
# *************************************

# for i in range(13000, 15000):
#     tft1.addList(TextParser(data[i]['text']).sortByAlphaNGram(2))
#
# with open('sample_reviews_10000_25000_2.json', 'r', encoding="utf8") as f2:
#     data = json.load(f2)
#
# for i in range(13000, 15000):
#     tft2.addList(TextParser(data[i]['text']).sortByAlphaNGram(2))
#
# with open('sample_reviews_10000_25000_4.json', 'r', encoding="utf8") as f4:
#     data = json.load(f4)
#
# for i in range(13000, 15000):
#     tft4.addList(TextParser(data[i]['text']).sortByAlphaNGram(2))
#
# with open('sample_reviews_10000_25000_5.json', 'r', encoding="utf8") as f5:
#     data = json.load(f5)
#
# for i in range(13000, 15000):
#     tft5.addList(TextParser(data[i]['text']).sortByAlphaNGram(2))

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

# w.loadVector()
# print(len(w.compareVector))


# *************************************
# This is the gui component
# *************************************

# window = tk.Tk()
# window.title("Yelp Sentiment Analyzer")
# gui = gui.MainApplication(window)
# gui.grid(row=0, column=0)
# tk.mainloop()
