from docx import Document
from nltk.corpus import stopwords, wordnet
from nltk.text import Text
from nltk.tokenize import word_tokenize
import re


def get_text(filename):
    doc = Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)


def percentage(count, total):
    return 100 * count / total;


def lexical_diversity(text):
    return len(set(text)) / len(text)


# remember to use dispersion plots for graphing

def filter_stopwords(text):
    sw = set(stopwords.words('english'))  # saves English stopwords for future use
    filtered = []
    for word in text:
        if word not in sw:
            filtered.append(word)
    return filtered


def convertToText(_input):
    if type(_input) is list:
        textObj = Text(_input)
        return textObj
    else:
        list1 = word_tokenize(_input)
        textObj = Text(list1)
        return textObj


def count_occurrences(word_list):
    word_occurrence = {}
    textWidget = convertToText(word_list)
    for word in word_list:
        word_occurrence[word] = textWidget.count(word)
    return word_occurrence


def remove_punctuation(_input):
    if _input is str:
        _input = re.sub(r'[^\w\s]', '', _input)
    elif _input is list:
        _input = ''.join(_input).re.sub(r'[^\w\s]', '', _input)
    return _input


def extract_synonyms(word, sentence):
    syns = []
    for s in wordnet.synsets(word):
        for l in s.lemma_names():
            if l in sentence and l != word:
                syns.append(l)
    return syns