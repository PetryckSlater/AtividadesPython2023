v = []
mq10 = []

numero = 4
for i in range(numero): 
    v.append(input(f'Digite quatro elementos da linha {i+1} da matriz separada por espaço: ').split(" "))
maior_q10 = 0
for i in range(len(v)):
    for j in range(len(v[i])):
        if int(v[i][j]) > 10:
            maior_q10 +=1
            mq10.append(v[i][j])

print('Elementos maiores que 10 na matriz: ', maior_q10)
print(mq10)