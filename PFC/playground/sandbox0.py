
from nltk.book import *
from nltk.draw.dispersion import dispersion_plot
from matplotlib import *
from numpy import *
from nltk.probability import FreqDist

V = set(text1)
long_words = [w for w in V if len(w) > 15]
print(sorted(long_words))

# while count < len_of_highlighted:
#     if selected[i] == word_list[j]:
#         color_text(text, tags[i], word, 'black', 'yellow')
#         i += 1
#     j += 1
#     count += 1