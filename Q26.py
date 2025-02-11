#Adiciona partidas com times e seus resultados e informa a pontuação de um time requisitado

def pontuacao(partidas, time):
    pontuacao = 0
    for partida in partidas:
        mandante = partida['mandante']
        visitante = partida['visitante']
        gols_mandante = partida['gols_mandante']
        gols_visitante = partida['gols_visitante']

        if gols_mandante > gols_visitante:
            if mandante == time:
                pontuacao +=3
        elif gols_mandante < gols_visitante:
            if visitante == time:
                pontuacao += 3
        else:
            if mandante == time or visitante == time:
                pontuacao += 1

    return pontuacao

partidas = []
n = int(input())

for i in range (n):
    entrada = input()
    dados = entrada.split()
    mandante = dados[0]
    visitante = dados[3]
    gols_mandante = int(dados[1])
    gols_visitante = int(dados[2])

    partida = {'mandante': mandante,
    'visitante': visitante,
    'gols_mandante': gols_mandante,
    'gols_visitante': gols_visitante
    }
    partidas.append(partida)

time = input()
r = pontuacao(partidas, time)
print(f'{time} tem {r} pontos')