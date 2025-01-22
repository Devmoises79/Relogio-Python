# importação de bibliotecas

from tkinter import * 
import tkinter
from datetime import datetime


# declaração de cores
cor1 = "#3d3d3d"
cor2 = "#fafcff"
cor3 = "#21c25c"
cor4 = "#eb463b"
cor5 = "#dedcdc"
cor6 = "#3080f0"

# cor de fundo
fundo = cor1

# cor do texto
cor = cor2

# criação da janela
janela=Tk()
janela.title("Relógio Digital")
janela.geometry("450x170")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=cor1)

# criação da função
def relogio():

    # atualiza a hora
    tempo=datetime.now()

    # formata a hora e o dia para o formato desejado
    hora=tempo.strftime("%H:%M:%S") 
    diaDaSemana=tempo.strftime("%A") # retorna o dia da semana
    dia=tempo.day # retorna o dia
    mes=tempo.strftime("%b") # retorna o mês por extenso
    ano=tempo.strftime("%Y") # retorna o ano
    
    # atualiza os labels
    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=diaDaSemana +" " + str(dia) + "/" + str(mes + "/" + str(ano)))

# criação do label do relógio
l1 = Label(janela, text="", font=("sans-serif 80"), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)

# criação do label da data
l2 = Label(janela, text="", font=("sans-serif 20"), bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)

# chama a função
relogio()
janela.mainloop() # inicia a janela