# Importa o modulo TkInter
import tkinter as tk

# Cria a janela
janela = tk.Tk()

# Dimensiona a janela
janela.geometry("1920x1080")

# Cria e dimensiona a area de desenho
canvas = tk.Canvas(janela, width = 1920, height = 1080)

# Funcao para criar um circulo
def criar_circulo(ponto_x, ponto_y, raio, cor):
    canvas.create_oval(
        ponto_x,
        ponto_y,
        raio + ponto_x,
        raio + ponto_y,
        outline = cor,
        width = 10
    )

# Circulo azul
criar_circulo(410, 240, 200, '#0885c2')

# Circulo amarelo
criar_circulo(535, 340, 200, '#fbb132')

# Circulo preto
criar_circulo(660, 240, 200, 'black')

# Circulo verde
criar_circulo(785, 340, 200, '#1c8b3c')

# Circulo vermelho
criar_circulo(910, 240, 200, '#ed334e')

# Coloca os desenhos na tela
canvas.pack()

# Mantem a janela aberta
janela.mainloop()