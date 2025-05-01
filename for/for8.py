#Ejercicio 6: Promedio de calificaciones
#Tipo de bucle: repetir-hasta
#Enunciado: Solicita una cantidad indeterminada de calificaciones hasta que el usuario ingrese -1.
#Calcula y muestra el promedio.
#Procedimiento paso a paso:
#1. Inicializa suma y contador en 0.
#2. Usa un bucle repetir-hasta para pedir una calificación.
#3. Si el número ingresado es diferente de -1, suma la calificación y aumenta el contador.
#4. Finaliza cuando el usuario ingresa -1.
#5. Calcula y muestra el promedio.

def promediarNotas():
    nota=0
    contador_nota=0
    suma=0
    while nota != -1:
        nota=int(input("Ingrese una nota de 0 a 100: "))
        
        if nota==-1:
            break
        else:
            suma+=nota
            contador_nota+= +1
    if contador_nota>0:
                promedio= suma/contador_nota
                print(f"Su promedio es {promedio:.0f}")
    else:
        print("No se ingreso una nota ")
        
def  main():
    promediarNotas()
main()
        
