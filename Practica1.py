from tkinter import *
from tkinter import filedialog
from matplotlib import colors
import matplotlib.pyplot as at
import re

# Funcion del Menú


def Menu():
    global opcion
    print("******* MENU ********")
    print("1. Cargar Data.")
    print("2. Cargar instrucciones.")
    print("3. Analizar.")
    print("4. Reportes.")
    print("5. Salir")

    opcion = int(input('Ingrese un número del menú:\n'))

Menu()


def Cargar_Data():
    # print('Si funciona')
    Tk().withdraw()
    # Abriendo y leendo el archivo .data
    global fileData
    fileData = open(filedialog.askopenfilename(filetypes=(
        ('Data files', '.data'), ("All files", "*.*"))), "r")
    fileData = fileData.read()
    fileData = fileData.lower()
    # fileData = fileData.close()
    # print(fileData)
    print("Se guardo el archivo de datos éxitosamente.\n")


def Cargar_Instrucciones():
    # print('si funciona')
    Tk().withdraw()
    # Abriendo y leendo el archivo .lfp
    global fileInstrucciones
    fileInstrucciones = open(filedialog.askopenfilename(filetypes=(('IPRO LFP Format files', '.lfp'), ("All files", "*.*"))), "r")
    fileInstrucciones = fileInstrucciones.read()
    fileInstrucciones = fileInstrucciones.lower()
    # fileInstrucciones.close()
    # print(fileInstrucciones)
    print("Se guardo el archivo de instrucciones éxitosamente.\n")


def validacion():
    if fileData == "" and fileInstrucciones == "":
        print("No se han cargado los datos")
    elif fileData != "" and fileInstrucciones == "":
        print("No se ha cargado el archivo de instrucciones")
    elif fileData == "" and fileInstrucciones != "":
        print("No se ha cargado el archivo de Datos")
    else:
        print("")

nombreProducto = []
Cantidad_Producto = []

def Analizar():
    # -------------------------LEER ARCHIVO .data------------------------
    # Para el mes
    dataMes = False
    dataAnio = False
    # Para productos
    dataProducto = True
    global nombreProducto
    nombreProducto = []
    global arrayProducto
    arrayProducto = []
    global Precio_Producto
    Precio_Producto = []
    precioProducto = False
    global Cantidad_Producto
    Cantidad_Producto = []
    cantidadProducto = False

    Contador = 0
    auxiliar = ""

    for i in fileData:
        if dataMes == False:
            if i != ":":
                auxiliar += i
            else:
                dataMes = auxiliar
                dataMes = True
                auxiliar = ""
        elif dataAnio == False:
            if i != "=":
                auxiliar += i
            else:
                dataAnio = auxiliar
                dataAnio = True
                auxiliar = ""
        elif i == "(":
            dataProducto = True
        elif i == ")":
            print("")
            #print("Veremos que pasa")
        elif i == "\n":
            pass
        elif i == "\t":
            pass

        elif dataMes == True and dataAnio == True and dataProducto == True:
            if i == "[":
                precioProducto = True
            elif i == "]":
                cantidadProducto = True
            elif i == '\"' or i == '\'':
                Contador += 1
            elif i == ";" and precioProducto == True and cantidadProducto == True and Contador == 2:
                listaData = auxiliar.split(",")

                listaData[1] = float(listaData[1])
                listaData[2] = int(listaData[2])
                arrayProducto.append(listaData)
                precioProducto = False
                cantidadProducto = False
                Contador = 0
                auxiliar = ""
            else:
                auxiliar += i

    # -----------------LEER ARCHIVO .lfp-------------------
    txt = fileInstrucciones.replace("<â¿", "")
    txt1 = txt.replace("?>", "")
    txt2 = txt1.replace("\n", "")
    txt3 = txt2.split(",")

    global Diccionario
    Diccionario = {}

    for v in range(len(txt3)):
        auxiliarV = txt3[v].split(":")
        Diccionario[auxiliarV[0]] = auxiliarV[1]
        #print(Diccionario)
    #print(Diccionario["grafica"])

    for x in arrayProducto:
        nombreProducto.append(x[0])
        Precio_Producto.append(x[1])
        Cantidad_Producto.append(x[2])
        #print("hello")
    
    if Diccionario["grafica"] == ' "barras"':
        graficaBarras(nombreProducto, Cantidad_Producto)
        #print("hola")
    elif Diccionario["grafica"] == ' "lineas"':
        graficaLineas(nombreProducto, Cantidad_Producto)
    elif Diccionario["grafica"] == ' "circular"' or Diccionario["grafica"] == ' "pie"' or Diccionario["grafica"] == ' "pastel"':
        graficaCircular(nombreProducto, Cantidad_Producto)
    else:
        print("Ocurrio algún error. \n")


def graficaBarras(ejexB, ejeyB):

    at.rcdefaults()
    figB, aXB = at.subplots()

    # Grafica Barras

    aXB.bar(ejexB, ejeyB)

    # Titulos de los ejes
    aXB.set_xlabel("Producto")
    aXB.set_ylabel("Cantidad")

    # Aspecto de la gráfica
    aXB.grid(axis='y', color = 'lightblue', linestyle = 'dashed')
    aXB.set_title("")

    # Mostrar gráfica
    figB.savefig('./graficaBarras.png')
    at.show()

    #print("Barras")


def graficaLineas(ejexB, ejeyB):
    at.rcdefaults()
    figL, aXL = at.subplots()

    # Grafica Lineas

    aXL.plot(ejexB, ejeyB) 

    # Titulos de los ejes
    aXL.set_xlabel("Producto")
    aXL.set_ylabel("Cantidad")

    # Aspecto de la gráfica
    aXL.grid(axis='y', color = 'lightblue', linestyle = 'dashed')
    aXL.set_title("")

    # Mostrar gráfica
    figL.savefig('./graficaLineas.png')
    at.show()


def graficaCircular(ejexB, ejeyB):
    at.rcdefaults()
    figC, aXC = at.subplots()

    # Grafica Circular
    aXC.pie(ejeyB, labels=ejexB, autopct="%0.1f %%")
    aXC.axis("equal")
    # Titulos de los ejes
    aXC.set_xlabel("Producto")
    aXC.set_ylabel("Cantidad")

    # Aspecto de la gráfica
    #aXC.grid(axis='y', color = 'blues')
    aXC.set_title("")

    # Mostrar gráfica
    figC.savefig('./graficaPie.png')
    at.show()


def Reportes():
    
    f = open('holamundo.html','w')

    mensaje = """
    
    

    """

    f.write(mensaje)
    f.close()
    print("insertar procedimineot aqui")


def Salir():
    exit()


if opcion == 1:
    Cargar_Data()
    Menu()
if opcion == 2:
    Cargar_Instrucciones()
    Menu()
if opcion == 3:
    Analizar()
    Menu()
if opcion == 4:
    graficaCircular(nombreProducto, Cantidad_Producto)
    # Reportes()
    Menu()
if opcion == 5:
    Salir()
if opcion <= 0 or opcion >= 6:
    print("Error, ingrese un número del menú.\n")
    Menu()
else:
    print(" ")
