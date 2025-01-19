produto = float(input("Qual o valor do produto ?"))

if produto <= 100:
    desconto = produto * 0.05
    valorFinal = produto - desconto
    print("O seu produto com descontos ficou com valor final de: ",valorFinal)
elif produto <= 200:
    desconto = produto * 0.1
    valorFinal = produto - desconto
    print("O seu produto com descontos ficou com valor final de: ",valorFinal)
else:
    desconto = produto * 0.15
    valorFinal = produto - desconto
    print("O seu produto com descontos ficou com valor final de: ",valorFinal)
