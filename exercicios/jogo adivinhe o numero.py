import random
numero = random.randint(1,100)

chute = int(input("Chute um número de 1 a 100"))

while numero != chute:
    print("Você errou")
    if numero > chute:
        print("O numero é maior")
    else:
        print("O número é menor")
    chute = int(input("Chute um numero de 1 a 100"))
print("Boa, você acertou!")
