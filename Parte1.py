import random

tentativas = 1

print("**************************")
print("*                        *")
print("* Jogo de Adivinhação    *")
print("*						*")
print("************************** \n")
print("Olá, qual é o seu nome?")
	
nome = input()

numero = random.randint(1, 101)

print("Bem", nome, "eu estou pensando em um número entre 1 e 100.")
print("Você é capaz de adivinha-lo? Você tem 3 chances para isso. \n")

while (tentativas <= 3):
	tentativa = int(input("%iª tentativa: " % tentativas))
	if (tentativa != numero):
		tentativas += 1
		if (tentativa < numero):
			print('Sua tentativa está baixa.')
		else:
			print('Sua tentativa está alta.')
	else:
		break

if (tentativa == numero):
	print('Parabéns, %s, você adivinhou meu número em %i tentativas =)' % (nome, tentativas))
else:
	print('Hehehe, o número era %i.' % (numero))
	print("Lamento, mas suas chances acabaram!")
