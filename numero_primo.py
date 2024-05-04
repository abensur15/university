# Funcao para verificar se algum numero eh primo
def primo(num):
	# * Assume-se que 1 seja composto
	if num == 1:
		return False
	else:
		cont = 2
		while cont < num:
			# * Se o numero for divisivel por algum valor desse intervalo, ele nao eh primo 
			if (num % cont) == 0:
				return False

			# * Caso contrario, incrementa-se o contador
			cont += 1
	
	return True

# Programa principal
# * Entrada limitada para apenas numeros positivos, incluindo 0
if num >= 0:
	numero = int(input())

#  - A entrada termina em 0 (nao eh um caso de execucao)
while num != 0:
	if primo(numero):
		print("{}: primo".format(numero))
	else:
		print("{}: composto".format(numero))
		
	numero = int(input())
