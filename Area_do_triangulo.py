from tkinter import*



window = Tk()

window.title("Calculadora - área de um triângulo")

window.geometry('200x200')



def calcular():

    try:

        base = float(entrada1.get())

        altura = float(entrada2.get())



        area = (base*altura)/2



        msg4.config(text=f"{area}")



    except ValueError:

        msg4.config(text="Valores incorretos")



def limpar():

    entrada1.delete(0,END)

    entrada2.delete(0,END)



    msg4.config(text="0")



msg1 = Label(window, text="Base do Triângulo:")

msg1.pack()



entrada1 = Entry(window)

entrada1.pack()

entrada1.focus()



msg2 = Label(window, text="Altura do Triângulo:")

msg2.pack()



entrada2 = Entry(window)

entrada2.pack()



frame_botoes = Frame(window)

frame_botoes.pack()



calcular_botao = Button(frame_botoes,text="Calcular", command = calcular)

calcular_botao.pack(side=LEFT)



frame_espaco = Frame(frame_botoes, width='75')

frame_espaco.pack()



limpar_botao = Button(frame_botoes, text="Limpar", command=limpar)

limpar_botao.pack(side=RIGHT)



msg3 = Label(window, text="Resultado:")

msg3.pack()



msg4 = Label(window, text="0", fg="red")

msg4.pack()



window.mainloop()
