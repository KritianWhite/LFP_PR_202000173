from audioop import add
from sqlite3.dbapi2 import _AggregateProtocol
from tkinter import *
from tkinter import filedialog
import re

from numpy import char 

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
    #print('Si funciona')
    Tk().withdraw()
    # Abriendo y leendo el archivo .data
    global fileData
    fileData = open(filedialog.askopenfilename(filetypes=( ('Data files','.data'),("All files","*.*") )), "r")
    fileData = fileData.read()
    cargaData = fileData.lower()
    return cargaData

    #fileData = limpiarUTF8(fileData.lower())
    #fileData = fileData.close()
    #print(fileData)
    print("Se guardo el archivo de datos éxitosamente.\n")
    
# Lista del archivo .data



def Cargar_Instrucciones():
    #print('si funciona')
    Tk().withdraw()
    # Abriendo y leendo el archivo .lfp
    global fileInstrucciones
    fileInstrucciones = open(filedialog.askopenfilename(filetypes=( ('IPRO LFP Format files','.lfp'),("All files","*.*") )), "r")
    fileInstrucciones = fileInstrucciones.read()
    cargaInstrucciones = fileData.lower()
    return cargaInstrucciones
    
    #fileInstrucciones = limpiarUTF8(fileInstrucciones.lower()) #Esto indica que se eliminan caracteres UTF8 y coniverte todo el texto en minusulas
    #fileInstrucciones.close()
    #print(fileInstrucciones)
    print("Se guardo el archivo de instrucciones éxitosamente.\n")

## El utf lo veo inecesario realmente por el momento
def limpiarUTF8(x):
    text = ""
    add = False

    for symbol in X:
        if symbol != '\"':
            if(symbol != " " and symbol != "\t" and symbol != "\n") or add1:
                texto += symbol
        elif not add1:
            text += symbol
            add1 = False
        else:
            text =+ symbol
            add1 = False
    return text


def Analizar(x):

    ########## Leendo archivo .data ############
    
    # Para el mes
    dataMes = False
    Mes = ""
    # Para el año
    dataAnio = False
    Anio = ""
    # Para productos
    dataProducto = True
    arrayProducto = []
    precioProducto = False
    cantidadProducto = False

    Contador = 0
    auxiliar = ""

    for i in x:
        if dataMes == False:
            if i != ":":
                auxiliar=+ i
            else:
                dataMes = auxiliar
                dataMes = True
                auxiliar = ""
        elif dataAnio == False:
            if i != "=":
                auxiliar=+ i
            else:
                dataAnio = auxiliar
                dataAnio = True
                auxiliar = ""
        elif i == "(":
            dataProducto = True
        elif i == ")":
            print("veremos que pasa")
        elif (dataMes and dataAnio and dataProducto) == True:
            if i == "[":
                precioProducto = True
            elif i == "]":
                cantidadProducto = True
            

    
    #print("insertar procedimineot aqui")

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
if opcion == 4:
    Reportes()
if opcion == 5:
    Salir()
if opcion <= 0 or opcion >=6:
    print("Error, ingrese un número del menú.\n")
    Menu()
else:
    print(" ")
print("holamuneod")