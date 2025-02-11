#Remove os dois menores numeros de uma lista

lista = []

for i in range(4):
    lista.append(int(input()))

for _ in range(2):  
    menor = min(lista)
    lista.remove(menor) 

for n in lista:
    print(n)
