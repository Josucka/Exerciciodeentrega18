#08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente ,
#  além da idade, com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

dados = dict()
nome = list()
ano_nasc = list()
salario = list()
dados['nome'] = str(input('Digite o nome: '))
dados['ano_nasc'] = int(input('Digiti ano de nascimento do trabalhador: '))
dados['cpts'] = int(input('Digite o numero da Carteira de trabalho: '))
if dados.get('cpts', 0) != 0:
   dados['ano_cont'] = int(input('Digite o ano de contrataçao: '))
   dados['salario'] = float(input('Digite o valor do salario: '))
   dados['ano_apo'] = dados.get('ano_cont') + 35
print(dados)
