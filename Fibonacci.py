a = 0

b = 1

passo = 1

i = 0



num = int(input("Insira um número inteiro: "))



print("Série de Fibonacci")

print("F%d = %d" %(passo,b))

num -= 1

for i in range(num):

    aux = a+b

    a = b

    b = aux

    passo = passo+1

    print("F%d = %d" %(passo,aux))
