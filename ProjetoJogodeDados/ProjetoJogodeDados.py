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

# Pergunta quantas rodadas, e cria o dicionário 
rodadas = int(input('Quantas rodadas você quer jogar?\n')) 
resultados = dict()
os.system('cls')

# Laço de repetição para quantidade de rodadas
for c in range(rodadas) :
    for j in range(4) :

     # Cria chave do dicionário que é o input do NOME DO JOGADOR // Cria o Valor de cada chave sorteando o um número aleatório de 1 a 6 ( 6 lados do Dado)
        resultados[input(f'Digite seu nome, jogador {j+1}:\n')] = rd.randint(1, 7)  
        os.system('cls')
        tm.sleep(0.5)

# Ordena o dicionario, e printa as chaves e os valores de cada chave
for i in sorted(resultados, reverse=True):   
    print(resultados[i])
    tm.sleep(3)





# Versão 2 


# rodadas = int(input('Digite quantas rodadas você quer jogar:\n'))

# resultados = {
#     input('Digite seu nome, jogador:\n') : rd.randint(1, 7),
#     input('Digite seu nome, jogador:\n') : rd.randint(1, 7),
#     input('Digite seu nome, jogador:\n') : rd.randint(1, 7),
#     input('Digite seu nome, jogador:\n') : rd.randint(1, 7),
# }
# for c in range(rodadas) :
