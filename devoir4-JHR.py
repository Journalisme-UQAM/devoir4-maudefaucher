# coding : utf-8

### BONJOUR MAUDE!
### J'AI REBAPTISÉ MA COPIE DE TRAVAIL DE TON SCRIPT PARCE QUE C'EST JUSTE PLUS FACILE DE LE FAIRE ROULER POUR MOI
### MAIS CE N'EST PAS PARCE QUE JE N'AIMAIS PAS LE NOM QUE TU AVAIS CHOISI! :)

import csv, nltk, string
from nltk.tokenize import  word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from collections import Counter 

# martineau = "Richard-Martineau.csv"
martineau = "../martino.csv" ### CHANGEMENT JUSTE POUR REFLÉTER CE QU'IL Y A SUR MON ORDI

fichier = open(martineau)
motsrecherches = csv.reader(fichier)
next(motsrecherches)

a = []
bigram = []

for mots in motsrecherches:
    # print(mots[3])
    print(mots[1]) ### J'AFFICHE LA DATE À CHAQUE CHRONIQUE POUR VOIR LE SCRIPT PROGRESSER DANS LE TERMINAL

    tokens = word_tokenize(mots[3])
    # print(tokens)

    fr = SnowballStemmer("french")

    racines = [fr.stem(mot) for mot in word_tokenize(mots[3])if mot not in stopwords.words("french") and mot not in string.punctuation and mot != "’" and mot != "..." and mot != "«" and mot != "»" and mot != "``"]
    # print(racines)

    ### JE METS EN COMMENTAIRES LA PETITE BOUCLE CI-DESSOUS CAR ELLE NE SEMBLE SERVIR À RIEN...
    # for racine in racines:
    #     a.append(racine)

    # for x, y in enumerate(mots[:-1]): ### ICI, TU UTILISES LA VARIABLE «MOTS», ALORS QUE C'EST PLUTÔT LA VARIABLE «RACINES» DANS LAQUELLE TU VEUX FAIRE TA BOUCLE
    for x, y in enumerate(racines[:-1]):
        bigrams="{} {}".format(racines[x], racines[x+1])
        if "islam" in bigrams or "musulm" in bigrams:
        # print(bigrams) ### C'ÉTAIT UNE BONNE IDÉE DE FAIRE CE PRINT... MAIS IL FALLAIT L'INDENTER D'UN CRAN À DROITE
        # bigram.append(bigrams) ### CETTE LIGNE ÉTAIT MAL INDENTÉE
            bigram.append(bigrams) ### C'EST ICI QU'ELLE DOIT ALLER
    print(len(bigram)) ### AFFICHAGE POUR VOIR LE PROGRÈS RÉALISÉ

freq = Counter(bigram)
print(freq.most_common(50)) 

### DES COMMENTAIRES AURAIENT ÉTÉ APPRÉCIÉS POUR SAVOIR CE QUE TU FAISAIS; MAIS AUSSI POUR ME DÉMONTRER QUE TU COMPRENAIS CE QUE TU FAISAIS...
### LES PROBLÈMES D'INDENTATION ME LAISSENT PENSER QUE TU N'AS PAS ESSAYÉ DE FAIRE ROULER TON SCRIPT...