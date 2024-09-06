from tkinter import *
from tkinter import ttk

calc = Tk()
calc.title("Calculadora")


style = ttk.Style()
style.theme_use('clam')
style.configure('estilo1.TButton', background='white', foreground='black', font=('Helvetica', 12, 'bold', ))
style.configure('estilo2.TButton', background='red', foreground='black', font=('Helvetica', 12, 'bold'))


# Variável para exibir os números e operações
show = "0"  # Inicializando como "0" para evitar erros
motext = StringVar()
motext.set(show)

# Exibindo o display da calculadora
display = ttk.Label(calc, textvariable=motext, style='Display.TLabel', anchor='e', relief="solid", borderwidth=3)
display.grid(columnspan=4, row=2,ipadx=10, ipady=10, sticky='nsew')

# Função para capturar os botões numéricos e operadores
def btnPress(num):
    global show
    if show == "0":  # Se o valor atual for "0", resetar para o próximo número
        show = ""
    show = show + str(num)  # Concatenando o número ou operador
    motext.set(show)  # Atualizando o display

# Função para calcular o resultado
def evaluate():
    global show
    try:
        # Corrigido: o eval espera "*" e não "x"
        total = str(eval(show))  # Calculando o valor da expressão
        if len(total) > 20:  # Limitação do tamanho do display
            total = total[0:20]
        motext.set(total)
        show = total  # Após mostrar o resultado, mantém o valor para operações futuras
    except:
        motext.set("Error")  # Caso a expressão seja inválida
        show = "0"

# Função para limpar o display
def clear():
    global show
    show = "0"
    motext.set(show)

# Função para calcular o fatorial
def fatorial(num):
    if num == 1:
        return 1
    elif num == 0: 
        return 1  # Corrigido: o fatorial de 0 é 1
    else:
        return num * fatorial(num - 1)

# Função para calcular o valor fatorial do número
def val_fat():
    global show
    try:
        show = int(show)  # Convertendo o valor atual para inteiro
        v = fatorial(show)
        show = str(v)
        if len(show) > 20:
            show = show[0:20]
        motext.set(show)
    except:
        motext.set("Error")
        show = "0"

# Função para calcular a raiz quadrada
def root():
    global show
    try:
        show = float(show) ** 0.5  # Calculando a raiz quadrada
        show = str(show)
        motext.set(show)
    except:
        motext.set("Error")
        show = "0"

# Função para calcular porcentagem
def percentage():
    global show
    try:
        show = str(float(show) / 100)  # Dividindo o valor por 100
        motext.set(show)
    except:
        motext.set("Error")
        show = "0"

# Botões numéricos
zero = ttk.Button(calc, text="0", style="estilo1.TButton",command=lambda: btnPress(0))
zero.grid(row=6, column=1,)

um = ttk.Button(calc, text="1",style="estilo1.TButton", command=lambda: btnPress(1))
um.grid(row=5, column=1)

dois = ttk.Button(calc, text="2",style="estilo1.TButton", command=lambda: btnPress(2))
dois.grid(row=5, column=2)

tres = ttk.Button(calc, text="3",style="estilo1.TButton", command=lambda: btnPress(3))
tres.grid(row=5, column=3)

quatro = ttk.Button(calc, text="4",style="estilo1.TButton",command=lambda: btnPress(4))
quatro.grid(row=4, column=1)

cinco = ttk.Button(calc, text="5",style="estilo1.TButton",command=lambda: btnPress(5))
cinco.grid(row=4, column=2)

seis = ttk.Button(calc, text="6",style="estilo1.TButton",command=lambda: btnPress(6))
seis.grid(row=4, column=3)

sete = ttk.Button(calc, text="7",style="estilo1.TButton",command=lambda: btnPress(7))
sete.grid(row=3, column=1)

oito = ttk.Button(calc, text="8",style="estilo1.TButton",command=lambda: btnPress(8))
oito.grid(row=3, column=2)

nove = ttk.Button(calc, text="9",style="estilo1.TButton",command=lambda: btnPress(9))
nove.grid(row=3, column=3)

# Operações matemáticas
mais = ttk.Button(calc, text="+", style="estilo1.TButton", command=lambda: btnPress("+"))
mais.grid(row=5, column=4   )

menos = ttk.Button(calc, text="-", style="estilo1.TButton", command=lambda: btnPress("-"))
menos.grid(row=4, column=4)

multi = ttk.Button(calc, text="x",style="estilo1.TButton",command=lambda: btnPress("*"))  # Corrigido: "x" não é reconhecido, usar "*"
multi.grid(row=3, column=4)

div = ttk.Button(calc, text="/", style="estilo1.TButton",command=lambda: btnPress("/"))
div.grid(row=2, column=4)

igual = ttk.Button(calc, text="=", style="estilo1.TButton", command=evaluate)  # Avaliar a expressão ao pressionar "="
igual.grid(row=6, column=3)

clear = ttk.Button(calc, text="C",style="estilo2.TButton",command=clear)  # Limpar a tela
clear.grid(row=6, column=2)

porcentagem = ttk.Button(calc, text="%",style="estilo1.TButton", command=percentage)  # Corrigido: função específica para calcular porcentagem
porcentagem.grid(row=6, column=4)

# Configurações da janela
calc.geometry("470x210")
calc.config(bg="white")

calc.mainloop()
