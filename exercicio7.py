#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados 
# os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

#Resposta

numeros = [[], []]

for i in range(0,7):
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

print(f"Os números digitados são: {numeros} pares: {numeros[0]} impares: {numeros[1]} ")

