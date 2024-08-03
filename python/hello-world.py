class HelloWorld:
    def __init__(self, texto):
        self.texto = texto
    
    def imprimir_texto(self):
        print(self.texto)

def main():
    hello_world = HelloWorld("Hello, World!")
    hello_world.imprimir_texto()

if __name__ == '__main__':
    main()
