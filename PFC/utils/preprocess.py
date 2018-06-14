from docx import Document
from nltk.corpus import stopwords, wordnet
from nltk.text import Text
from nltk.tokenize import word_tokenize
import re
import math
from collections import Counter


def get_text(filename):
    doc = Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)


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


def convert_to_text(_input):
    if type(_input) is list:
        text_obj = Text(_input)
        return text_obj
    else:
        list1 = word_tokenize(_input)
        text_obj = Text(list1)
        return text_obj


def count_occurrences(word_list):
    word_occurrence = {}
    text_widget = convert_to_text(word_list)
    for word in word_list:
        word_occurrence[word] = text_widget.count(word)
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


word_filter = re.compile(r'\w+')


def calc_cos(v1, v2):
    intersec = set(v1.keys()) & set(v2.keys())
    top = sum([v1[x] * v2[x] for x in intersec])
    sum_of_first_vec = sum([v1[x] ** 2 for x in v1.keys()])
    sum_of_second_vec = sum([v2[x] ** 2 for x in v2.keys()])
    bottom = math.sqrt(sum_of_first_vec) * math.sqrt(sum_of_second_vec)
    if not bottom:
        return 0.0
    else:
        return float(top) / bottom


def convert_text_to_vec(_input):
    all_instances = word_filter.findall(_input)
    return Counter(all_instances)


def cosine_similarity(sentence1, sentence2):
    v1 = convert_text_to_vec(sentence1)
    v2 = convert_text_to_vec(sentence2)
    cos = calc_cos(v1, v2)
    return cos
