corpus = "(S (NP (NNP John)) (NP (NNP Mary))) (. .))"
corpus = corpus.replace(',','').replace('.','')

for i in range(len(corpus)):

#o objetivo desse codigo é gerar uma lista do tipo ['tag', 'palavra', 'tag', . . . 'palavra']
