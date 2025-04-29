#Leer un número ingresado por el usuario
#mostrar la letra a por cada letra del 1 al número
#ingresado por el usuario ejemplo, Numero: 3
#a
#aa
#aaa
def mostrarLetra(numero):
    for i in range (numero + 1):
        print(f"a"* i )
        
def main():
    num = int(input("Ingresa un número: "))
    mostrarLetra(num)
  
main()