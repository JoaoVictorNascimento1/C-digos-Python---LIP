#Encontra o par de elementos cuja subtraçao é a maior possível

def subtrair(lista):
    maior = float('-inf')
    a = 0
    b = 0
    for i in range(len(lista)):
        j = i+1
        while j<len(lista):
            if (lista[i]-lista[j])>maior:
                maior = lista[i]-lista[j]
                a = lista[i]
                b = lista[j]
            j+=1
    print(f'{a} e {b} = {maior}')

n = int(input())
lista = []

while n!=0:
    lista.append(n)
    n = int(input())

subtrair(lista)
