import copy
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.sentiment import sentiment_analyzer


def fluff_cutter(text):
    try:
        highlighted = []
        sw = set(stopwords.words('english')) #saves English stopwords for future use
        filtered = []
        for word in text:
            if word not in sw:
                filtered.append(word)
        highlighted = filtered[:]
        return highlighted
    except Exception as ex:
        print(str(ex))