veloc = float(input("Qual a velocidade em km/h que o carro estava ao passar no radar"))

if veloc <= 80:
    print("Ok, tudo normal")

else:
    KmAcima = veloc - 80
    multa = 15 * KmAcima
    print("A multa aplicada à cada km/h acida do limite ficou de: ",multa)
