from docx import Document

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