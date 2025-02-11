#Encontra o par de elementos cuja subtraçao é a maior possível

a=[]
digito = int(input())

while digito != 0:
    a.append(digito)
    digito = int(input())

a.append(0)
sub = 0
maiorsub = 0
n1 = 0
n2=0

for i in range (len(a)-1):
    sub = a[i] - a[i+1]
    if sub > maiorsub:
        maiorsub = sub
        n1 = a[i]
        n2 = a[i+1]

print(f'{n1} e {n2}, cuja subtração em módulo é {maiorsub}.')