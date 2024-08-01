# Importa o modulo TkInter
import tkinter as tk

# Importa o modulo Math
import math

# Funcao para criar um circulo
def criar_circulo(pontos_circ, cor):
    canvas.create_oval(
        pontos_circ,
        fill = cor,
    )

# Funcao para criar um quadrado
def criar_quadrado(pontos_quad, cor_principal, cor_borda):
    canvas.create_rectangle(
        pontos_quad,
        fill = cor_principal,
        outline = cor_borda
    )

# Funcao para criar um triangulo equilatero
def criar_triangulo(pontos_tri, cor_principal, cor_borda):
    canvas.create_polygon(
        pontos_tri,
        fill = cor_principal,
        outline = cor_borda
    )

# Cria a janela
janela = tk.Tk()

# Dimensiona a janela
janela.geometry("1920x1080")

# Le um numero
num = int(input("Digite um numero: "))

# Verifica se numero eh menor que 1
while num < 1:
    print("O numero digitado nao eh valido!")
    print("Por favor, digite um numero positivo.")
    
    # Repete leitura enquanto numero for negativo
    num = int(input("Digite um numero: "))

# Cria e dimensiona a area de desenho
canvas = tk.Canvas(janela, width = 2 * num, height = 2 * num)

# Desenha as linhas divisorias
canvas.create_line(num, 0, num, 2 * num, fill = 'black')
canvas.create_line(0, num, 2 * num, num, fill = 'black')

# Raio do circulo
raio = 0.45 * num

# Pontos do circulo
pontos_circ = [
    (0.05 * num), # x0
    (0.05 * num) + num, # y0
    (0.05 * num) + (2 * raio), # x1
    (0.05 * num) + (2 * raio) + num # y1
]

# Lados do retangulo e do triangulo
lado = 0.9 * num

# Pontos do quadrado
pontos_quad = [
    (0.05 * num) + num, # x0
    (0.05 * num) + num, # y0
    (0.05 * num) + num + lado, # x1
    (0.05 * num) + num + lado # y1
]

# Altura do triangulo
alt_tri = (math.sqrt(3)/2) * lado

# Pontos do triangulo
pontos_tri = [
    (1.05 * num), # x0
    num - (0.05 * num), # y0
    (1.05 * num) + lado, # x1
    num - (0.05 * num), # y1
    (1.05 * num) + (lado / 2), # x2
    num - (0.05 * num) - alt_tri # y2
]

# Circulo vermelho
criar_circulo(pontos_circ, 'red')

# Quadrado azul 
criar_quadrado(pontos_quad, 'blue', 'black')

# Triangulo amarelo
criar_triangulo(pontos_tri, 'green', 'black')

# Coloca os desenhos na tela
canvas.pack()

# Mantem a janela aberta
janela.mainloop()
