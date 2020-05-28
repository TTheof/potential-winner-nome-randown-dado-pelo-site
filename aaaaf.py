import random
aa = [0,1]
a= random.choice(aa)
#             de manha                                               a tarde
almoço= [['só arroz','miojo','carne','ovo cozido','ovo frito'],['maça','café','chá','bolo']]
if a>0:
    print ('a tarde eu vou comer/beber')
else:
    print ('de manha eu vou comer/beber')
kk = random.choice(almoço[a])
print ('um/uma', kk)