#Contador regresivo
#Tipo de bucle: para
#Enunciado: Solicita al usuario un número positivo e imprime un conteo regresivo hasta 0.
#Procedimiento paso a paso:
#1. Solicita un número entero positivo.
#2. Usa un bucle para que comience desde el número ingresado y vaya disminuyendo hasta 0.
#3. Muestra cada número en pantalla.

def contarNumeros(numero):
    for i in range (numero,-1,-1):
        print(i)
    
def main():
    numero=int(input("Ingrese un numero entero positivo: "))
    contarNumeros(numero)
    if numero>=0:
        contarNumeros(numero)
    else:
        print("Ingrese un numero entero positivo")
main()