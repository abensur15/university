"""Funcao para verificar se algum numero eh primo"""
def primo(num):
	# Assume-se que 1 seja composto
	if num == 1:
		return False
	else:
		cont = 2
		while cont < num:
			# Se o numero for divisível por algum valor desse intervalo
			# ele nao é primo
			if (num % cont) == 0:
				return False

			# Caso contrário, incrementa-se o contador
			cont += 1
	
	return True

def main():
	num = int(input())
	
	# Entrada limitada para apenas numeros positivos, incluindo 0
	# Entrada termina em 0 (nao eh um caso de execucao)
	while num > 0:
		if primo(num):
			print("{}: primo".format(num))
		else:
			print("{}: composto".format(num))
	    
		num = int(input())

if __name__ == "__main__":
	main()