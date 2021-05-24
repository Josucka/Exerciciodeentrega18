#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
# As perguntas são:
   # "Telefonou para a vítima?"
   # "Esteve no local do crime?"
   # "Mora perto da vítima?"
   # "Devia para a vítima?"
   # "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
   # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
   # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
   # Caso contrário, ele será classificado como "Inocente".

#Resposta
count = 0
resp = str(input('Telefonou para a vítima? ').lower())
if resp == 'sim' or resp == 's':
   count = count + 1 
resp = str(input('Esteve no local do crime? ').lower()) 
if resp == 'sim' or resp == 's':
   count = count + 1 
resp = str(input('Mora perto da vítima? ').lower()) 
if resp == 'sim' or resp == 's':
   count = count + 1 
resp = str(input('Devia para a vítima? ').lower()) 
if resp == 'sim' or resp == 's':
   count = count + 1 
resp = str(input('Já trabalhou com a vítima? ').lower()) 
if resp == 'sim' or resp == 's':
   count = count + 1 
if count == 2:
   print('Suspeita')
if count == 3 or count == 4:
   print('Cúmplice')
if count == 5:
   print('Assassino')
else:
   print('Inocente')
