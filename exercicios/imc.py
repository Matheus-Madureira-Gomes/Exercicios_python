peso = float(input("Qual seu peso em kg "))
altura = float(input("Qual sua altura em M "))

imc = peso / (altura**2)

if imc < 18.5:
    print("Você está abaixo do peso")

elif imc <= 24.9:
    print("Você está no peso adequado")

elif imc <= 29:
    print("Você está em sobrepeso")

else:
    print("Você está em estado de obesidade")
