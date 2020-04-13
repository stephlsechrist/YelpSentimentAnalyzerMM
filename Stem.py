# import these modules
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# class Stem:
#     def __init__(self, text):
#         ps = PorterStemmer()
#         self.text = text
#
#     def stem(self):
#         # ps = PorterStemmer()
#         stemmedList = []
#
#         words = word_tokenize(self.text)
#
#         for w in words:
#             stemmedList.append(self.ps.stem(w))
#
#         return stemmedList

def stem(text):
    ps = PorterStemmer()
    # self.text = text
    stemmedList = []

    # words = word_tokenize(text)

    for w in text:
        stemmedList.append(ps.stem(w))

    print(stemmedList)
    return stemmedList