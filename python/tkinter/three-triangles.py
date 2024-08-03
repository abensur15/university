# Importa o modulo TkInter
import tkinter as tk

# Cria a janela
janela = tk.Tk()

# Dimensiona a janela
janela.geometry("1920x1080")

# Cria e dimensiona a area de desenho
canvas = tk.Canvas(janela, width = 1920, height = 1080)

# Triangulo vermelho
canvas.create_polygon(
    [930, 480, 780, 480, 855, 600],
    outline = 'black',
    fill = 'red'
)

# Triangulo verde
canvas.create_polygon(
    [960, 480, 885, 600, 1035, 600],
    outline = 'black',
    fill = 'lime'
)

# Triangulo azul
canvas.create_polygon(
    [990, 480, 1140, 480, 1065, 600],
    outline = 'black',
    fill = 'blue'
)

# Coloca os desenhos na tela
canvas.pack()

# Mantem a janela aberta
janela.mainloop()
