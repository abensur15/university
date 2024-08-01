# Importa o modulo Turtle
import turtle as tortuguita

# Importa o modulo Random
import random

# Abre a janela de desenho
tortuguita.home()

# Altera a forma do ponteiro para uma tartaruga
tortuguita.shape('turtle')

# Altera a grossura da caneta para 5 unidades
tortuguita.pensize(5)

# Altera a velocidade da tartaruga
tortuguita.speed(1)

# Altera modo de cor para notacao RGB
tortuguita.colormode(255)

# Le o numero de retangulos
num = int(input("Digite o numero de retangulos: "))

# Verifica se numero eh menor que 1
while num < 1:
    print("O numero digitado nao eh valido!")
    print("Por favor, digite um numero positivo.")
    
    # Repete leitura enquanto numero for menor que 1
    num = int(input("Digite o numero de retangulos: "))

# Desenha o numero lido de retangulos
for i in range(num):
    # Cria uma cor aleatoria
    red, green, blue = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    # Inicia o preenchimento do retangulo
    tortuguita.begin_fill()

    # Altera a cor do prenchimento
    tortuguita.fillcolor(red, green, blue)

    # Cria a forma do retangulo
    for _ in range(2):
        tortuguita.fd(300) # Move 300 passos para frente (lados maiores)
        tortuguita.right(90) # Rotaciona 90 graus para direita
        tortuguita.fd(30) # Move 30 passos para frente (lados menores)
        tortuguita.right(90) # Rotaciona 90 graus para direita

    # Finaliza o preenchimento do retangulo
    tortuguita.end_fill()

    if i < (num - 1):
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

# Mantem a janela aberta
tortuguita.mainloop()