temp = []

mes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

media = 0



for i in range(12):

    valor = float(input("Digite a temperatura em ºC do %dº mês: " %(i+1)))

    temp.append(valor)

    media += valor



media = media/12



print("Meses com temperatura acima da média anual\n")

print("Média anual: %.1f" %media)



for i in range(12):

    if temp[i]>media:

        print("Mês %d - %s: %.1f ºC" %(i+1, mes[i], temp[i]))
