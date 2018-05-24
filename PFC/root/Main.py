import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import state_union
import tkinter
from tkinter import filedialog
from utils.preprocess import getText




def process(tokenized):
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            namedEnt = nltk.ne_chunk(tagged, binary=True)
            namedEnt.draw()
    except Exception as ex:
        print(str(ex))

def main():
    root = tkinter.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    train_text = state_union.raw("2006-GWBush.txt")
    sample_text = getText(file_path)
    custom_sentence_tokenizer = PunktSentenceTokenizer(train_text)
    t = custom_sentence_tokenizer.tokenize(sample_text)
    process(t)

main()
