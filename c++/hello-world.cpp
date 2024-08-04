#include <iostream>
using namespace std;

class HelloWorld {
    private:
        string mensagem;
    public:
        HelloWorld(string texto) {
            mensagem = texto;
        }

        void imprimirMensagem() {
            cout<< mensagem <<endl;
        }
};

int main() {
    HelloWorld helloWorld("Hello, World!");
    helloWorld.imprimirMensagem();
    return 0;
}
