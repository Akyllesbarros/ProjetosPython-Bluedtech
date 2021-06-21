import random
import os
import time

replay = 0 # VARIÁVEL PARA ENCERRAR OU RODAR O JOGO NOVAMENTE! 
os.system('cls')
nome = input('Olá, Sou o Jaime 🤖 , vamos jogar um pouco de joKenPo ?? Para iniciar, me diga seu nome:\n')
os.system('cls')

# LAÇO QUE INICIA, TERMINA E CONTINUA O JOGO

while True : 
    rodadas = int(input('Quantas rodadas vamos jogar?  '))
    venceuPC = 0 # VARIÁVEL QUE INDICA QUANTAS VEZES O PC GANHOU
    venceuHumano = 0 #VARIÁVEL QUE INDICA QUANTAS VEZES O HUMANO GANHOU 
    os.system('cls')
    time.sleep(1)

    for c in range(rodadas) : # INICIA LACO QUE INDICA AS RODADAS DO JOGO
        escolhaHumana = int(input('''Você escolhe Pedra, Papel ou Tesoura?
        [ 1 ] Pedra 🤜
        [ 2 ] Papel 🧾
        [ 3 ] Tesoura ✂
        \n\n'''))
        os.system('cls')
        time.sleep(0.5)

        if escolhaHumana == 1 :
            print('- Você escolheu PEDRA 🤜')
        if escolhaHumana == 2 :
            print('- Você escolheu PAPEL 🧾')
        if escolhaHumana == 3 :
            print('- Você escolheu TESOURA ✂')

        # DEFINE A ESCOLHA DO PC ALEATORIAMENTE E MOSTRA EM FORMATO DE TEXTO PARA O USUÁRIO

        time.sleep(0.5)
        escolhaPC = random.randint(1, 3)
        if escolhaPC == 1 :
            print('🤖 Eu escolho PEDRA 🤜\n')
        if escolhaPC == 2 :
            print('🤖 Eu escolho PAPEL 🧾\n')
        if escolhaPC == 3 :
            print('🤖 Eu escolho TESOURA ✂\n')

        # CONDIÇOES DE VITÓRIA OU DERROTA 

        print('Jo...')
        time.sleep(1)
        print('..Ken..')
        time.sleep(1)
        print('Po.\n')
        if (escolhaPC) == 1 and (escolhaHumana == 2) : # HUMANO GANHA
            print(f'{nome}, você venceu essa!\n')
            venceuHumano += 1
            time.sleep(2)
        if (escolhaPC == 1) and (escolhaHumana == 3) : # PC GANHA
            print(f'Eu Venci hehe! 🌟 \n')
            venceuPC += 1
            time.sleep(2)
        if (escolhaHumana == 1) and (escolhaPC == 2) : # PC GANHA
            print(f'Eu Venci haha! 🌟 \n')
            venceuPC += 1
            time.sleep(2)
        if (escolhaHumana == 1) and (escolhaPC == 3) : # HUMANO GANHA
            print(f'{nome}, Você venceu essa! 🌟 \n')
            venceuHumano += 1
            time.sleep(2)
        if (escolhaHumana == 3) and (escolhaPC == 2) : # HUMANDO GANHA
            print(f'{nome}, Você venceu essa! 🌟 \n')
            venceuHumano += 1
            time.sleep(2)
        if (escolhaHumana == 2) and (escolhaPC == 3) : # PC GANHA
            print('Agora eu venci!! 🌟 \n')
            venceuHumano += 1
            time.sleep(2)
        if escolhaPC == escolhaHumana : # EMPATE
            print('Empatamos!! \n')  
            time.sleep(2)   

    # CALCULA O VENCEDOR DA RODADA 
    os.system('cls')
    print('Calculando vencedor da rodada...')
    time.sleep(3)
    if venceuPC > venceuHumano :
        print(f''' 
        
        🤖 {venceuPC} x {venceuHumano} 🤡

        ''')
        print(f'✨🤖 Haha, Eu te venci, com {venceuPC} a {venceuHumano}, mais sorte da próxima vez!\n🤖 Na verdade já quero jogar de novo!\n🤖 Vamos mais uma???')
    if venceuHumano > venceuPC :
        print(f'''
        
         🤖 {venceuPC} x {venceuHumano} 👨

        ''')
        print(f'🤖 Parabéns!!🎉🎊🎉 Você me venceu {nome}, por {venceuHumano} a {venceuPC}, aproveite seu pouco tempo vitorioso...\nVamos mais uma? ')
    if venceuHumano == venceuPC :
        print(f'''
        
         🤖 {venceuPC} x {venceuHumano} 👨

        ''')
        print('Empatamos essa, vamos de novo? ')
    
    # PERGUNTA SE O USUARIO QUER JOGAR NOVAMENTE 
    replay = int(input('Clique 1 para jogar novamente, e 0 para desistir... '))
    if replay == 0 :
        break
    if replay == 1 :
        continue



    

