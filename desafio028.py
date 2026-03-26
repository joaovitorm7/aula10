##Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep

print("Vou pensar em um número entre 0 e 5. Você deve tentar adivinhar que número pensei.")
numero = randint(0, 5) ## Faz o computador pensar em um número inteiro entre 0 e 5
palpite = int(input("Qual é o seu palpite? "))
print("Processando...")
sleep(2) ## Faz o programa esperar 2 segundos para criar um efeito de suspense
if palpite == numero:
    print("Parabéns! Você acertou!")
else:
    print("Que pena! Você errou. O número que eu pensei foi {}.".format(numero))