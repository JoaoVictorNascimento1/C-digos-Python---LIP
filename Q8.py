#Remove nos indices impares os elementos com tamanho maior que n

l = int(input())
lista = []


for _ in range(l):
    ingredientes = input().split()
    lista.append(ingredientes)

n = int(input())  
pizzas = []

for i in range(l):
    if i % 2 != 0: 
        lista_nova = []
        for ingrediente in lista[i]:
            if len(ingrediente) > n:
                lista_nova.append(ingrediente)
        pizzas.append(lista_nova)

for pizza in pizzas:
    print(pizza)
