#Validar se uma lista tem seu elementos ordenados de forma crescente;

n = int(input())
lista = []

for i in range(n):
 lista.append(int(input()))

ordem = True

for i in range(n-1):
 if lista[i] > lista[i+1]:
    ordem = False

if ordem == True:
 print('ELEMENTOS ORDENADOS')
else:
 print('ELEMENTOS NÃO ORDENADOS')