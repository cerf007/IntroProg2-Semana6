#Ejercicio 3: Suma de números hasta alcanzar un límite
#Tipo de bucle: repetir-hasta
#Enunciado: Solicita al usuario números hasta que la suma de ellos supere 100.
#Procedimiento paso a paso:
#1. Inicializa una variable suma en 0.
#2. Usa un bucle repetir-hasta para pedir al usuario que ingrese un número.
#3. Suma el número ingresado a la variable suma.
#4. Repite mientras la suma sea menor o igual a 100.
#5. Al finalizar, muestra la suma total.

def sumarNumeros (primer_numero):
    suma=0
    suma=primer_numero
    while suma<=100:
        numero= int(input("Ingrese un número: "))
        suma= suma + numero
        print(f"La suma es: {suma}")
    print(f"La suma ha alcanzado su máximo de 100, su suma actual es de {suma}")
        
def main():
    primer_numero=int(input("Ingrese el primer numero: "))
    sumarNumeros(primer_numero)

main()
    