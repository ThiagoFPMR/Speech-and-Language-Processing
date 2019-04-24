corpus = "((S (SBJ I) (NOUN uh) (NOT don't) (NEXP like) (OBJ it) (UNK re)))"
corpus = corpus.replace("(", "").replace(")", "").replace("S", "").split()
#separador de tags e palvras:
tags = []
words = []
for index, word in enumerate(corpus):
    if index % 2 == 0:
        tags.append(word)
    else:
        words.append(word)



print(corpus)
print(words)
print(tags)
