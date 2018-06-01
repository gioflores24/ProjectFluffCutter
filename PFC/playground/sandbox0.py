
from nltk.book import *
from nltk.draw.dispersion import dispersion_plot
from matplotlib import *
from numpy import *
from nltk.probability import FreqDist

V = set(text1)
long_words = [w for w in V if len(w) > 15]
print(sorted(long_words))