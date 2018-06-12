import copy
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.sentiment import sentiment_analyzer
from nltk.tokenize import sent_tokenize
from utils.preprocess import filter_stopwords
from utils.preprocess import count_occurrences




def fluff_cutter(word_list):
    try:
        bySentence = sent_tokenize(' '.join(word_list))
        highlighted = []
        filtered = filter_stopwords(word_list)
        counts = count_occurrences(filtered)
        for key, value in counts.items():
            if value >= 2:
                highlighted.append(key)


        return highlighted

    except Exception as ex:
        print(str(ex))