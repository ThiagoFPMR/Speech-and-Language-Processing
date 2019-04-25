
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

bigrams = {} #isso ainda não serve, para nada, so para ficar ai amostra mesmo, servindo de motivação, sla

for index, word in enumerate(words):
    if index >= 1:
        bigram = tags[index - 1] + " " + word
        #os bigramas serão formados por uma tag e a palavra que a segue, ja que assim reprensenta-se melhor relações gramaticais
        #e como uma palavra se comporta quando precedida de uma especifica classe de palavra (ja que para intuito do PoS Tagger,
        #vale mais considerar isso a cada caso de palavra precedida por outra palavra), o que tambem permite a coleta de mais
        #dados ja que duplas diferentes de palvras podem ser consideradas a mesma sequência, então favor não confundir o modelo de
        #bigrama usado aqui com o taggeamento da palavra em questão.
        print(bigram)
