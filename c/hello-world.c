#include <stdio.h>

typedef struct helloWorld HelloWorld;
void imprimirMensagem(HelloWorld helloWorld);

struct helloWorld {
    char* texto;
};

void imprimirMensagem(HelloWorld helloWorld) {
    printf("%s\n", helloWorld.texto);
}

int main(){
    HelloWorld helloWorld;
    helloWorld.texto = "Hello, World!";
    imprimirMensagem(helloWorld);
    return 0;
}
