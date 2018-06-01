from nltk.tokenize import word_tokenize



def fluffCutter(tokenized):
    try:
        words = []
        for i in tokenized:

            words = word_tokenize(i)
            # tagged = nltk.pos_tag(words)
            # namedEnt = nltk.ne_chunk(tagged, binary=True)
            # namedEnt.draw()
        return words
    except Exception as ex:
        print(str(ex))