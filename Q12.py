#Faz a soma de números ímpares até um número informado

n = int(input())
imp = []
i = 1
while i <= n:
    imp.append(i)
    i +=2

v1 = int(input())
v2 = int(input())
j = v1
soma = 0

while j <= v2:
    soma = soma + imp[j]
    j+=1

print(soma)