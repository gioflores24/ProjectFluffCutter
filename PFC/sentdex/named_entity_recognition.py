import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized[5:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            namedEnt = nltk.ne_chunk(tagged, binary=True)
            namedEnt.draw()
            print('finished')
    except Exception as ex:
        print(str(ex))

process_content()


'''
NE Type Examples

ORGANIZATION Georga-Pacific Corp., WHO
PERSON Eddy Bonte, President Obama
LOCATION Murray River, Mount Everest
DATE June, 2008-06-29
TIME
MONEY 175 million Canadian Dollars, GBP 10.40
PERCENT twenty pct, 18.75%
FACILITY Washington Monument, Stonehenge
GPE (Geographical Location) South East Asia, Midlothian
'''
