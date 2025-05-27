num = input("Insira um número inteiro e positivo: ")



#verificando se todos os caracteres digitados são números

def énumeros (num_2):

    for  i in num:

        if not i in "0123456789":

            return False

    return True



énumeros(num)



while énumeros(num) == False:

    num = input("Dígitos informados contém outros caracteres além de números. Digite novamente: ")

    énumeros(num)



invertido = ""



while len(num)>1:

    ultimo_digito = num[-1:]

    invertido = invertido + ultimo_digito

    num = num[:-1]



invertido = invertido + num



print("O resultado invertido será: %s" %invertido)
