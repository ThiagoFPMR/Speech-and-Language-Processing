
#separador de tags e palvras:
corpus = "((S (UBK re) (UBK re) (ARK re) (SBJ I) (NOUN uh) (NOT don't) (NOT don't) (NEXP like) (NEXP like) (OBJ it) (UNK re) ))"
corpus = corpus.replace("(", "").replace(")", "").replace("S", "").split()
#definidas as duas listas que serão utilizadas pelo codigo para ter acesso as tags e as palavras (as duplas estão relacionadas pelos indices das listas)?
tags = []
words = []
#abaixo fica o separador que filtra o corpus fornecido para o training do tagger, o qual define os valores das listas de tags e words usando o corpus como base:
for index, word in enumerate(corpus):
    if index % 2 == 0:
        tags.append(word)
    else:
        words.append(word)

unigrams = {} #definido o dicionario que será o output desse codigo e será usado pelo PoS Tagger.

for word in set(words):
    word_repetitions = [i for i, w in enumerate(words) if w == word]
    rep_tags = [tags[ind] for ind in word_repetitions]
    tag_counts = {}
    for tag in set(rep_tags):
        tag_counts[tag] = rep_tags.count(tag)
    word_tags = {}
    word_tags[word] = tag_counts #serve para caso eu queira ter uma contagem das tags para melhor vizualização (utilizar o print).
    #print(tag_counts)
    hight_tag_count = max(tag_counts.values())
    hight_tag = [key for key, value in tag_counts.items() if value == hight_tag_count]
    if sum(tag_counts.values()) > 1:
        unigrams[word] = hight_tag[0]
    else:
        unigrams[word] = 'UNK'
        
print(unigrams)
