import copy
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.sentiment import sentiment_analyzer
from utils.preprocess import filter_stopwords


def fluff_cutter(text):
    try:
        highlighted = []
        highlighted = filter_stopwords(text)
        return highlighted
    except Exception as ex:
        print(str(ex))