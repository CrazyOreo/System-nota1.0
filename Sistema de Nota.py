nota1=float(input("Por favor, qual foi sua primeira nota? \n"))
nota2=float(input("Por favor, qual foi sua segunda nota? \n"))

valorfinal=(nota1+nota2)/2

if valorfinal==10:
    print("Aprovado com Distinção")
elif valorfinal<=7:
    print("Aprovado")
else:
    print("Reprovado")