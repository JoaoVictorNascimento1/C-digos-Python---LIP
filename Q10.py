#Procura um nome numa lista fornecida pelo usuario

lista1 = list(input().split(','))
lista2 = list(input().split(','))
lista3 = list(input().split(','))
lista_final = (lista1 + lista2 + lista3)

b = False
nome = input()
for i in range (len(lista_final)):
    if lista_final[i] == nome:
        b = True

if b == True:
 print(f'Tem {nome} em alguma turma')
else:
 print(f'Nenhuma turma tem {nome}')