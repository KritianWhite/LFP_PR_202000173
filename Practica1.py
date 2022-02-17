from tkinter import *
from tkinter import filedialog



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
    global root
    #root = Tk()
    fileData = open(filedialog.askopenfilename(filetypes=( ('Data files','.data'),("All files","*.*") )), "r")
    fileData = fileData.read()
    print(fileData)

def Cargar_Instrucciones():
    Tk().withdraw()
    fileInstrucciones = open(filedialog.askopenfilename(filetypes=( ('IPRO LFP Format files','.lfp'),("All files","*.*") )), "r")
    print(fileInstrucciones)
    #fileData = tkinter.fileopenbox()

def Analizar():
    print("insertar procedimineot aqui")

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
