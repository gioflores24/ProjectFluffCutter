from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize('better', pos='a'))
print(lemmatizer.lemmatize('infamous', pos='v'))
print(lemmatizer.lemmatize('current', pos='v'))