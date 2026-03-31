## Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
from time import sleep

numero = int(input("Digite um número, que direi ser é PAR ou ÍMPAR: "))

print("Analisando...")
sleep(2)

if numero % 2 == 0:
    print('O número {} é PAR!' .format(numero))
else:
    print('O número {} é ÍMPAR!' .format(numero))