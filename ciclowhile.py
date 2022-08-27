centinela = 100

#ciclo while
print(".:Menu:.")
print("1. Saludar")
print("2. Despedir")
print("0. Salir")
while(centinela!=0):
    centinela=int(input("Digita una opcion: "))
    if(centinela==1):
        print("Hola")
    elif(centinela==2):
        print("Chao")
    elif(centinela==0):
        break
    else:
        print("Digite una opcion valida")
else:
    print("Termine")