#02 - Utilizando estruturas de repetição com variável de controle, 
# faça um programa que receba uma string com uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u 
# e mostre na tela, depois mostre na tela essa mesma frase sem nenhuma vogal.
#resposta

frase = str(input('Digite uma frase: ')).upper()
a = e = i = o = u = 0
for c in frase:
   if c == 'A':
      a += 1
   if c == 'E':
      e += 1
   if c == 'I':
      i += 1
   if c == 'O':
      o += 1
   if c == 'U':
      u += 1
   for h in 'AEIOU':
      frase = frase.replace(h, '')
print(f'vogal A: {a}\nvogal E: {e}\nvogal I: {i}\nvogal O: {o}\nvogal U: {u}')   
print(f'a frase em vogal fica assim: {frase}')
