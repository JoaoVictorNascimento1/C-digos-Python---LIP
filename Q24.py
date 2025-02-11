# O código gerencia pedidos de pizza, armazenando nome, preço e ingredientes, 
# e encontra a pizza mais cara que contém um ingrediente específico.

def pedidos(n):
    pizzas = []
    for i in range (n):
        nome = input()
        preço = int(input())
        ing = input().split(' ')
        pizza = {'nome':nome,
        'preço': preço,
        'ing': ing
        }
        pizzas.append(pizza)
    return pizzas

def encontrar(pizzas,x):
    preço = float('-inf')
    maiscara = None
    for i in range(len(pizzas)):
        for j in range(len(pizzas[i]['ing'])):
            if pizzas[i]['ing'][j] == x:
                if pizzas[i]['preço'] > preço:
                    preço = pizzas[i]['preço']
                    maiscara = pizzas[i]['nome']
    if maiscara:
        print(f'mais cara com é {maiscara}')
    else:
        print('não tem')

n = int(input('n: '))
pizzas = pedidos(n)
x = input('qual? ')
encontrar(pizzas,x)