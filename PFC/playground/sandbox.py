
from nltk.tokenize import word_tokenize
from nltk.draw.dispersion import dispersion_plot
from matplotlib import *
from numpy import *
from nltk.probability import FreqDist
from nltk.corpus import wordnet
import collections

text = "Not giving the poor food is very bad. It's bad because they starve. Starvation causes guilt among the people"
word_list = word_tokenize(text)
word_counts = collections.Counter(word_list)
for word, count in sorted(word_counts.items()):
    print('"%s"  is repeated %d time%s' % (word, count, "s" if count > 1 else ""))


