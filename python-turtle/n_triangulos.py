# Importa o modulo tortuguita
import turtle as tortuguita

# Abre a janela de desenho
tortuguita.home()

# Altera a forma do ponteiro para uma tartaruga
tortuguita.shape('turtle')

# Altera a grossura da caneta para 5 unidades
tortuguita.pensize(5)

# Altera a velocidade da tartaruga
tortuguita.speed(1)

# Le o numero de triangulos
num = int(input("Digite o numero de triangulos: "))

# Verifica se numero eh menor que 1
while num < 1:
    print("O numero digitado nao eh valido!")
    print("Por favor, digite um numero positivo.")
    
    # Repete leitura enquanto numero for negativo
    num = int(input("Digite o numero de triangulos: "))

largura_imagem = 1500

segmento = largura_imagem / (num + 1)

lado = segmento / 2

tortuguita.pu()

# Posiciona a tartaruga no início da linha
tortuguita.setpos(-largura_imagem / 2, 0)

tortuguita.pd()

for i in range(num):
    if i == 0:
        tortuguita.fd(segmento - (lado / 2))
    
    # Desenha dois lados de um triangulo
    tortuguita.left(60)
    tortuguita.fd(lado)
    tortuguita.right(120)
    tortuguita.fd(lado)
    tortuguita.left(60)

    if i == num - 1:
        tortuguita.fd(segmento - (lado / 2))
    else:
        tortuguita.fd(segmento - lado)

# Mantem a janela aberta
tortuguita.mainloop()