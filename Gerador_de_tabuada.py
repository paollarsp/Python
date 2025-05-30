import tkinter as tk

import tkinter.scrolledtext as st



window = tk. Tk()



def gerador_tabuada():

    try:

    aux=0

    valor = int(entrada.get())



    while aux<=100:

        resultado = valor*aux

        texto.insert(tk.INSERT,f"{aux} x {valor} = {resultado}\n")

        aux +=1





window.title("Tabuada de 0 a 100")

window.geometry('300x300')



msg = tk.Label(window, text="Digite um número:")

entrada = tk.Entry(window)

botao = tk.Button(window, text="Calcular", command = gerador_tabuada)

texto = st.ScrolledText(window, width=20, height=5)



msg.pack(pady=5)

entrada.pack(pady=5)

botao.pack(pady=5)

texto.pack(pady=5)



window.mainloop()
