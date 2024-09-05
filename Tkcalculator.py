from tkinter import *

root=Tk()
root.title("Calculadora")

#Numeros Para Operacao

zero = Button(root, text="0", width=5, height=5)
zero.grid(row=6, column=1)

um = Button(root, text="1", width=5, height=5)
um.grid(row=5, column=1)

dois = Button(root, text="2", width=5, height=5)
dois.grid(row=5, column=2)

tres = Button(root, text="3", width=5, height=5)
tres.grid(row=5, column=3)

quatro = Button(root, text="4", width=5, height=5)
quatro.grid(row=4, column=1)

cinco = Button(root, text="5", width=5, height=5)
cinco.grid(row=4, column=2)

seis = Button(root, text="6", width=5, height=5)
seis.grid(row=4, column=3)

sete = Button(root, text="7", width=5, height=5)
sete.grid(row=3, column=1)

oito = Button(root, text="8", width=5, height=5)
oito.grid(row=3, column=2)

nove = Button(root, text="9", width=5, height=5)
nove.grid(row=3, column=3)

# Operações matemáticas

mais = Button(root, text="+", width=5, height=5)
mais.grid(row=5, column=4)

menos = Button(root, text="-", width=5, height=5)
menos.grid(row=4, column=4)

multi = Button(root, text="x", width=5, height=5)
multi.grid(row=3, column=4)

limpe = Button(root, text="C", width=5, height=5)
limpe.grid(row=6, column=2)

igual = Button(root, text="=", width=5, height=5)
igual.grid(row=6, column=3)

porcentagem = Button(root, text="%", width=5, height=5)
porcentagem.grid(row=6, column=4)


menos = Button(root, text="-", width=5,height=5)
menos.grid(column=4, row=4,)
root.geometry("400x400")
root.config(bg="white")

root.mainloop()