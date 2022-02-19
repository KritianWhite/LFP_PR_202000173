from tkinter import *
from tkinter import filedialog
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
    # return cargaData

    # fileData = limpiarUTF8(fileData.lower())
    # fileData = fileData.close()
    print(fileData)
    # print("Se guardo el archivo de datos éxitosamente.\n")

# Lista del archivo .data


def Cargar_Instrucciones():
    # print('si funciona')
    Tk().withdraw()
    # Abriendo y leendo el archivo .lfp
    global fileInstrucciones
    fileInstrucciones = open(filedialog.askopenfilename(filetypes=(
        ('IPRO LFP Format files', '.lfp'), ("All files", "*.*"))), "r")
    fileInstrucciones = fileInstrucciones.read()
    fileInstrucciones = fileInstrucciones.lower()
    # return cargaInstrucciones

    # fileInstrucciones = limpiarUTF8(fileInstrucciones.lower()) #Esto indica que se eliminan caracteres UTF8 y coniverte todo el texto en minusulas
    # fileInstrucciones.close()
    print(fileInstrucciones)
    # print("Se guardo el archivo de instrucciones éxitosamente.\n")


def validacion():
    if fileData == "" and fileInstrucciones == "":
        print("No se han cargado los datos")
    elif fileData != "" and fileInstrucciones == "":
        print("No se ha cargado el archivo de instrucciones")
    elif fileData == "" and fileInstrucciones != "":
        print("No se ha cargado el archivo de Datos")
    else:
        print("")


def Analizar():

    # -------------------------LEER ARCHIVO .data------------------------
    # Para el mes
    dataMes = False
    # Mes = ""
    # Para el año
    dataAnio = False
    # Anio = ""
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
            # print("holas")
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
    # print(listaData)
    global x
    for x in arrayProducto:
        nombreProducto.append(x[0])
        Precio_Producto.append(x[1])
        Cantidad_Producto.append(x[2])
    #print(arrayProducto)#Impresion del array productos

    # -----------------LEER ARCHIVO .lfp-------------------
    global Diccionario
    Diccionario = {}

    txt = fileInstrucciones.replace("<â¿", "")
    txt1 = txt.replace("?>", "")
    txt2 = txt1.replace("\n", "")
    txt3 = txt2.split(",")

    for v in range(len(txt3)):
        auxiliarV = txt3[v].split(":")
        Diccionario[auxiliarV[0]] = auxiliarV[1]
        print(Diccionario)
    print(Diccionario["grafica"])


def hola():

    # -------------------------LEER ARCHIVO .data------------------------
    # Para el mes
    dataMes = False
    # Mes = ""
    # Para el año
    dataAnio = False
    # Anio = ""
    # Para productos
    dataProducto = True
    global nombreProducto
    nombreProducto = []
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
            print("veremos que pasa")
        elif i == "\n":
            pass
        elif i == "\t":
            pass

        elif dataMes == True and dataAnio == True and dataProducto == True:
            # print("holas")
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
    # print(listaData)
    global x
    for x in arrayProducto:
        str(nombreProducto.append(x[0]))
        Precio_Producto.append(x[1])
        Cantidad_Producto.append(x[2])
    # print(arrayProducto)#Impresion del array productos

    # -----------------LEER ARCHIVO .lfp-------------------

    Diccionario = {}

    txt = fileInstrucciones.replace("<â¿", "")
    txt1 = txt.replace("?>", "")
    txt2 = txt1.replace("\n", "")
    txt3 = txt2.split(",")

    for v in range(len(txt3)):
        auxiliarV = txt3[v].split(":")
        Diccionario[auxiliarV[0]] = auxiliarV[1]
        print(Diccionario)
    print(Diccionario["grafica"])


def pruebas():
    Diccionario = {}

    txt = fileInstrucciones.replace("<â¿", "")
    txt1 = txt.replace("?>", "")
    txt2 = txt1.replace("\n", "")
    txt3 = txt2.split(",")

    for v in range(len(txt3)):
        auxiliarV = txt3[v].split(":")
        Diccionario[auxiliarV[0]] = auxiliarV[1]
        print(Diccionario)
    print(Diccionario["grafica"])


def graficaBarras(ejex, ejey):

    at.rcdefaults()
    figB, aXB = at.subplots()

    # Grafica Barras
    #ejexB = nombreProducto
    #ejeyB = Cantidad_Producto
    
    #aXB.bar(nombreProducto, Cantidad_Producto)

    # Titulos de los ejes
    aXB.set_xlabel(Diccionario["titulox"])
    aXB.set_ylabel(Diccionario["tituloy"])

    # Aspecto de la gráfica
    aXB.grid(axis='y', color = 'lightblue', linestyle = 'dashed')
    aXB.set_title("")

    # Mostrar gráfica
    figB.savefig('./graficaBarras.png')
    at.show()

    #print("Barras")


def graficaLineas():
    print("Lineas")


def graficaCircular():
    print("Circular")


def Reportes():
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
    graficaBarras()
    # Reportes()
    Menu()

if opcion == 5:
    Salir()
if opcion <= 0 or opcion >= 6:
    print("Error, ingrese un número del menú.\n")
    Menu()
else:
    print(" ")
