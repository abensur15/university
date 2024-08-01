# Importa o modulo Turtle
import turtle as tortuguita

# Abre a janela de desenho
tortuguita.home()

# Modifica a forma do ponteiro para uma tartaruga
tortuguita.shape('turtle')

# Altera a grossura da caneta para 5 unidades
tortuguita.pensize(5)

# Altera a velocidade da tartaruga
tortuguita.speed(1)

# Altera a cor do preenchimento para azul
tortuguita.fillcolor('#000080')

# Inicia o preenchimento do triangulo
tortuguita.begin_fill()

# Desenha o triangulo
for _ in range(2):
    tortuguita.forward(120) # Move 120 passos para frente
    tortuguita.left(120) # Rotaciona 120 graus para esquerda

# Finaliza o preenchimento do triangulo
tortuguita.end_fill()

# Mantem a janela aberta
tortuguita.mainloop()
