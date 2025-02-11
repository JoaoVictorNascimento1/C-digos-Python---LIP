#Funções para encontrar média, mediana e moda de uma lista

def media(lista):
    
    soma = 0
    for i in range (len(lista)):
        soma = soma + lista[i]
        media = soma/(len(lista))
    
    return media

def mediana(lista):
    
    if len(lista)%2 != 0:
        central = (n//2)
        mediana = lista[central]
        return mediana
    else:
        c1 = (len(lista))//2
        c2 = (len(lista)//2)-1
        mediana = (lista[c1]+lista[c2])/2
    
    return mediana

def moda(lista):
    moda = lista[0]
    quant = 0
    cont = 0
    for i in range (len(lista)):
        for j in range (len(lista)):
            if lista[i] == lista[j]:
                cont += 1
        if cont > quant:
            quant = cont
            moda = lista[i]
        cont = 0
    return moda


n = int(input())
lista = []
for i in range (n):
 lista.append(int(input()))
print(f'(media, moda, mediana) = ({media(lista):.2f}, {moda(lista)}, {mediana(lista):.2f})')