# Utilizando os conceitos aprendidos até dicionários, crie um programa onde 4
# jogadores joguem um dado e tenham resultados aleatórios.
# O programa tem que:
# • Perguntar quantas rodadas você quer fazer;
# • Guardar os resultados dos dados em um dicionário.
# • Ordenar esse dicionário, sabendo que o vencedor tirou o maior número
# no dado.
# • Mostrar no final qual jogador ganhou mais rodadas e foi o grande
# campeão.


# # Início do Código

import os # Biblioteca para limpar o terminal
import random as rd # biblioteca para criar aleatoriedade e cria um atalho pra chamar ela (as 'rd')
import time as tm # biblioteca para criar deley 
from operator import itemgetter  # biblioteca para ordenar lista de dicionários


    # Pergunta quantas rodadas o jogador quer jogar, e declara as listas e o dicionário e o contador
rodadas = int(input('Olá, Quantas rodadas você quer jogar?\n')) 
resultados = dict()
listaOrdena = list()


    # Permite que o usuário digite seu nome de jogador
jogador1 = input(f'🎮 Digite seu nome, jogador 1: 🎮\n')
jogador2 = input(f'🎮 Digite seu nome, jogador 2: 🎮\n')
jogador3 = input(f'🎮 Digite seu nome, jogador 3: 🎮\n')
jogador4 = input(f'🎮 Digite seu nome, jogador 4: 🎮\n')
os.system('cls')


    # Laço de repetição para quantidade de rodadas
for c in range(0, rodadas) :
    
    print(f'''
        🎲  {c+1} rodada !  🎲
    ''')

        # Cria o dicionário e adiciona valores aleatórios da biblioteca "random"
    resultados = {
    jogador1 : rd.randint(1, 6),
    jogador2 : rd.randint(1, 6),
    jogador3 : rd.randint(1, 6),
    jogador4 : rd.randint(1, 6)
}
        # Ordena por ordem decrescente os valores das chaves do dicionário, e inclui o maior valor em uma lista. 
    vencedor = sorted(resultados.items(), key=itemgetter(1), reverse=True)
    listaOrdena.append(vencedor[0])

        # imprime os resultados do dicionário em ordem.
    for t in sorted(resultados, reverse=True):   
        print(f'''
           {t} Tirou {resultados[t]} !''')
        tm.sleep(1)
    os.system('cls')

    # Reinverte a ordem da lista e imprime os vencedores de cada rodada. 
reversed(listaOrdena)
for i, v in enumerate(listaOrdena) :
    print(f''' 
        A {i+1}º rodada foi do(a) {v[0]} com resultado: {v[1]}''')

