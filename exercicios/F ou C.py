temp = float(input("Digite uma temperatura"))
unidade = input("A temperatura citada está em 'C' celsius ou 'F' Fahrenheit")

if unidade == "c":
    f = temp * 9/5 + 32
    print("Sua temperatura em Fahrenheit é de: ",f)
else:
    c = (temp-32) *5/9
    print("Sua temperatura em Celsius é de :",c)
