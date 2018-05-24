from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from docx import Document

# tokenizing - word tokenizers...sentence tokenizers (separates by words...separates by sentence)
#lexicon and corpora
# corpus - body of text. ex: medical journals, presidential speeches, English lang
# lexicon - words and their meanings.




# def getText(filename):
#     doc = Document(filename)
#     fullText = []
#     for para in doc.paragraphs:
#         fullText.append(para.text)
#     return '\n'.join(fullText)


example_sentence = "This is an example showing off stop word filtration."
stop_words= set(stopwords.words('english')) #pre-defined stop words

words = word_tokenize(example_sentence, language='english')

filtered_sentence = []

# for w in words:
#      if w not in stop_words:
#          filtered_sentence.append(w)

filtered_sentence = [w for w in words if not w in stop_words]
print(filtered_sentence)




