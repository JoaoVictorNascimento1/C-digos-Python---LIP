#Uso de funções em listas para somar os numeros pares até um numero fornecido

def listar_pares(n):
    for i in range (n+1):
        if i%2 == 0:
            lista.append(i)

    return lista

def somar_pares(lista):
    soma = 0
    for i in range (len(lista)):
        soma = soma + lista[i]
    return soma


lista = []
n = int(input())
print(somar_pares(listar_pares(n)))