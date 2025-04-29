#Hacer un programa que me da la tabla de multiplicar de un numero cualquiera del 1 al 12
def multiplicarNumero(numero):
    for i in range (1,13):
        resultado = numero * i
        print(f"{numero} * {i} = {resultado}")
    
def main(): 
    numero = int(input("Ingrese el número a multiplicar: "))
    multiplicarNumero(numero)

main()