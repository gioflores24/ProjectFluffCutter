from docx import Document
from nltk.corpus import stopwords


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
