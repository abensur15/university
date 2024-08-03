def min_heapify(quase_heap, raiz, tamanho):
	menor = raiz
	
	esquerdo = (2 * raiz) + 1
	if (esquerdo < tamanho) and (quase_heap[esquerdo] < quase_heap[menor]):
		menor = esquerdo
	
	direito = (2 * raiz) + 2
	if (direito < tamanho) and (quase_heap[direito] < quase_heap[menor]):
		menor = direito
	
	if menor != raiz:
		temp = quase_heap[raiz]
		quase_heap[raiz] = quase_heap[menor]
		quase_heap[menor] = temp
		
		min_heapify(quase_heap, menor, tamanho)

def montar_min_heap(tamanho, lista):
	ultimo = (tamanho // 2) - 1
	
	for i in range(ultimo, -1, -1):
		min_heapify(lista, i, tamanho)
		
def aumentar_chave(heap, pos, novo):
	tam_heap = len(heap)
	
	if pos == tam_heap:
		heap.append(novo)
		tam_heap += 1
	else:
		heap[pos] = novo
	
	montar_min_heap(tam_heap, heap)

def inserir_heap(heap, chave):
	heap.append(chave)
	montar_min_heap(len(heap), heap)

def remover_heap(heap):
	if heap != []:
		removido = heap.pop(0)
		print(removido.valor)
		montar_min_heap(len(heap), heap)

def heap_sort(heap):
	tam_heap = len(heap)
	montar_min_heap(tam_heap, heap)
	
	for i in range(tam_heap - 1, 0, -1):
		heap[0], heap[i] = heap[i], heap[0]
		min_heapify(i, heap, 0)
