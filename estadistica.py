# Programa en Python que permite calcular
# formulas estadisticas de la
# media aritmetica
# Realizado por el Lcdo. Jose Fernando Frugone Jaramillo
# para el calculo de la media
# Para el arreglo
# arreglo de datos
import statistics as stats
import math
# Para el calculo de la media
def media(numero):
    # Para calcular la media aritmetica
    # definimos los numeros que valor a
    # ingresar dependiendo del total
    # de numeros a ingresar
    # Variable valor para los valores a ingresar
    # Variable cont para contar
    # hasta el numero de veces a ingresar
    valor = 0
    cont = 0
    # Definimos el tamaño del arreglo
    datos = []
    # para el tamaño
    for cont in range(0,numero): 
        # Para los numeros que se va a ingresar
        # dependiendo de los numeros
        valor = int(input(f"Ingrese valor del indica {cont} : ".format(cont)))
        # validar que el valor ingresado sea positvo
        if valor<=0:
            print()
            print(f"Ingreso incorrecto debe ingresar numeros positivos {valor} : \n ", end="")
            print()
            valor = int(input(f"Ingrese valor del indice {cont} : ".format(cont)))
            # Agrega valor al arreglo
            datos.append(valor)
        else:
            datos.append(valor)
    # Para mostrar la media aritmetica de los numeros ingresados
    print()
    print("La media es : ", round(sum(datos)*1.0 / numero,2))
# Termino de la funcion de la Media aritmetica

# Para el calculo de la moda
def moda(numero):
    # Para el calculo de la moda es el valor que se repite
    cont = 0
    valor = 0
    # definimos el tamaño del arreglo
    datos = []
    # para el total de valores
    for cont in range(0,numero):
        valor = int(input(f"Ingrese valor de la posicion {cont} de este numero : ".format(cont)))
        # validar el valor ingresado
        if valor<=0:
            print()
            print(f"Ingreso incorrecto debe ingresar numeros positivos {valor} : \n", end="")
            print()
            valor = int(input(f"Ingrese valor de la posicion {cont} de este numero : ".format(cont)))
            datos.append(valor)
        else:
            datos.append(valor)     
    # Para mostrar la moda
    # de un conjunto de numeros
    print()
    print("La moda es : ", stats.mode(datos), end="")
    print()
    
# Para el calculo de la mediana
def mediana(numero):
    # Para el calculo de la mediana encuentra el valor central
    # de un grupo de valores
    cont = 0
    valor = 0
    # Definimos el tamaño del arreglo
    datos = []
    # para el tamaño del arreglo
    for cont in range(0,numero):
        # Para la mediana
        valor = int(input(f"Ingrese valor de la posicion {cont} de este numero : ".format(cont)))
        if valor<=0:
            print()
            print(f"Ingreso incorrecto debe ingresar numeros positivos {valor} : \n", end="")
            print()
            valor = int(input(f"Ingrese valor de la posicion {cont} de este numero : ".format(cont)))
            datos.append(valor)
        else:
            datos.append(valor)
    # Para mostrar la mediana
    print()
    print("La mediana es : " , stats.median(datos))

# Terminacion del proceso
def media_arm(numero):
    # Para el calculo de la media armonica es el reciproco
    # de la media aritmetica de los inversos de los datos
    cont = 0
    valor = 0
    # Definimos el arreglo
    datos = []
    # para recorrer el arreglo
    for cont in range(0,numero):
        # Para la Media Armonica
        valor = int(input(f"Ingrese valor de posicion {cont} de este numero : ".format(cont)))
        if valor<=0:
            print()
            print(f"Ingreso incorrecto debe ingresar numeros postivos {valor} : \n", end="")
            print()
            valor = int(input(f"Ingrese valor de la posicion {cont} de este numero : ".fotmat(cont)))
            datos.append(valor)
        else:
            datos.append(valor)
    # Para mostrar la Media Armonica
    print()
    print("La media Armonica es : " , stats.harmonic_mean(datos))
# Fin del proceso
while True:
    print()
    print("Programa para calcular los calculos Estadisticos \n", end="")
    print("Realizado por el Lcdo Jose Fernando Frugone Jaramillo \n", end="")
    print()
    opcion = 0
    print("1.- Media Aritmetica \n", end="")
    print("2.- Moda \n", end="")
    print("3.- Mediana \n", end="")
    print("4.- Media Armonica \n", end="")
    print("5.- Salir \n", end="")
    print()
    opcion = int(input('Ingrese una opcion  (1/5) : '))
    if opcion==1:
        num_veces = int(input('Ingrese el numero de veces a ingresar : '))
        media(num_veces)
    elif opcion==2:
        num_veces = int(input('Ingrese el numero de veces a ingresar : '))
        moda(num_veces)
    elif opcion==3:
        num_veces = int(input('Ingrese el numero de veces a ingresar : '))
        mediana(num_veces)
    elif opcion==4:
        num_veces = int(input('Ingrese el numero de veces a ingresar : '))
        media_arm(num_veces)
    else:
        print()
        print("Termino el programa \n", end="")
        break

