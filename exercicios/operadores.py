num1 = int(input("Digite um número"))
num2 = int(input("Digite outro número"))

operador = int(input("Qual operação deseja realizar ? 1-soma, 2-subtração, 3-divisão, 4-multiplicação "))
if operador == 1:
    resultado = num1 + num2
    print("A soma é igual a: ",resultado)

elif operador == 2:
    resultado = num1 - num2
    print ("A subtração é igual a: ",resultado)

elif operador == 3:
    resultado = num1 / num2
    print ("A divisão é igual a: ",resultado)

else:
    resultado = num1 * num2
    print("A multiplicação é igual a:",resultado)

