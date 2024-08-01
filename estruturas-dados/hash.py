def sondagem_linear(tamanho_tabela, tabela_hash, chave):
	novo_indice = (chave + 1) % tamanho_tabela
	
	while tabela_hash[novo_indice] is not None:
		novo_indice = (novo_indice + 1) % tamanho_tabela

	tabela_hash[novo_indice] = chave

def metodo_divisao(tamanho_tabela, tabela_hash, chave):
	indice = chave % tamanho_tabela
	
	if tabela_hash[indice] is not None:
		sondagem_linear(tamanho_tabela, tabela_hash, chave)
	else:
		tabela_hash[indice] = chave