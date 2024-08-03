package main

import "net/http"

func paginaEstatica(resposta http.ResponseWriter, requisicao *http.Request) {
	http.ServeFile(resposta, requisicao, "./pagina_estatica.html")
}

func main() {
	http.HandleFunc("/", paginaEstatica)
	http.ListenAndServe(":8080", nil)
}
