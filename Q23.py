#Adiciona o nome das músicas e seu respectivos estilos em um dicionário e uma lista de estilos
#Encontra as músicas de mesmo estilo da lista estilos

def receber_musica(n):
    musicas = []
    for i in range (n):
        nome = input()
        estilo = input()
        musica = {'nome': nome, 'estilo': estilo}
        musicas.append(musica)
    return musicas

def receber_estilos(m):
    estilos = []
    for i in range(m):
        estilo = input()
        estilos.append(estilo)
    return estilos

def encontrar(musicas,estilos):
    nomes = []
    for i in range(len(musicas)):
        for j in range (len(estilos)):
            if musicas[i]['estilo']==estilos[j]:
                nomes.append(musicas[i]['nome'])
                break
    return nomes

n =int(input('n: ' ))
musicas = receber_musica(n)

m = int(input('m: '))
estilos = receber_estilos(m)

nomes = encontrar(musicas,estilos)

for i in range(len(nomes)):
    print(nomes[i])
