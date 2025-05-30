from tkinter import*



window = Tk()

window.geometry('200x200')

window.title("Cálculo Área do Retângulo")



def calcular():

    try:

        comprimento = float(entrada1.get())

        largura = float(entrada2.get())



        area = comprimento*largura



        msg4["text"] = area



    except ValueError:

        msg4["text"] = "Valores Inválidos"







def limpar():

    entrada1.delete(0,END)

    entrada2.delete(0,END)



    msg4.config(text="0")



msg1 = Label(window, text="Comprimento do Retângulo:")

msg1.pack()



entrada1 = Entry(window)

entrada1.pack()

entrada1.focus()



msg2 = Label(window, text="Largura do Retângulo:")

msg2.pack()



entrada2 = Entry(window)

entrada2.pack()



botoes_frame = Frame(window)

botoes_frame.pack()



calcular_botao = Button(botoes_frame, text="Calcular", command=calcular)

calcular_botao.pack(side = LEFT)



espaco_botoes = Frame(botoes_frame, width=20)

espaco_botoes.pack(side = LEFT)



limpar_botao = Button(botoes_frame, text="Limpar", command=limpar)

limpar_botao.pack(side=LEFT)



msg3 = Label(window, text="Resultado:")

msg3.pack()



msg4 = Label(window, text="0", fg="red")

msg4.pack()



window.mainloop()
