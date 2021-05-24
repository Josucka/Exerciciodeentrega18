#04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA 
# e devolva uma string no formato DD de mesPorExtenso de AAAA. 
# Opcional: valide a data e retorne 'data inválida' caso a data seja inválida.

#resposta // O exercicio pede que crie uma lista mais eu nao consegui concluir o exercicio retornando o valor exato do mes que se pede

from datetime import datetime
dias = int(input("Digite o dia: "))
mes = int(input("Digite o mes: "))
ano = int(input("Digite o ano: "))
di = dias
me = [[1,'janeiro'],[2,'feverreiro'],[3,'março'],[4,'abril'],[5,'maio'],[6,'junho'],[7,'julho'],[8,'agosto'],[9,'setembro'],[10,'outubro'],[11,'novenbro'],[12,'dezembro']]
an = ano
if dias > 0 and dias <= 31:
   dias = True
else:
   dias = False
if mes > 0 and mes <= 12:
   mes = True
else:
   mes = False
if ano >= 0 and ano <= 9999:
   ano = True
else: 
   ano = False
if dias == True and mes == True and ano == True:
   print(f'Data valida!: {di, me[:], an}') #Com o formato %d / %B / %Y que o python tem pra gerar o mes ja por extenso nao esta rodando na minha maquina e pra criar uma lista com todos os nomes de mes e pedindo o numero do mes retornando ele por extenso nao consigo elaborar
else:
   print("Data invalida!")
