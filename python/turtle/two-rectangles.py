# Importa o modulo Turtle
import turtle as tortuguita

# Abre a janela de desenho
tortuguita.home()

# Altera a forma do ponteiro para uma tartaruga
tortuguita.shape('turtle')

# Altera a grossura da caneta para 5 unidades
tortuguita.pensize(5)

# Altera a velocidade da tartaruga
tortuguita.speed(1)

# Altera a cor do prenchimento para verde
tortuguita.fillcolor('#008000')

# Desenha dois retangulos
for i in range(2):
    # Inicia o preenchimento do triangulo
    tortuguita.begin_fill()

    # Cria a forma do retangulo
    for _ in range(2):
        tortuguita.fd(300) # Move 300 passos para frente (lados maiores)
        tortuguita.right(90) # Rotaciona 90 graus para direita
        tortuguita.fd(30) # Move 30 passos para frente (lados menores)
        tortuguita.right(90) # Rotaciona 90 graus para direita

    # Finaliza o preenchimento do retangulo
    tortuguita.end_fill()

    if i < 1: 
        # Retira a caneta do papel
        tortuguita.pu()

        # Rotaciona 90 graus para esquerda
        tortuguita.left(90)

        # Move 60 passos para frente
        tortuguita.fd(60)

        # Coloca a caneta no papel de novo
        tortuguita.pd()

        # Rotaciona 90 graus para direita
        tortuguita.right(90)

        # Altera a cor do preenchimento para azul
        tortuguita.fillcolor('#000080')

# Mantem a janela aberta
tortuguita.mainloop()
