def busca_binaria(arvore, chave):
	if arvore is None:
		return False
	elif arvore['valor'] == chave:
		return True
	elif arvore['valor'] > chave:
		return busca_binaria(arvore['esq'], chave)
	else:
		return busca_binaria(arvore['dir'], chave)

def inserir_arvore(arvore, chave):
	if arvore is None:
		return {'valor': chave, 'esq': None, 'dir': None}
	else:
		if arvore['valor'] > chave:
			arvore['esq'] = inserir_arvore(arvore['esq'], chave)
		else:
			arvore['dir'] = inserir_arvore(arvore['dir'], chave)
	return arvore

def remover_arvore(arvore, chave):
	if arvore is None:
		return None
	elif arvore['valor'] > chave:
		arvore['esq'] = remover_arvore(arvore['esq'], chave)
	elif arvore['valor'] < chave:
		arvore['dir'] = remover_arvore(arvore['dir'], chave)
	else:
		if arvore['dir'] is None:
			return arvore['esq']
		elif arvore['esq'] is None:
			return arvore['dir']
		else:
			copia = antecessor_arvore(arvore['esq'])
			arvore['valor'] = copia['valor']
			arvore['esq'] = remover_arvore(arvore['esq'], copia['valor'])
			
	return arvore

def pre_ordem(arvore):
	if arvore is not None:
		print(arvore['valor'], end = ' ')
		pre_ordem(arvore['esq'])
		pre_ordem(arvore['dir'])

def in_ordem(arvore):
	if arvore is not None:
		in_ordem(arvore['esq'])
		print(arvore['valor'], end = ' ')
		in_ordem(arvore['dir'])

def pos_ordem(arvore):
	if arvore is not None:
		pos_ordem(arvore['esq'])
		pos_ordem(arvore['dir'])
		print(arvore['valor'], end = ' ')
		
def antecessor_arvore(arvore):
	while arvore and arvore['dir'] is not None:
		arvore = arvore['dir']
		
	return arvore

def sucessor_arvore(arvore):
	while arvore and arvore['esq'] is not None:
		arvore = arvore['esq']
		
	return arvore
