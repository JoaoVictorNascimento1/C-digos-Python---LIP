#Verifica se todas as listas posssuem uma certa fruta

lista1 = list(input().split(' '))
lista2 = list(input().split(' '))
lista3 = list(input().split(' '))

b = 0
c = 0
d = 0
fruta = input()

for i in range (len(lista1)):
    if lista1[i] == fruta:
        b += 1
        break
for i in range (len(lista2)):
    if fruta == lista2[i]:
        c += 1
        break
for i in range (len(lista3)):
    if fruta == lista3[i]:
        d += 1
        break

if b == 1 and c == 1 and d == 1:
 print(f'{fruta} aparece em todas as saladas')
else:
 print(f'{fruta} não aparece em todas as saladas')