package main

import (
	"fmt"
	"sync"
)

// Funcao que simula um produtor
func produtor(canal chan int, num int, filaProdutor *sync.WaitGroup) {
	// Loop para produzir 10 produtos
	for i := 1; i <= 10; i++ {
		fmt.Printf("Produtor %d esta produzindo %d produto(s)\n", num, i)

		// Envia o numero do produto para o canal
		canal <- i
	}

	// Indica que o produtor terminou
	filaProdutor.Done()
}

// Funcao que simula um consumidor
func consumidor(canal chan int, num int, filaConsumidor *sync.WaitGroup) {
	// Loop para consumir produtos do canal
	for j := range canal {
		fmt.Printf("Consumidor %d esta consumindo %d produto(s)\n", num, j)
	}

	// Indica que o consumidor terminou
	filaConsumidor.Done()
}

func main() {
	// Canal para comunicacao entre produtor e consumidores
	var canal = make(chan int)

	// WaitGroups para esperar todas as goroutines
	var filaProdutor sync.WaitGroup
	var filaConsumidor sync.WaitGroup

	// Adiciona os WaitGroups para produtores e consumidores
	filaProdutor.Add(3)
	filaConsumidor.Add(6)

	// Inicia 3 goroutines de produtores
	for i := 1; i <= 3; i++ {
		go produtor(canal, i, &filaProdutor)
	}

	// Inicia 6 goroutines de consumidores
	for j := 1; j <= 6; j++ {
		go consumidor(canal, j, &filaConsumidor)
	}

	// Espera todos os produtores terminarem
	filaProdutor.Wait()

	// Bloqueio do canal (nenhum envio adicional eh permitido)
	close(canal)

	// Espera todos os consumidores terminarem
	filaConsumidor.Wait()

	// Encerra a execucao
	fmt.Println("Execucao finalizada")
}
