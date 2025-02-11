#Verifica se um número é frequente numa lista ou não (Aparece mais de 2x = Frequente)

lista = []
for i in range (3):
    m = input().split()
    lista.append(m)

n = input()
cont = 0

for lista in lista:
    if n in lista:
        cont += 1

if cont == 2:
 print(f'{n} é um número frequente')
else:
 print(f'{n} não é um número frequente')