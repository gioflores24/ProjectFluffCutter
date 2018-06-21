from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.draw.dispersion import dispersion_plot
from matplotlib import *
from numpy import *
from nltk.probability import FreqDist
from nltk.corpus import wordnet
from utils.preprocess import convert_to_text
from utils.preprocess import filter_stopwords
from utils.preprocess import count_occurrences
from utils.preprocess import remove_punctuation
from nltk.tokenize import RegexpTokenizer
import re
from nltk.corpus import stopwords

import collections

highlighted = []
text = "Not giving the poor food is very bad. It's bad because they starve. If they starve, everyone is guilty."
text2= """
Good afternoon, everyone. 
My name is Giovanni Flores, and on behalf of the 
computer science department and the McNair program, 
I am conducting research under the mentorship of 
Dr. Craig Reinhart on how to eliminate redundancy in 
written text, such as filler content and repetition. 
To accomplish this, I am constructing a text editor 
that highlights said redundancy. With this, I hope to 
facilitate proofreading, and allow ideas to be communicated 
more clearly in writing. Thank you. 
"""
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

text2 = word_tokenize(text2)
filtered = filter_stopwords(text2)
print(filtered)

fdist = FreqDist(filtered)
fdist.plot()

list_of_sentences = sent_tokenize(text)

# if len(list_of_sentences) > 2:
#     for i in range(len(list_of_sentences) - 1):
#         sent1 = list_of_sentences[i+1]
#         sent2 = list_of_sentences[i]



# if len(list_of_sentences) > 2:
#     for i in range(len(list_of_sentences) - 1):
#         sent1 = list_of_sentences[i+1]
#         sent2 = list_of_sentences[i]
#         for word in sent1:
            


