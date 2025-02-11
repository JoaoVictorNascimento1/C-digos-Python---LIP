#Deleta os elementos que a tem iguais a b

a = input().split(' ')
b = input().split(' ')

i = 0
while i < len(a):
    j = 0
    while j < len(b):
        if a[i] == b[j]:
            del a[i]
            i -= 1
            break
        j+=1
    i+=1
print(a)