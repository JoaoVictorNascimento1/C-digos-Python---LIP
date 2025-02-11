#Se o indice do elemento da lista for impar remove o maior nome, se for par remove o menor. Até restar um.

n = int(input())
lista = []

for i in range (n):
    lista.append(input())

i = 1
while len(lista) > 1:
    
    if i%2 != 0:
        maior = lista[0]
    for nome in lista:
        if len(nome) > len(maior):
            maior = nome
            lista.remove(maior)

    else:
        menor = lista[0]
        for nome in lista:
            if len(nome) < len(menor):
                menor = nome
                lista.remove(menor)

    i+=1

print(lista[0])