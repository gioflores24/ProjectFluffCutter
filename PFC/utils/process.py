from nltk.tokenize import word_tokenize
from nltk.sentiment import sentiment_analyzer


def fluffCutter(tokenized):
    try:
        s = sentiment_analyzer(tokenized)
        print(s)
    except Exception as ex:
        print(str(ex))