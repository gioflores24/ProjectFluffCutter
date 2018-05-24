
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import PorterStemmer
from docx import Document

#stemming is a form of normalization

ps = PorterStemmer()

example_words = [
    'python', 'pythoner', 'pythoning', 'pythoned', 'pythonic', 'pythonly'
]


for w in example_words:
    print(ps.stem(w))

new_text = "It is very important to be pythonly while you are pythoning with python." \
           "All pythoners have pythoned poorly at least once"

words = word_tokenize(new_text, language='english')

for w in words:
    print(ps.stem(w))