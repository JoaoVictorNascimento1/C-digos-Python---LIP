#Verifica se o menor elemento de A é maior que o maior elemento de B

def V_F(a,b):
 menora = float('inf')
 maiorb = float('-inf')
 for i in range(len(a)):
    if a[i] < menora:
        menora = a[i]

 for i in range(len(b)):
    if b[i] > maiorb:
        maiorb = b[i]

 return menora, maiorb

a = []
b = []

na = int(input())
for i in range (na):
    a.append(float(input()))

nb = int(input())
for i in range (nb):
    b.append(float(input()))

menora, maiorb = V_F(a,b)

if menora > maiorb:
    print('Saída "True"')
else:
    print('Saída "False"')