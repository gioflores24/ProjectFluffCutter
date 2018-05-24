import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

#we can separate by sentence, word, and part of speech tag

#we can only chunk things that are touching.

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)


def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP><NN>?} """ #any form of an adverb, 0 or more of these

            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            print(chunked)
    except Exception as e:
        print(str(e))


process_content()
