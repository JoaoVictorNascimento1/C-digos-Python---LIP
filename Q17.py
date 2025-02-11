#Função para contar elementos iguais em uma lista

def contar_elementos(lista):
    
    cont = []
    i = 0
    
    while i < len(lista):
        contatual = 1
        j = i+1
        while j < len(lista):
            if lista[i] == lista[j]:
                contatual += 1
                del lista[j]
                j -= 1
            j += 1
        cont.append(contatual)
        i += 1

    return cont


lista = input().split(' ')
contagens = contar_elementos(lista)
for i in range(len(lista)):
    print(f"{lista[i]} = {contagens[i]}")