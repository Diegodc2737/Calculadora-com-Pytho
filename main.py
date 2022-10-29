# Importando tkinter
from tkinter import Button, Frame, Tk
from tkinter import ttk
from tkinter import *

from setuptools import Command

# Cores
cor1 = "#332d2c" # preta
cor2 = "#feffff" # branca
cor3 = "#292e5e" # azul
cor4 = "#d5d6e0" # cinzenta
cor5 = "#f5691d" # laranja

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x308")
janela.config(bg=cor1)


# Criando frames
frame_tela = Frame(janela, width=335, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=335, height=268 )
frame_corpo.grid(row=1, column=0)

# Criando label
valor_texto = StringVar()
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=6, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0,y=0)



# variável todos valores
todos_valores = ''


# criando função
def entrar_valores(valor):
    global todos_valores
    
    todos_valores = todos_valores + str(valor)
    
    # passando valor ára a tela
    valor_texto.set(todos_valores)
    
# função para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    # resultado na tela
    valor_texto.set(str(resultado))

# função limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")




# criando botoes
b_1 = Button(frame_corpo, command=limpar_tela, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command= lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_corpo,command= lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_corpo,command= lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=53)
b_5 = Button(frame_corpo,command= lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=57, y=53)
b_6 = Button(frame_corpo,command= lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=117, y=53)
b_7 = Button(frame_corpo,command= lambda: entrar_valores('*'), text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=53)

b_8 = Button(frame_corpo,command= lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=100)
b_9 = Button(frame_corpo,command= lambda: entrar_valores('5'), text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=57, y=100)
b_10 = Button(frame_corpo,command= lambda: entrar_valores('6'), text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=117, y=100)
b_11 = Button(frame_corpo,command= lambda: entrar_valores('-'), text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=100)

b_12 = Button(frame_corpo,command= lambda: entrar_valores('1'), text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=150)
b_13 = Button(frame_corpo,command= lambda: entrar_valores('2'), text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=57, y=150)
b_14 = Button(frame_corpo,command= lambda: entrar_valores('3'), text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=117, y=150)
b_15 = Button(frame_corpo,command= lambda: entrar_valores('+'), text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=150)

b_16 = Button(frame_corpo,command= lambda: entrar_valores('0'), text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=200)
b_17 = Button(frame_corpo,command= lambda: entrar_valores('.'), text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=200)
b_18 = Button(frame_corpo, command= calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=200)



janela.mainloop()

