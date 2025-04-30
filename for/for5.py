#Ejercicio 2: Contar números pares hasta un límite
#Tipo de bucle: mientras
#Enunciado: Solicita un número positivo y muestra todos los números pares desde 0 hasta ese
#número.
#Procedimiento paso a paso:
#1. Solicita al usuario un número positivo.
#2. Inicializa un contador en 0.
#3. Utiliza un bucle mientras que se ejecute mientras el contador sea menor o igual al número
#ingresado.
#4. En cada iteración, verifica si el contador es par.
#5. Si es par, muestra el número.
#6. Incrementa el contador en 1.

def contarPares(numero=0):
    for i in range(numero + 1 ):
        if i % 2 ==0:
            print(i, end=" ")
def main():
        numero= int(input("Ingrese un número positivo: "))
        contarPares(numero)

main()