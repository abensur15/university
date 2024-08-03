package main

import "net/http"

func paginaEstatica(resposta http.ResponseWriter, requisicao *http.Request) {
	http.ServeFile(resposta, requisicao, "./index.html")
}

func main() {
	http.HandleFunc("/", paginaEstatica)
	http.ListenAndServe(":8080", nil)
}
