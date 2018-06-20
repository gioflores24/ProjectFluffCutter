from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.draw.dispersion import dispersion_plot
from matplotlib import *
from numpy import *
from nltk.probability import FreqDist
from nltk.corpus import wordnet
from utils.preprocess import convertToText
from utils.preprocess import count_occurrences
from utils.preprocess import remove_punctuation
from nltk.tokenize import RegexpTokenizer
import re

import collections

highlighted = []
text = "Not giving the poor food is very bad. It's bad because they starve. If they starve, everyone is guilty."

# word_list = word_tokenize(text)
# print(word_list)
#
#
# counts = count_occurrences(word_list)
# for key, value in counts.items():
#     if value >= 2:
#         highlighted.append(key)
#
# print(highlighted)


num_of_sentences = sent_tokenize(text)

if len(num_of_sentences) > 2:
    for i in range(len(num_of_sentences) - 1):
        sent1 = num_of_sentences[i+1]
        sent2 = num_of_sentences[i]
        for word in sent1:
            

