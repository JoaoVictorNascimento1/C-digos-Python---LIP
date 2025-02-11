#Adicionar pratos e seus valore a um dicionário e selecionar quais tem seu valor menor que S.

def receber(nome,valor):
    prato = {'nome':nome,
    'valor': valor}
    return prato

def encontrar(pratos,s):
    for i in range(len(pratos)):
        if pratos[i]['valor']<=s:
            print(pratos[i]['nome'], pratos[i]['valor'])

pratos = []
n = int(input('n:'))

for i in range (n):
    nome = input()
    valor = int(input())
    r = receber(nome,valor)
    pratos.append(r)

s = int(input('s: '))
encontrar(pratos,s)
