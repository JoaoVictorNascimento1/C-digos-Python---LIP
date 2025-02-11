#Adiciona um numero de elementos fornecidos pelo usuario a uma lista e verifica se eles são iguais a x ou y, caso sejam são removidos

L1 = []
L2 = []
n=int(input())

for i in range(n):
 a = input()
 L1.append(a)

x = int(input())
y = int(input())

for i in range (len(L1)):
 if len(L1[i]) != x and len(L1[i]) != y:
    L2.append(L1[i])


# COM REMOVE

n = int(input())
lista = []

for i in range(n):
    lista.append(input())

x = int(input())
y = int(input())

i=0
while i < len(lista):
    if len(lista[i]) == x or len(lista[i]) == y:
        lista.remove(lista[i])
        i-=1
    i+=1

print(lista)
print(L2)