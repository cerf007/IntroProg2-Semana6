#Leer 2 numeros e imprimir los numero entre ellos
def mostrarNumeros(inicio=0, fin=0):
    if (inicio<fin):
        for i in range (inicio, fin+1):
            print(i, end=" ")
    else:
        for i in range (fin, inicio+1):
            print(i, end=" ")
            
def main():
    inicio = int(input("Ingrese el primer número: "))
    fin = int(input("Ingrese el segundo número: "))
    mostrarNumeros(inicio, fin)
    
main()