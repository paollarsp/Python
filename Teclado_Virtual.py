import tkinter as tk



window = tk.Tk()

window.title("Teclado Virtual")

window.geometry('500x300')



def add_entry(event):

    botao_clicado = event.widget

    entrada.insert(tk.END, botao_clicado["text"])



def clear_entry():

    entrada.delete(0, tk.END)



entrada = tk.Entry(window, font="Arial 12", width=50)

teclado = tk.Frame(window)



# Criação dos botões

botoes_texto = [

    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",

    "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P",

    "A", "S", "D", "F", "G", "H", "J", "K", "L",

    "Z", "X", "C", "V", "B", "N", "M", " "

]

for i in range(len(botoes_texto)):

        texto = botoes_texto[i]

        botao = tk.Button(teclado, text=texto, font="Arial 12 bold", width=3)

        botao.grid(row=i//10, column=i%10, padx=5, pady=5)

        botao.bind("<Button-1>", add_entry)



b_limpar = tk.Button(window, text="Limpar", font="Arial 12 bold", command=clear_entry)



entrada.pack(pady=5)

teclado.pack()

b_limpar.pack(pady=5)



window.mainloop()
