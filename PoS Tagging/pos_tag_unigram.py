corpus = "((S (UNK re) (SBJ I) (NOUN uh) (NOT don't) (NEXP like) (OBJ it) (UNK re)))"
corpus = corpus.replace("(", "").replace(")", "").replace("S", "").split()
#separador de tags e palvras:
tags = []
words = []
for index, word in enumerate(corpus):
    if index % 2 == 0:
        tags.append(word)
    else:
        words.append(word)

for word in set(words):
    word_rep = [i for i, w in enumerate(words) if w == word]
    print(word + str(word_rep))
    #o print é so de teste
print(corpus)
print(words)
print(tags)
