"""Função para verificar se algum numero é primo"""
def primo(num):
	# Assume-se que 1 seja composto
	if num == 1:
		return False
	else:
		cont = 3
		while cont < num:
			# Se o numero for divisível por algum valor desse intervalo, ele não é primo
			if (num % cont) == 0:
				return False

			# Caso contrário, incrementa-se o contador
			cont += 1
	
	return True

def main():
	num = int(input())
	
	# Entrada limitada para apenas números positivos
	while num > 0:
		if primo(num):
			print("{}: primo".format(num))
		else:
			print("{}: composto".format(num))
	    
		num = int(input())

if __name__ == "__main__":
	main()