#corpus de treino que será importado diretamente dos arquivos.
corpus = open('PoS Tagging/Corpora/traindata').read()
corpus = corpus.replace(',','').replace('.','').replace('\n','').replace('\n','')

filtered_corpora = [] #o objetivo desse codigo é gerar uma lista no formato: ['tag', 'palavra', 'tag', ... 'palavra']

for i in range(len(corpus)):
    if corpus[i] == ')' and corpus[i - 1] != ' ' and corpus[i - 1] != ')':
        num = 0
        letters = []
        tagged_word = []
        #o loop abaixo fornece uma lista das letras que compõe a string desejada na ordem inversa.
        while corpus[i - num - 1] != '(':
            num += 1
            letters.append(corpus[i - num])
        #o loop abaixo desinverte a lista.
        for rep in range(1, len(letters) + 1):
            rep *= -1
            tagged_word.append(letters[rep])
        #a linha abaixo junta as letras para formar a string.
        tagged_word = ''.join(tagged_word)
        #a linha abaixo separa a string em duas: uma para a tag e outra para a palavra.
        tag_word = tagged_word.split(' ')
        if tag_word[0] != '-NONE-':
            filtered_corpora.append(tag_word[0]) #adiciona a tag à lista.
            filtered_corpora.append(tag_word[1]) #adiciona a palavra à lista.
