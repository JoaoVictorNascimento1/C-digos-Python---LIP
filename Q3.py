#Verificar se em algum dia o numero de nascimentos foi maior que a soma deles. Não conta o dia 0.

n = int(input())
lista = []

s = 0
b = False

for i in range(n):
    lista.append(int(input()))

    if lista[i]>s and i!=0:
        b = True
        print(f'dia {i}')
        break
    s=s+lista[i]

if b == False:
    print('não há')