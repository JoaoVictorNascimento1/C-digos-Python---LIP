lista = []

for i in range (4):
 lista.append(input())

novo_ingrediente = input()
b = False

for i in range (4):
    if lista[i] == novo_ingrediente:
        b = True
        break
    else:
        b = False

if b == True:
 print(f'Pizza já tem {novo_ingrediente}')
else:
 print(f'Colocando {novo_ingrediente} na pizza')