#separador de texto que não remove pontuação, visto que a existencia de pontuação pode afetar a classificação da palavra.
text = "I, uh, don't like it."
words = text.split()
tags = []
#dicionarios de unigramas e bigramas que indicam a tag mais provavel para uma dada palavra (obitda através no analyzer).
unigrams = {'I': 'SBJ', 'uh': 'NOUN', "don't":'NOT', 'like': 'EXP', 'it.': 'OBJ'}
bigrams = {"don't like": 'NEXP', 'like it': 'OBJ'}
#inicio do algoritimo do PoS tagger tendo os dados predefinidos:
for index, word in enumerate(words):
    if index == 0 or words[index - 1].count(',') != 0 or words[index - 1].count('.') != 0:
        word = word.replace('.', '')
        word = word.replace(',', '')
        tags.append(unigrams[word])
        print(word)
    else:
        word = word.replace('.', '')
        word = word.replace(',', '')
        bigram = words[index - 1] + " " + word
        tags.append(bigrams[bigram])
        print(bigram)

words = [word.replace('.', '') for word in words]
words = [word.replace(',','') for word in words]

print(words)
print(tags)
print(list(zip(tags, words)))
