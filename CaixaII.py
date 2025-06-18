conta = int(input("Digite o valor da conta: "))

pagamento = int(input("Digite o valor do pagamento: "))

                

troco = pagamento-conta



notas = [50,20,10,5,2,1]



num_notas = [0,0,0,0,0,0] #corresponde respectivamente aos valores de notas acima



while troco >= notas[0]:

    num_notas[0] += 1

    troco -= 50



while troco >= notas[1]:

    num_notas[1] += 1

    troco -= 20



while troco >= notas[2]:

    num_notas[2] += 1

    troco -= 10



while troco >= notas[3]:

    num_notas[3] += 1

    troco -= 5



while troco >= notas[4]:

    num_notas[4] += 1

    troco -= 2



while troco >= notas[5]:

    num_notas[5] += 1

    troco -= 1



print("\nTroco:")

print("%d nota(s) de R$50.00" %num_notas[0])

print("%d nota(s) de R$20.00" %num_notas[1])

print("%d nota(s) de R$10.00" %num_notas[2])

print("%d nota(s) de R$5.00" %num_notas[3])

print("%d nota(s) de R$2.00" %num_notas[4])

print("%d moeda(s) de R$1.00" %num_notas[5])
