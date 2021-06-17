# Importando biblioteca para limpar o terminal a cada pergunta e para dar tempo para as respostas do terminal.
from os import system
from time import sleep
system('cls')
print("Carregando Cenário.....")
sleep(3) # Inclui tempo de espera para exibir resultado no terminal
system('cls') # Limpa o terminal

nome = input("Por favor, digite seu nome abaixo para iniciar o jogo: \n")
system('cls')
sleep(1) 

print(f'{nome}, Hoje é segunda feira, 7 horas da manhã, e a Polícia federal acaba de bater na sua porta para fazer algumas perguntas a respeito da morte de sua cunhada que aconteceu no seu quintal no último final de semana....')
sleep(10)
system('cls')

print(f'{nome}, as perguntas serão de resposta afirmativa (sim) ou negativa (não).')
sleep(5)
system('cls')

print('A policia federal conta com sua colaboração e sinceridade para o andamento dessa investigação...')
sleep(5)
system('cls')

print('''A partir daqui, você concorda em ser dizer a verdade e somente a verdade sob pena do artigo 342 do Código Penal de multa ou até retenção...   ''')
sleep(8)
system('cls')

# Entrada das respostas as perguntas // Transforma todas strings de entrada em minúsculo; 
pergunta1 = input(f'{nome}, não é verdade que você telefonou para a vítima nesse último final de semana? [S/N]\n').lower()
system('cls')

pergunta2 = input(f'Você esteve no local do crime em algum momento desse final de semana? [S/N]\n').lower()
system('cls')

pergunta3 = input(f'{nome}, você mora perto da vítima? [S/N]\n').lower()
system('cls')

pergunta4 = input(f'{nome}, Não é verdade que você devia algum valor para vítima? [S/N]\n').lower()
system('cls')

pergunta5 = input(f'Em algum momento você trabalhou com a vítima? [S/N]\n').lower()
system('cls')

print(f'''Obrigado {nome}, Sem mais perguntas.''')
sleep(5)
system('cls')

# Declaração do contador de respostas "S"
contador = 0 
# Reduz as entradas em somente a primeira letra; 
primeiraLetra1 = pergunta1[0]
primeiraLetra2 = pergunta2[0]
primeiraLetra3 = pergunta3[0]
primeiraLetra4 = pergunta4[0]
primeiraLetra5 = pergunta5[0]

# Cada IF confirma a entrada e soma ao contador a resposta como válida.
if primeiraLetra1 == 's' : 
    contador += 1 

if primeiraLetra2 == 's' : 
    contador += 1

if primeiraLetra3 == 's' : 
    contador += 1 

if primeiraLetra4 == 's' : 
    contador += 1

if primeiraLetra5 == 's' : 
    contador += 1 

# If contador compara o número de respostas e imprime o resultado na tela. 
print(f'''Mais tarde na delegacia...''')
sleep(3)
system('cls')

if contador == 2 :
    print(f"Sr delegado, a partir das respostas, identificamos o {nome} como um SUSPEITO.")

if contador == 3 or contador == 4 :
    print(f"Sr delegado, a partir das respostas, identificamos o {nome} como um dos CUMPLICES.")
if contador == 5 :
    print(f"Sr delegado, a partir das respostas, identificamos o {nome} como o ASSASSINO da própria cunhada. ")
elif contador == 0 or contador == 1:
    print(f"Sr delegado, a partir das respostas, identificamos o {nome} como INOCENTE, e o liberamos.")
