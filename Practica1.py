
from tkinter import *
from tkinter import filedialog
import webbrowser
from matplotlib import axis, colors
import matplotlib.pyplot as at
import numpy as np


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
arrayProducto = []
nombreProducto = []
ArrayAuxiliar = []

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
    global GananciaProducto
    GananciaProducto = []

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
        GananciaProducto.append(x[1]*x[2])
    #print(GananciaProducto)
    
    arrayAux = []
    global ArrayAuxiliar
    ArrayAuxiliar = []
    for r in range(len(arrayProducto)):
        arrayAux = []
        arrayAux.append(nombreProducto[r])
        arrayAux.append(Precio_Producto[r])
        arrayAux.append(Cantidad_Producto[r])
        arrayAux.append(GananciaProducto[r])
        ArrayAuxiliar.append(arrayAux)
    #print(ArrayAuxiliar)

    #arrayProducto.sort(reverse=True)

    if Diccionario["grafica"] == ' "barras"':
        graficaBarras(nombreProducto, Cantidad_Producto)
        print("Se imprimió y guardó la grafica de barras.\n")
        #print("hola")
    elif Diccionario["grafica"] == ' "lineas"':
        graficaLineas(nombreProducto, Cantidad_Producto)
        print("Se imprimió y guardó la grafica de Lineas.\n")
    elif Diccionario["grafica"] == ' "circular"' or Diccionario["grafica"] == ' "pie"' or Diccionario["grafica"] == ' "pastel"':
        graficaCircular(nombreProducto, Cantidad_Producto)
        print("Se imprimió y guardó la grafica circular/pie/pastel.\n")
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
    
    j = ""
    k = ""
    l = ""

    f = open('index.html','w')

    mensaje = """
    
    <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
    <title>REPORTES</title>
    <meta name="description" content="" />
    <meta name="author" content="Tooplate" />
    <!-- Bootstrap core CSS -->
    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet" />
    <!-- Additional CSS Files -->
    <link href="https://fonts.googleapis.com/css?family=Lato:100,300,400,700,900" rel="stylesheet" />
    <link rel="stylesheet" href="assets/css/fontawesome.css" />
    <link rel="stylesheet" href="assets/css/tooplate-style.css" />
    <link rel="stylesheet" href="assets/css/owl.css" />
    <link rel="stylesheet" href="assets/css/lightbox.css" />
  </head>
<!--
https://www.tooplate.com/view/2116-blugoon
-->
  <body>
    <div id="page-wraper">
      <!-- Sidebar Menu -->
      <div class="responsive-nav">
        <i class="fa fa-bars" id="menu-toggle"></i>
        <div id="menu" class="menu">
          <i class="fa fa-times" id="menu-close"></i>
          <div class="container">
            <div class="image">
              <a href="#"><img src="assets/images/logo-image.jpg" alt="Blugoon by Tooplate" /></a>
            </div>
            <div class="author-content">
              <h4>202000173</h4>
              <span>Christian Alessander Blanco González</span>
            </div>
            <nav class="main-nav" role="navigation">
              <ul class="main-menu">
                <li><a href="#section1">Introducción</a></li>
                <li><a href="#section2">Ganancias</a></li>
                <li><a href="#section4">Contacto</a></li>
              </ul>
            </nav>
            <div class="social-network">
              <ul class="soial-icons">
                <li>
                  <a href="https://www.facebook.com/KriitianWhite/"><i class="fa fa-facebook"></i></a>
                </li>
                <li>
                  <a href="https://twitter.com/blanco5321"><i class="fa fa-twitter"></i></a>
                </li>
                <li>
                  <a href="#"><i class="fa fa-linkedin"></i></a>
                </li>
                <li>
                  <a href="#"><i class="fa fa-dribbble"></i></a>
                </li>
                <li>
                  <a href="#"><i class="fa fa-rss"></i></a>
                </li>
              </ul>
            </div>
            <div class="copyright-text">
              <p>Copyright 2022 Christian®<br>
              Design: by Christian Blanco</p>
            </div>
          </div>
        </div>
      </div>

      <section class="section about-me" data-section="section1">
        <div class="container">
        <div class="top-header">
        	<img src="assets/images/aerobic-girls.jpg" alt="aerobic girls" />
        </div>
          <div class="section-heading">
          
            <h2>Sobre Nosotros</h2>
            <div class="line-dec"></div>
            <span>Somos una agencia creativa estratégica de propiedad independiente, siempre curiosa y lista para transformar la forma en que se hacen los negocios. Aunque somos una máquina bien engrasada, nuestra gente está lejos de ser engranajes. El talento que cultivamos adquiere la importancia de perfeccionar sus respectivos oficios. Ayuda a servir mejor tanto a los demás como a nuestros socios, y se nota en todo, desde lo que diseñamos y producimos, hasta lo que valoramos y creemos.</span>
          </div>
          <div class="right-image-post">
            <div class="row">
 
              <div class="col-md-8">
                <div class="left-text">
                  <h4>Web Design</h4>
                  <p>No importa Estamos demasiado ocupados pensando más allá de las limitaciones del resumen típico. Creatividad: es lo que nos impulsa. Hacemos nuestro mejor trabajo cuando las barandillas están bajas y podemos extender nuestras alas. Los diseños son más limpios, las estrategias más nítidas y, en general, el mundo se convierte en un lugar mejor.</p>
                  <p>También creemos que los grandes productos pueden venir de cualquier parte. Por lo tanto, alentamos a nuestro equipo a relajarse, estirar las piernas y explorar espacios de trabajo alternativos.
                  </p>
                  
                </div>
              </div>
              <div class="col-md-4">
                <div class="right-image">
                  <img src="assets/images/mountain-reflection.jpg" alt="Mountain Reflection" />
                </div>
              </div>
              
            </div>
          </div>
          <div class="left-image-post">
            <div class="row">
            
              <div class="col-md-4">
                <div class="left-image">
                  <img src="assets/images/girl-nature.jpg" alt="Nature Girl" />
                </div>
              </div>
              
              <div class="col-md-8">
                <div class="right-text">
                  <h4>Consultores Creativos</h4>
                  <p>Brindamos asesoramiento estratégico y experiencia en marcas, marketing y comunicaciones para ayudar a las empresas inteligentes a lanzarse, transformarse, conectarse y prosperar.</p>
                  <p>“Recomiendo Alto a cualquiera que busque un excelente socio de comunicación estratégica y branding”
                    Jefe de Marketing de ASQA</p>
                </div>
              </div>
              
            </div>
          </div>
        </div>
      </section>

      <section class="section my-services" data-section="section2">
        <div class="container">
          <div class="section-heading">
            <h2>Tabla de Ganancias</h2>
            <div class="line-dec"></div>
            <span>En la siguiente se presentan cada una de las ganancias del mes.</span>
          </div> 
          <TABLE align="center" border=solid>
            <TR align="center">
                <TH>Producto</TH>
                <TH>Precio</TH>
                <TH>Cantidad</TH>
                <TH>Total Ganancias</TH>
            </TR>"""
    
    f.write(mensaje)

    for q in range(len(ArrayAuxiliar)):
        j = f"""
                <TR ALIGN=center>
                <TD ALIGN="center">{ArrayAuxiliar[q][0]}</TD>
                <TD ALIGN="center">{ArrayAuxiliar[q][1]}</TD>
                <TD ALIGN="center">{ArrayAuxiliar[q][2]}</TD>
                <TD ALIGN="center">{ArrayAuxiliar[q][1]*ArrayAuxiliar[q][2]}</TD>
            </TR>"""
        f.write(j)

    k = """
        </TABLE>
        </div>
      </section>

      <section class="section contact-me" data-section="section4">
        <div class="container">
          <div class="section-heading">
            <h2>Contactanos</h2>
            <div class="line-dec"></div>
            <span>Para mayor información y resolución sobre tus dudas. </span>
          </div>
          <div class="row">
            <div class="right-content">
              <div class="container">
                <form id="contact" action="" method="post">
                  <div class="row">
                    <div class="col-md-6">
                      <fieldset>
                        <input name="name" type="text" class="form-control"
                          id="name" placeholder="Your name..." required="" />
                      </fieldset>
                    </div>
                    <div class="col-md-6">
                      <fieldset>
                        <input name="email" type="text" class="form-control"
                          id="email" placeholder="Your email..." required=""  />
                      </fieldset>
                    </div>
                    <div class="col-md-12">
                      <fieldset>
                        <input name="subject" type="text" class="form-control" 
                          id="subject" placeholder="Subject..." required="" />
                      </fieldset>
                    </div>
                    <div class="col-md-12">
                      <fieldset>
                        <textarea name="message" rows="6" class="form-control"
                          id="message" placeholder="Your message..." required="" ></textarea>
                      </fieldset>
                    </div>
                    <div class="col-md-12">
                      <fieldset>
                        <button type="submit" id="form-submit" class="button">
                          Enviar Mensaje
                        </button>
                      </fieldset>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
    <!-- Scripts -->
    <!-- Bootstrap core JavaScript -->
    <script src="vendor/jquery/jquery.min.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

    <script src="assets/js/isotope.min.js"></script>
    <script src="assets/js/owl-carousel.js"></script>
    <script src="assets/js/lightbox.js"></script>
    <script src="assets/js/custom.js"></script>
    <script>
      //according to loftblog tut
      $(".main-menu li:first").addClass("active");

      var showSection = function showSection(section, isAnimate) {
        var direction = section.replace(/#/, ""),
          reqSection = $(".section").filter(
            '[data-section="' + direction + '"]'
          ),
          reqSectionPos = reqSection.offset().top - 0;

        if (isAnimate) {
          $("body, html").animate(
            {
              scrollTop: reqSectionPos
            },
            800
          );
        } else {
          $("body, html").scrollTop(reqSectionPos);
        }
      };

      var checkSection = function checkSection() {
        $(".section").each(function() {
          var $this = $(this),
            topEdge = $this.offset().top - 80,
            bottomEdge = topEdge + $this.height(),
            wScroll = $(window).scrollTop();
          if (topEdge < wScroll && bottomEdge > wScroll) {
            var currentId = $this.data("section"),
              reqLink = $("a").filter("[href*=\\#" + currentId + "]");
            reqLink
              .closest("li")
              .addClass("active")
              .siblings()
              .removeClass("active");
          }
        });
      };

      $(".main-menu").on("click", "a", function(e) {
        e.preventDefault();
        showSection($(this).attr("href"), true);
      });

      $(window).scroll(function() {
        checkSection();
      });
    </script>
  </body>
</html>
    """

    f.write(k)
    f.close()
    webbrowser.open_new_tab("index.html")
    print("Reporte impreso")


def Salir():
    print("\nEsperamos vuelva pronto. Con cuidado!\n")
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
    Reportes()
    Menu()
if opcion == 5:
    Salir()
if opcion <= 0 or opcion >= 6:
    print("Error, ingrese un número del menú.\n")
    Menu()
else:
    print("Ocurrio un error")
