#05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário e retorne o resultado.
#  Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.

#Resposta  #imagido que esteja errado pq nao dei conta de estruturar esse codigo

def frase(string):
   vogal = 'aeiou'
   cont = 0
   
   for l in string:
      if l in vogal:
         'cont' += 1
      else:
         print(f'vogais retiradas {cont}')
   for l in vogal:
      if l == 'aeiou':
         cont += 1
         print(f'quantidade de vogal retirada {cont}')
   
refatore = str(input('Digite uma frase: '))

frase(refatore)
