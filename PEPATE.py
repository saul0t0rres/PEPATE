print ('\n====== PEDRA, PAPEL OU TESOURA ======\n')
import random
print('''Estas são as suas opções abaixo:
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
jogador = int(input('Insira o número da sua jogada: '))
computador = random.randint(1, 3)
lista = ('Pedra', 'Papel', 'Tesoura')
print('-=' * 16)
print(f'Sua jogada: {lista[(jogador) - 1]}')
print(f'Jogada da IA: {lista[(computador) - 1]}')
print('-=' * 16)
if computador == jogador:
    print('Nós empatamos! :/')
elif (jogador == 1 and computador == 2) or (jogador == 2 and computador == 3) or (jogador == 3 and computador == 1):
    print('Eu ganhei e você perdeu! "hahaha" (Risos Robotizados) :D')
else:
    print('Você ganhou! (Pra um ser baseado em caborno, até que você é esperto(a). ;)')