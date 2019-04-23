#separador de texto que não remove pontuação, visto que a existencia de pontuação pode afetar a classificação da palavra.
text = "I, uh, don't like it. re"
words = text.split()
tags = []
#dicionarios de unigramas e bigramas que indicam a tag mais provavel para uma dada palavra (obitda através no analyzer).
unigrams = {'I': 'SBJ', 'uh': 'NOUN', "don't":'NOT', 'like': 'EXP', 'it': 'OBJ'}
bigrams = {"don't like": 'NEXP', 'like it': 'OBJ'}
#inicio do algoritimo do PoS tagger tendo os dados predefinidos:
for index, word in enumerate(words):
    if index == 0 or words[index - 1].count(',') != 0 or words[index - 1].count('.') != 0:
        word = word.replace(',', '').replace('.', '')
        if unigrams.get(word):
            tags.append(unigrams[word])
        else:
            tags.append('UNK')
        #o primeiro if checa se a palavra anterior tem pontuação ou se não ha palavra anterior, então ele atribui um unigrama ou UNK baseado nos dados do dicionario.
    elif unigrams.get(word.replace(',', '').replace('.', '')):
        word = word.replace(',', '').replace('.', '')
        bigram = words[index - 1] + " " + word
        if bigrams.get(bigram):
            tags.append(bigrams[bigram])
        #assumindo que há uma palavra anterior e a palavra estudada está presente no dicionarios de unigramas, tenta-se analisar com base em bigrama e, se falhar, com base em unigrama.
        else:
            tags.append(unigrams[word])
    else:
        tags.append('UNK')
        #no caso de não se ter o valor da palavra estudada nos dicionarios, ela é definida como UNK.
words = [word.replace('.', '') for word in words]
words = [word.replace(',','') for word in words]
tagged_words = list(zip(tags, words))
tagged_text = "((S "

for tags, words in tagged_words:
    tagged_text += "({} {}) ".format(tags, words)
tagged_text = tagged_text.rstrip() + "))"
print(tagged_text)
