from tkinter import *
import tkinter
from datetime import datetime

###### Cores #######
cor1 = "#3d3d3d"  # preta
cor2 = "#fafcff"  # branca
cor3 = "#21c25c"  # verde
cor4 = "#eb463b"  # vermelha
cor5 = "#dedcdc"  # cinza
cor6 = "#3080f0"  # azul

fundo = cor1
cor = cor3

janela = Tk()
janela.title("Horário")
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg = fundo)


def horario():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%B")
    ano = tempo.strftime("%Y")
    l1.config(text = hora)
    l1.after(200, horario)
    l2.config(text = dia_semana + " " + str(dia) + " " + str(mes) + " " + str(ano))

l1 = Label(janela, text = "10:40:34", font = "ROBOTO 80", bg = fundo, fg = cor)
l1.grid(row = 0, column = 0, sticky = NW, padx = 5)

l2 = Label(janela, text = "", font = "ROBOTO 20", bg = fundo, fg = cor)
l2.grid(row = 25, column = 0, sticky = NW, padx = 5)

horario()
janela.mainloop()