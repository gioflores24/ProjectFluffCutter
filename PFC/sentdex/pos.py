import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
#part-of-speech tagging: labeling the parts of speech to every single word from whatever you're feeding

#punkt sentence tokenizer: unsupervised ML sentence tokenizer: you can train it if you want.

train_text = state_union.raw('2005-GWBush.txt')
sample_text = state_union.raw('2006-GWBush.txt')


custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

#PunktSentenceTokenizer: abstract class for default sentence tokenizer (sent_tokenize)
#initialize it with no parameters, and it will not require training. Since we included an argument, it must be trained.

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)
    except Exception as e:
        print(str(e))


process_content()