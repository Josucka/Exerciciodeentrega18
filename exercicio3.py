#03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar seu processamento, 
# só deixe o usuário continuar se a senha estiver correta, após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação, 
# onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, 
# a cada palpite do usuário diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou, 
# no final mostre quantos palpites foram necessários para vencer.

#resposta
from random import randint
terminar = 'N'
def computador():     
   return computador
while True:
   senha = int(input('Digite uma senha: '))
   loguin = int(input('Qual o loguin: '))
   if senha == loguin:
      print('Bem vindo ao programa')
   else:
      senha != loguin
      print(f'tente novamente: ')
      loguin = int(input('Qual o loguin: '))
   tent = 0
   sorteado = randint(0, 10)
   while True:
      tent += 1
      numero = int(input('Acerte o numero que o programa gerou: 0 A 10 '))
      if numero < sorteado:
         print('o numero digitado é menor que o sorteado')
      elif numero > sorteado:
         print('o numero digitado é maio que o sorteado')
      elif numero == sorteado:
         print('Parabens voce acertou o numero: ')
         print('fim do jogo')
         print(f'Voce prescisou de: {tent} tentativas')
         break
