# coding : utf-8

import csv, nltk, string
from nltk.tokenize import  word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from collections import Counter 

martineau = "Richard-Martineau.csv"

fichier = open(martineau)
motsrecherches = csv.reader(fichier)
next(motsrecherches)

a = []
bigram = []

for mots in motsrecherches:
    # print(mots[3])

    tokens = word_tokenize(mots[3])
    # print(tokens)

    fr = SnowballStemmer("french")

    racines = [fr.stem(mot) for mot in word_tokenize(mots[3])if mot not in stopwords.words("french") and mot not in string.punctuation and mot != "’" and mot != "..." and mot != "«" and mot != "»" and mot != "``"]
    # print(racines)

    for racine in racines:
        a.append(racine)

    for x, y in enumerate(mots[:-1]): 
	    bigrams="{} {}".format(racines[x], racines[x+1])
        if "islam" in bigrams or "musulm" in bigrams:
        # print(bigrams)
        bigram.append(bigrams)

freq = Counter(bigram)
print(freq.most_common(50)) 