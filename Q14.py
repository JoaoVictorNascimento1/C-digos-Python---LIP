#Função para remover um elemento da lista no indice i

def remover(a,i):
    a.pop(i)
    if a == []:
        print('lista vazia')
    for j in range (len(a)):
        print(a[j], end = ' ')

a = []
n = int(input())

for i in range (n):
    a.append(int(input()))
i = int(input())
remover(a,i)