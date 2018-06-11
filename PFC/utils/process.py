import copy
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.sentiment import sentiment_analyzer
from utils.preprocess import filter_stopwords
from utils.preprocess import count_occurrences


def fluff_cutter(word_list):
    try:
        highlighted = []
        #highlighted = filter_stopwords(text)
        counts = count_occurrences(word_list)
        print(counts)
        for key, value in counts.items():
            highlighted.append(key)
        return highlighted

    except Exception as ex:
        print(str(ex))