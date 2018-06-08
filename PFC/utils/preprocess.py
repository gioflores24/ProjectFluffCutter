from docx import Document
from nltk.corpus import stopwords
from nltk.text import Text
from nltk.tokenize import word_tokenize


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

#remember to use dispersion plots for graphing

def filter_stopwords(text):
    sw = set(stopwords.words('english'))  # saves English stopwords for future use
    filtered = []
    for word in text:
        if word not in sw:
            filtered.append(word)
    return filtered

def convertToText(text):
    word_list = word_tokenize(text)
    textObj = Text(word_list)
    return textObj

def count_occurrences(text):
    word_list = word_tokenize(text)
    word_occurrence = {}
    for word in word_list:
        # print(word)
        word_occurrence[word] = (convertToText(word_list).count(word))
    return word_occurrence


