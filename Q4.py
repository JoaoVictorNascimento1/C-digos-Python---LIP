#Deleta elementos iguais da lista fornecida pelo usuário

n = int(input())
lista = []

for i in range (n):
    lista.append(int(input()))

i=0
while i < len(lista):
    j = i + 1
    while j < len(lista):
        if lista[i] == lista[j]:
            del lista[j]
            j -= 1
        j += 1
    i += 1

print(lista)
