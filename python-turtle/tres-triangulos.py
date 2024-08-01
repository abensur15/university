# Importa o modulo Turtle
import turtle as tortuguita

def criar_triangulo(vertice_alfa, vertice_beta, vertice_gama, cor):
    """Funcao para criar um triangulo usando as coordenadas de seus vertices como parametros"""

    # Retira a caneta do papel
    tortuguita.pu()

    # Posiciona a tartaruga no vertice alfa
    tortuguita.goto(vertice_alfa)

    # Inicia o preenchimento do triangulo
    tortuguita.begin_fill()

    # Altera a cor da tartaruga
    tortuguita.fillcolor(cor)

    # Recoloca a caneta no papel
    tortuguita.pd()

    # Posiciona a tartaruga no vertice beta
    tortuguita.goto(vertice_beta)

    # Posiciona a tartaruga no vertice beta
    tortuguita.goto(vertice_gama)

    # Reposiciona a tartaruga no vertice alfa
    tortuguita.goto(vertice_alfa)

    # Finaliza o preenchimento do triangulo
    tortuguita.end_fill()

# Abre a janela de desenho
tortuguita.home()

# Modifica a forma do ponteiro para uma tartaruga
tortuguita.shape('turtle')

# Altera a velocidade da tartaruga
tortuguita.speed(1)

# Trinagulo vermelho
criar_triangulo((-300, 300), (-150, 300), (-225, 180), 'red')

# Triangulo verde
criar_triangulo((-120, 300), (-45, 180), (-195, 180), 'lime')

# Triangulo azul
criar_triangulo((-90, 300), (60, 300), (-15, 180), 'blue')

# Mantem a janela aberta
tortuguita.mainloop()
