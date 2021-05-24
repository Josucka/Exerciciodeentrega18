#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
   # A soma deles;
   # A multiplicação entre eles;
   # A divisão inteira deles;
   # Mostre na tela qual é o maior;
   # Verifique se o resultado da soma é par ou impar e mostre na tela;
   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.
#Respostas

         #primeiro o input que pergunta os numeros ao usurio
#num1 = int(input('Digite um numero aleatorio: '))
#num2 = int(input('Digite um segundo numero aleatorio: '))
         #agora presciso fazer as equaçoes necessarias podendo ser ja no printe se posivel
#print(f'A soma de {num1} + {num2} é: {num1+num2} ')
#print(f'A multiplicaçao de {num1} x {num2} é: {num1*num2} ')
#print(f'A divisão inteira de {num1} e {num2} é: {num1 // num2}')
         #pra mostras qual o valor maior presciso coloca um if
#if num1 > num2:
#   print(f'O maior entre eles é: {num1}')
#else:
#   print(f'O maior entre eles é: {num2}')
#if (num1 + num2) % 2 == 0:
#   print(f'essa soma é par: {num1} + {num2} é {num1 + num2}')
#else:
#   print(f'A soma é impar')
#if (num1 * num2) >= 40:
#      print(f'A multiplicaçao de {num1} x  {num2} é {num1*num2} e a divisao inteira é: {num1//num2} logo o resultado é {num1*num2} ')
#else:
#   print('O numero é menor que 40')
#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
   # A soma deles;
   # A multiplicação entre eles;
   # A divisão inteira deles;
   # Mostre na tela qual é o maior;
   # Verifique se o resultado da soma é par ou impar e mostre na tela;
   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.
#Respostas

         #primeiro o input que pergunta os numeros ao usurio
num1 = int(input('Digite um numero aleatorio: '))
num2 = int(input('Digite um segundo numero aleatorio: ')) #agora presciso fazer as equaçoes necessarias podendo ser ja no printe se posivel
print(f'A soma de {num1} + {num2} é: {num1+num2} ')
print(f'A multiplicaçao de {num1} x {num2} é: {num1*num2} ')
print(f'A divisão inteira de {num1} e {num2} é: {num1 // num2}')#pra mostras qual o valor maior presciso coloca um if
if num1 > num2:
   print(f'O maior entre eles é: {num1}')
else:
   print(f'O maior entre eles é: {num2}')
if (num1 + num2) % 2 == 0:
   print(f'essa soma é par: {num1} + {num2} é {num1 + num2}')
else:
   print(f'A soma é impar')
if (num1 * num2) >= 40:
      print(f'A multiplicaçao de {num1} x  {num2} é {num1*num2} e a divisao inteira é: {num1//num2} logo o resultado é {num1*num2} ')
else:
   print('O numero é menor que 40')
