data = input("Insira a data (na seguinte formatação dd/mm/aaaa)")

if len(data)== 10:

    if (data[2] or data[5])!= "/":
        print("Formatação inválida (não apresenta as '/' nos locais exatos)")
    else:
        dia = int(data[0:2])
        mês = int(data[3:5])
        ano = int(data[6:10])

        if ano>2025:
            print("Data inválida (ano)")
        elif mês<1 or mês>12:
            print("Data inválida (mês)")
        elif dia<1 or dia>31:
            print("Data inválida (dias)")

    if (mês==4 or mês==6 or mês==9 or mês==11) and dia>30:
            print("Data inválida (esse mês possui apenas 30 dias)")
    if mês==2:
        #ano bissexto
        if ano%100==0 and ano%400==0 and mês==2 and dia!=29: #se for divisível por 400 e centenário é bissexto                                           :
            print("Data inválida (esse mês possui no máximo 29 dias)")
        elif ano%4==0 and mês==2 and dia!=29:
            print("Data inválida (esse mês possui no máximo 29 dias)")
        elif dia!=28:
            print("Data inválida (esse mês possui no máximo 28 dias)")
    print("Data válida")         
else:
    print("Formatação inválida (quantidade de caracteres superior ou inferior a 10)")

