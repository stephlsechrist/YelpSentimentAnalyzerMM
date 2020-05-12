
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



# ***********************
# This will tell you the range of the tests
# ***********************
#
# w = WeightedVector()
# w.loadVector()
# star = 5
#
# with open(f"sample_reviews_100_{star}.json", 'r', encoding="utf8") as f:
#     data = json.load(f)
#
# total = 0
# difference = 0
#
# for i in range(100):
#     score = w.predict(data[i]['text'])
#     print(score, end='')
#     print(" " + str(w.eval((data[i]['text']))))
#     total += score
#     difference += abs(score - star)
#
# print(total / 100)
# print(difference / 100)



# 1308077 terms in the weighted vector

# ***********************
# this is for cutting the massive reviewfile
# ***********************

# review_list1 = []
# review_list2 = []
# review_list3 = []
# review_list4 = []
# review_list5 = []
# count1 = 0
# count2 = 0
# count3 = 0
# count4 = 0
# count5 = 0

# data = [json.loads(line) for line in open('yelp_academic_dataset_review.json', 'r', encoding="utf8")]
#
# for i in range(1000000, 1010000):
#     if data[i]['stars'] == 1:
#         count1 += 1
#         if count1 <= 100:
#             review_list1.append(data[i])
#     elif data[i]['stars'] == 2:
#         count2 += 1
#         if count2 <= 100:
#             review_list2.append(data[i])
#     elif data[i]['stars'] == 3:
#         count3 += 1
#         if count3 <= 100:
#             review_list3.append(data[i])
#     elif data[i]['stars'] == 4:
#         count4 += 1
#         if count4 <= 100:
#             review_list4.append(data[i])
#     elif data[i]['stars'] == 5:
#         count5 += 1
#         if count5 <= 100:
#             review_list5.append(data[i])
#
#
# with open('sample_reviews_100_1.json', 'w') as json_file:
#     json.dump(review_list1, json_file)
#
# with open('sample_reviews_100_2.json', 'w') as json_file:
#     json.dump(review_list2, json_file)
#
# with open('sample_reviews_100_3.json', 'w') as json_file:
#     json.dump(review_list3, json_file)
#
# with open('sample_reviews_100_4.json', 'w') as json_file:
#     json.dump(review_list4, json_file)
#
# with open('sample_reviews_100_5.json', 'w') as json_file:
#     json.dump(review_list5, json_file)


# *************************************
# This is to text averages
# *************************************

# with open('sample_reviews_10000_25000_1.json', 'r', encoding="utf8") as f:
#     data = json.load(f)
#
# average = 0
# count = 2000
# high = w.eval(data[0]['text'])
# low = w.eval(data[0]['text'])

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
# 5star -            3.204176265824693      -13.028643924917958        16.88578222214421
# 4star -            1.986488533999484      -17.01176984015702         14.129129977512243
# 2star -           -9.19865360868044       -34.297560069624424        3.1208862013592356
# 1star -           -12.6266329264273       -46.05009804491635         0.9829178989403702



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
