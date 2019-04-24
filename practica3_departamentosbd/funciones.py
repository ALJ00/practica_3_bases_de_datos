import csv
from datetime import datetime, timedelta
from clases import *
from os import system
from fpdf import FPDF, fpdf
import fitz
import os
import PyPDF2
import pymysql
from time import *
import time
import random
from datetime import datetime
import shutil


# Funcion que muestra al usuario el menu principal
def mostrar_menu_principal():
    print("---------------------------------------------------")
    print("           Bienvenido al menú principal            ")
    print("---------------------------------------------------")
    print("Selecciona opción:\n"
          "a) Servicio post-venta\n"
          "b) Ventas - Tienda\n"
          "c) Administración\n"
          "d) Taller\n"
          "e) Marketing\n"
          "f) Salir del sistema")
    opcion = input("Opción: ")
    return opcion


# Funcion que se encarga de dar de alta un nuevo usuario en el sistema
def altaUsuario(usuario, password):
    u = usuario
    p = password

    dep = opcionDepartamento()

    user = UsuarioBd(u, p, dep)

    insertarUsuarioBD(user)

    ''' 
    # Controlo que usuario y password no vengan vacíos.
    if len(usuario) < 5 or len(password) < 5:
        print("Error, el usuario y la contraseña deben contener mínimo 5 caracteres.")
    else:
        # Variables de control
        a = 0
        b = 0

        # Cargo el fichero csv y lo recupero en una lista
        usuarios = leer_csv("usuarios.csv")

        for row in usuarios:
            # Contabilizo
            if usuario in row:
                a += 1
            elif password in row:
                b += 1

        if a > 0:
            print("Usuario existente")

        elif b > 0:
            print("Contraseña existente")
        else:
            fields = [u, p]
            with open("usuarios.csv", "a+", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(fields)

           

            print("Usuario dado de alta en el sistema correctamente")
    '''


# Funcion principal sistema_rp
def sistema_erp():
    # Mientras sea True no se saldra del bucle While
    while True:
        # Muestro el menu y cojo el operando retornado por la funcion mostrar_menu_principal() que es quien interactua
        # con el usuario
        operando = mostrar_menu_principal()

        # Compruebo las diferentes opciones y en cada opcion se llama a la funcion correspondiente
        # quien se encarga de abrir el menú del módulo.
        if operando == "a":

            # Compruebo credenciales de usuario
            if menu_verificacion_usuario_contrasenya():

                opcionMenuPostVenta()

        elif operando == "b":

            # Compruebo credenciales de usuario
            if menu_verificacion_usuario_contrasenya():
                usuario = "ventas"

                opcionMenuVentas(usuario)

        elif operando == "c":

            # Compruebo credenciales de usuario
            u = input("Usuario: ")
            c = input("Contraseña: ")
            if u == "admin" and c == "admin":
                print("Credenciales de ADMINISTRADOR correctas")
                opcionMenuAdministracion()
            else:
                print("Credenciales de ADMINISTRADOR INCORRECTAS")

        elif operando == "d":

            # Compruebo credenciales de usuario
            if menu_verificacion_usuario_contrasenya():

                usuario = "taller"
                opcion_menu_taller(usuario)

        elif operando == "e":

            # Compruebo credenciales de usuario
            if menu_verificacion_usuario_contrasenya():
                opcionMenuMarketing()

        elif operando == "f":
            print("Agur, mila esker...")
            break
        # En caso de introducir un dato erroneo se retorna al inicio del bucle
        else:
            input("Error, seleccione una opción correcta, pulsa INTRO/RETURN  para continuar... ")


# Funcion que muestra el menu gestion de usuarios y devuelve una opcion
def mostrarSubmenuGestionUsuarios():
    mi_string = color.BLUE + " Submenú gestión de usuarios ".capitalize().upper() + color.END
    print(mi_string.center(50, "="))
    print("Selecciona opción:\n"
          "a) Ver facturas vinculadas a un usuario\n"
          "b) Mostrar usuarios\n"
          "c) Salir del submenú")
    opcion = input("Opción: ")
    return opcion


# Funcion para mostrar opciones del menu usuario
def opcionSubmenuGestionUsuarios():
    while True:

        # Recojo el operando seleccionado
        operando = mostrarSubmenuGestionUsuarios()

        # Si es a muestro las facturas emitidas por un usuario
        if operando == "a":

            u = input("Usuario: ")
            #c = input("Password: ")

            # alta en csv
            # altaUsuario(u, c)

            # recojo el departamento
            #dep = opcionDepartamento()

            # creo un objeto UsarioBd
            #nuevoUusario = UsuarioBd(u, c, dep)

            # lo inseto en la Bd
            #insertarUsuarioBD(nuevoUusario)

            if comprobarUsuario(u):
                verFacturasDeUsuario(u)



        # Si es b, muestro los usuarios de la bd
        elif operando == "b":
            recuperarUsuariosBd()
            '''#user = input("Usuario: ")
            # eliminarUsuarioBd(user)'''


        # Si es la opcion c muestro todos los usuarios
        #elif operando == "c":
         #   list = leer_csv("usuarios.csv")
          #  for i in list:
           #     print("Usuario: " + i[0], " Contraseña: " + i[1])

            #recuperarUsuariosBd()


        # Si es la opcion c salgo del menu
        elif operando == "c":
            break

        # En caso de introducir un dato erroneo se retorna al inicio del bucle
        else:
            input("Error, seleccione una opción correcta, pulsa INTRO/RETURN  para continuar... ")


# Funcion que muestra el menu de compras
def mostrar_menu_postVenta():
    mi_string = color.RED + " Menú Servicio Post-Venta ".capitalize().upper() + color.END
    print(mi_string.center(50, "="))
    print("Selecciona opción:\n"
          "a) Mostrar listado de devoluciones\n"
          "b) Mostrar información de devolución\n"
          "c) Borrar devolución\n"
          "d) Generar orden de devolución proveedor\n"
          "e) Salir del menú")
    opcion = input("Opción: ")
    return opcion

# Funcion que muestra el menu de ventas
def mostrar_menu_ventas():
    mi_string = color.RED + " Menú ventas ".capitalize().upper() + color.END
    print(mi_string.center(50, "="))
    print("Selecciona opción:\n"
          "a) Nuevo venta\n"
          "b) Generar orden de reparación\n"
          "c) Mostrar ventas\n"
          "d) Generar devolución\n"
          "e) Mostrar clientes\n"
          "f) Salir del menú")
    opcion = input("Opción: ")
    return opcion

# Funcion que muestra el menu de RRHH
def mostrar_menu_Administracion():
    mi_string = color.RED + " Menú administración ".capitalize().upper() + color.END
    print(mi_string.center(50, "="))
    print("Selecciona opción:\n"
          "a) Contabilizar facturas\n"
          "b) Crear oferta de trabajo\n"
          "c) Gestión de usuarios\n"
          "d) Mostrar facturas activas\n"
          "e) Salir del menú")
    opcion = input("Opción: ")
    return opcion

# Funcion que muestra el menu de taller y devuelve la opcion seleccionada del menu
def mostar_menu_taller():
    mi_string = color.RED + " Menú taller ".capitalize().upper() + color.END
    print(mi_string.center(50, "="))
    print("Selecciona opción:\n"
          "a) Nueva orden de reparación\n"
          "b) Borrar reparación\n"
          "c) Listado de reparaciones\n"
          "d) Ver factura de reparación\n"
          "e) Salir del menú")
    opcion = input("Opción: ")
    return opcion

# Funcion que muestra el menu de marketing
def mostrar_menu_marketing():
    mi_string = color.RED + " Menú marketing ".capitalize().upper() + color.END
    print(mi_string.center(50, "="))
    print("Selecciona opción:\n"
          "a) Generar oferta\n"
          "b) Borrar oferta\n"
          "c) Mostrar contactos\n"
          "d) Crear contacto\n"
          "e) Salir del menú")
    opcion = input("Opción: ")
    return opcion

# Funcion que gestiona las opciones del menu taller
def opcion_menu_taller(usuario):
    while True:
        operando = mostar_menu_taller()
        # Compruebo las diferentes opciones y en cada una de ellas se realiza la función correspondiente
        if operando == "a":
            generar_orden_de_reparacion(usuario)
        elif operando == "b":
            numero = str(input("Introduzca orden de reparación a buscar: "))

            # borro el archivo de la carpeta reparaciones
            borrarOrdenTaller(numero)

            # borro la factura de la bd
            borrarReparacionBd(numero)

        elif operando == "c":
            listado_reparaciones()
        elif operando == "d":
            numero = input("Introduzca orden de reparación a visualizar: ")
            buscarOrden(numero)

        elif operando == "e":
            break
        # En caso de introducir un dato erroneo se retorna al inicio del bucle
        else:
            input("Error, seleccione una opción correcta, pulsa INTRO/RETURN  para continuar... ")

# Funcion para comprobar si usuarioe y password son correctos
def verificacion_usuario_contrasenya(usuario, password):
    # Variables de control
    verificacion = False
    user = 0
    contra = 0
    # Cargo el fichero csv y lo recupero en una lista
    with open('usuarios.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:

            # Contabilizo
            if usuario in row and password in row:
                user += 1
                contra += 1
    if user > 0 and contra > 0:
        print("Usuario y contraseña correctos")
        verificacion = True
    else:
        print("Error, usuario o contraseña incorrectos")

    return verificacion

# Funcion que muestra el menu usuario contrasenya para que el usuario se loguee tb con Bd
def menu_verificacion_usuario_contrasenya():
    print("Usuario y contraseña ---->")
    user = input("Usuario: ")
    pas = input("Password: ")
    dep = opcionDepartamento()

    # Guardo el valor que me retorna la funcion verificacion_usuario_contrasenya()
    # verificacion = verificacion_usuario_contrasenya(user, pas)

    verificacion = comprobarUsuarioContrasenyaBd(user, pas, dep)

    return verificacion

# Funcion que crea una orden de reparacion
def generar_orden_de_reparacion(usuario):
    diccionario = []

    control = "s"

    dep = "ta"

    cabeza = "Orden de reparación"

    while True:

        if control == "s":

            producto = input("Detalle de la reparación: ")
            importe = input("Importe: ")

            observacion = comprobar_numero_usuario(importe)

            if producto == "" or observacion == "":
                print("Error, debe introducir datos")
            else:

                linea = [producto, observacion]
                diccionario.append(linea)

                control = input("Nueva línea de reparación (s/n) ?")

        elif control == "n":

            print("Generando orden de reparación ------>")

            name = input("¿ Nuevo cliente? s/n: ")

            if name == "n":

                try:
                    d = str(input("Introduzca el dni: "))

                    cl = comprobarSiExisteClienteYrecuperarlo(d)

                    fact = Factura(diccionario, cl, dep, dep, cabeza)

                    generarFacturaPdf(fact, "reparaciones", usuario)

                    break

                except:
                    print("Error, revise los datos.")


            elif name == "s":

                # Datos
                name = input("Nombre cliente: ")
                telefono = input("Teléfono: ")
                fecha = time.strftime("%d/%m/%y")
                mail = input("E-mail: ")
                dni = str(input("Dni sin letra:"))

                if name == "" or telefono == "" or mail == "" or dni == "":
                    print("Error, inserte todos los datos")
                else:
                    cabecera = [fecha, name, telefono, mail]

                    # Creo un nuevo contacto para el departamento de marketing
                    contacto = [name, telefono, mail]
                    generarContacto(contacto)

                    d = ClienteBd(name, telefono, mail, dni)

                    insertarClienteBD(d)

                    fact = Factura(diccionario, d, dep, dep, cabeza)

                    generarFacturaPdf(fact, "reparaciones", usuario)

                    '''
                    ultNum = int(ultimoNumeroOrdenReparacion())

                    mi_fichero = open("reparaciones/" + "orden" + str(ultNum + 1) + ".csv", "w", newline="")

                    diccionario.append(cabecera)

                    with mi_fichero:
                        writer = csv.writer(mi_fichero)
                        writer.writerows(diccionario)

                    print("Creada correctamente orden de reparación nº {}".format(str(ultNum + 1)))
                    '''

                    break

            else:
                print("Error, introduzca s/n")
                break

        else:
            control = input("Error, introduzca un dato correcto: (s/n)")

# Funcion que lee archivo csv y devuelve una lista da datos
def leer_csv(archivoLeer):
    datos = []
    with open(archivoLeer, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            datos.append(row)
    return datos

# Funcion que escribe un archivo csv
def escribir_csv(datos):
    lista = datos
    with open('usuarios.csv', 'w+', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(lista)

# Funcion para eliminar las ordenes de reparacion
def borrar_reparacion(numero):
    # Cargo el archivo
    archivo = "reparaciones/" + "orden" + numero + ".csv"

    try:
        # Elimino el archivo
        os.remove(archivo)
        print("Eliminida orden de reparación.")
    except IOError:
        print("Archivo no encontrado")

# Funcion que muestra una lista de reparaciones
def listado_reparaciones():
    rootDir = '.'
    for dirName, subdirList, fileList in os.walk(rootDir):
        if "reparaciones" in dirName:
            print("Lista de {}: ".format("repaciones"))
            for fname in fileList:
                print('\t%s' % fname)

# Función que me genera una nueva factura tras recibir una orden de reparación
def generarFacturaTaller(orden):
    try:
        # Busco la orden
        archivo = "reparaciones/" + "orden" + orden + ".csv"

        # Leo el archivo y creo una lista de datos
        datos = leer_csv(archivo)

        # Pido el importe de la factura
        importe = input("Importe factura: ")
        comprobar_numero_usuario(importe)
        cabecera = [importe]

        # Obtengo el numero de la ultima factura
        num = int(ultimoNumeroFactura())

        datos.append(cabecera)

        try:
            # Elimino el archivo
            os.remove(archivo)

            with open("facturas/" + "factura" + str(num + 1) + ".csv", 'w+', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(datos)
            print("Creada correctamente factura nº {}".format(str(num + 1)))

        except IOError:

            print("Orden de reparación no encontrada")

    except IOError:
        print("Orden de reparación no encontrada")

# Funcion que genera una factura de venta
def generarFacturaVenta(usuario):
    # diccionario de lineas de factura
    diccionario = []
    control = "s"
    totalFactura = 0

    depar = "ve"

    cabeza = "Factura de venta"

    while True:

        if control == "s":

            producto = input("Producto: ")

            if producto == "":
                print("Error, revise los datos")
            else:
                valor = input("Importe: ")

                importe = comprobar_numero_usuario(valor)

                totalFactura += importe

                # linea de factura/pedido con su nombre o descripcion e importe
                linea = [producto, importe]

                # añado al diccionario de lineas de factura la linea
                diccionario.append(linea)

                control = input("Nuevo producto (s/n) ?")

        elif control == "n":

            print("Generando factura de venta ------>")

            consulta = input("¿Nuevo cliente? si/no")

            cl = None
            tel = None
            ml = None
            di = None

            fecha = time.strftime("%d/%m/%y")

            if consulta == "si":

                # Datos de cliente de la factura
                cliente = input("Nombre cliente: ")
                telefono = input("Teléfono: ")
                mail = input("E-mail: ")
                d = str(input("Dni (sin letra): "))

                if cliente == "" or telefono == "" or mail == "" or d == "":

                    print("Error, datos vacíos.")

                else:
                    cabecera = [fecha, cliente, telefono, mail, str(totalFactura)]

                    # Creo un nuevo contacto para el departamento de marketing
                    contacto = [cliente, telefono, mail]
                    generarContacto(contacto)

                    # Creo objeto Cliente
                    c = ClienteBd(cliente, telefono, mail, d)

                    # Inserto en la BD el cliente
                    insertarClienteBD(c)

                    # Obtengo el ultimo numero de la factura
                    # ultNum = int(ultimoNumeroFactura())

                    factura = Factura(diccionario, c, depar, depar, cabeza)


                    generarFacturaPdf(factura, "facturas", usuario)


                    # codigo para generar factura csv
                    '''mi_fichero = open("facturas/" + "factura" + str(ultNum + 1) + ".csv", "w+", newline="")
                    diccionario.append(cabecera)
                    with mi_fichero:
                        writer = csv.writer(mi_fichero)
                        writer.writerows(diccionario)'''

                    # print("Creada correctamente facturaventa {}".format(str(ahora)))
                    break

            elif consulta == "no":

                documento = str(input("Introduzca el dni del cliente: "))

                try:

                    cli = comprobarSiExisteClienteYrecuperarlo(documento)

                    factura = Factura(diccionario, cli, depar, depar, cabeza)

                    generarFacturaPdf(factura, "facturas", usuario)

                    break

                except:
                    print("Revise los datos")


            else:
                print("Introduzca si/no ")
                break


        else:
            control = input("Error, introduzca un dato correcto: (s/n)")

# Funcion para comprobar que el dato introducido por el usuario sea un numero
def comprobar_numero_usuario(numero):
    while True:
        num = None
        for conv in (int, float, complex):
            try:
                num = conv(numero)
                break
            except ValueError:
                pass
        if num is None:
            numero = input("Dato erróneo, inserte un numero:")
        else:
            return num
            break

# Funcion para distribuir las acciones del menu ventas
def opcionMenuVentas(usuario):
    while True:
        operando = mostrar_menu_ventas()
        # Compruebo las diferentes opciones y en cada una de ellas se realiza la función correspondiente
        if operando == "a":
            generarFacturaVenta(usuario)
        elif operando == "b":
            generar_orden_de_reparacion(usuario)
        elif operando == "c":
            listado_facturas()
        elif operando == "d":
            generarDevolucionBd()
        elif operando == "e":
            recuperarClientesBd()
        elif operando == "f":
            break
        # En caso de introducir un dato erroneo se retorna al inicio del bucle
        else:
            input("Error, seleccione una opción correcta, pulsa INTRO/RETURN  para continuar... ")

# Funcion para mostrar la lista de facturas
def listado_facturas():
    rootDir = '.'
    for dirName, subdirList, fileList in os.walk(rootDir):
        if "facturas" in dirName:
            print("Lista de {}: ".format("todas las facturas"))
            for fname in fileList:
                print('\t%s' % fname)

# Funcion para generar facturaDevolucion
def generarDevolucion(orden):
    try:
        # Busco la orden
        archivo = "facturas/" + "factura" + orden + ".csv"

        # Leo el archivo y creo una lista de datos
        datos = leer_csv(archivo)

        # Elimino el archivo
        os.remove(archivo)

        with open("devoluciones/" + "facturaDevolucion" + orden + ".csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(datos)
        print("Creada correctamente facturaDevolución nº {}".format(orden))

    except IOError:

        print("Factura de venta no encontrada")

# Funcion que crea un nuevo contacto en archivo txt
def generarContacto(datos):
    try:
        f = open("marketing/directorioContactos/contactos.txt", 'a')
        f.write(str(datos) + "\n")
        f.close()

    except IOError:
        print("Archivo no encontrado")

# Funcion que genera un listado de contactos
def listado_contactos():
    contactos = []

    try:
        dirFichero = "marketing/directorioContactos/contactos.txt"
        with open(dirFichero, 'r', newline="") as reader:
            for line in reader:
                contactos.append(line)
        if len(contactos) == 0:
            print("No hay contactos registrados")
        else:
            for linea in contactos:
                print(linea, end="")


    except IOError:
        print("No existe un archivo de contactos")

    print("")

# Funcion para mostrar las opciones del menú Marketing
def opcionMenuMarketing():
    while True:
        operando = mostrar_menu_marketing()
        # Compruebo las diferentes opciones y en cada una de ellas se realiza la función correspondiente
        if operando == "a":
            # generarOferta()

            producto = input("Producto en oferta: ")
            descripcion = input("Descripción de oferta: ")
            descuento = input("Descuento:")

            if producto == "" or descripcion == "" or descuento == "":
                print("Datos vacíos, revise los datos")
            else:
                insertarOfertaVentaBD(producto, descripcion, descuento)


        elif operando == "b":
            num = input("Introduzca número de oferta a borrar: ")
            borrarOfertaMarketing(num)
        elif operando == "c":
            #listado_contactos()

            recuperarClientesBd()

        elif operando == "d":
            nombre = input("Nombre: ")
            telf = input("Teléfono: ")
            mail = input("Mail: ")
            dni = str(input("Dni: "))
            if nombre == "" or telf == "" or mail == "" or dni == "":
                print("Error, introduzca todos los datos")
            else:
                #datos = [nombre, telf, mail]
                #generarContacto(datos)

                c = ClienteBd(nombre,telf, mail, dni)

                insertarClienteBD(c)

                print("Generado contacto correctamente")

        elif operando == "e":
            break
        # En caso de introducir un dato erroneo se retorna al inicio del bucle
        else:
            input("Error, seleccione una opción correcta, pulsa INTRO/RETURN  para continuar... ")

# Funcion para generar una oferta
def generarOferta():
    fecha = time.strftime("%d/%m/%y")
    producto = input("Producto en oferta: ")
    descripcion = input("Descripción de oferta: ")
    descuento = input("Descuento:")

    comprobar_numero_usuario(descuento)

    lineaOferta = [fecha, producto, descripcion, descuento]

    if producto == "" or descripcion == "":
        print("Error, revise los datos")
    else:

        n = int(ultimo_numero_oferta())

        dirFichero = 'marketing/ofertas/oferta' + str(n + 1) + '.txt'
        fichero = open(dirFichero, 'w')
        for l in lineaOferta:
            fichero.write(l + ",")
        fichero.close()
        print("Creada la oferta nº{} correctamente".format(str(n + 1)))

# Funcion que cuenta las ofertas activas que hay en el sistema
def contarOfertas():
    try:
        lista = []
        rootDir = '.'
        for dirName, subdirList, fileList in os.walk(rootDir):
            if "ofertas" in dirName:

                for fname in fileList:
                    lista.append(fname)

        numeroOfertas = len(lista)

        return numeroOfertas

    except IOError:
        print("No existe un archivo de contactos")

# Funcion para eliminar ofertas
def borrar_oferta(numero):
    # Cargo el archivo
    archivo = "marketing/ofertas/" + "oferta" + numero + ".txt"

    try:
        # Elimino el archivo
        os.remove(archivo)
        print("Eliminida oferta correctamente.")
    except IOError:
        print("Archivo no encontrado")

# Funcion para obtener el ultimo numero del archiv(ofertas, facturas ..) para poner numero al nuevo archivo
def ultimo_numero_oferta():
    try:
        lista = []
        rootDir = '.'
        for dirName, subdirList, fileList in os.walk(rootDir):
            if "ofertas" in dirName:

                for fname in fileList:
                    lista.append(fname)

        # Cuantos archivos hay
        numeroOfertas = len(lista)

        if numeroOfertas == 0:

            return 0

        else:
            # Cojo el ultimo
            ultimo_archivo = str(lista[numeroOfertas - 1])

            # Le doy la vuelta
            ultimo_archivo_reves = list(reversed(ultimo_archivo))

            # Preparo el dato
            dato = ""

            # Busco el numero de archivo
            for i in range(len(ultimo_archivo_reves)):
                if i == 4:
                    dato = ultimo_archivo_reves[i]

            # Retorno que numero tiene la ultima oferta
            return dato




    except IOError:
        print("No existe un archivo de ofertas")

# Funcion que devuelve el nuemero de la ultima factura
def ultimoNumeroFactura():
    try:
        lista = []
        rootDir = '.'
        for dirName, subdirList, fileList in os.walk(rootDir):
            if "facturas" in dirName:

                for fname in fileList:
                    lista.append(fname)

        # Cuantos archivos hay
        numeroFactura = len(lista)

        if numeroFactura == 0:

            return 0
        else:

            # Cojo el ultimo
            ultimo_archivo = str(lista[numeroFactura - 1])

            # Le doy la vuelta
            ultimo_archivo_reves = list(reversed(ultimo_archivo))

            # Preparo el dato
            dato = ""

            # Busco el numero de archivo
            for i in range(len(ultimo_archivo_reves)):
                if i == 4:
                    dato = ultimo_archivo_reves[i]

            # Retorno que numero tiene la ultima oferta
            return dato


    except IOError:
        print("No existe un archivo de contactos")

# Funcion que devuelve el numero de la ultima orden de reparacion
def ultimoNumeroOrdenReparacion():
    try:
        lista = []
        rootDir = '.'
        for dirName, subdirList, fileList in os.walk(rootDir):
            if "reparaciones" in dirName:

                for fname in fileList:
                    lista.append(fname)

        # Cuantos archivos hay
        numeroReparacion = len(lista)

        if numeroReparacion == 0:

            return 0

        else:

            # Cojo el ultimo
            ultimo_archivo = str(lista[numeroReparacion - 1])

            # Le doy la vuelta
            ultimo_archivo_reves = list(reversed(ultimo_archivo))

            # Preparo el dato
            dato = ""

            # Busco el numero de archivo
            for i in range(len(ultimo_archivo_reves)):
                if i == 4:
                    dato = ultimo_archivo_reves[i]

            # Retorno que numero tiene la ultima oferta
            return dato


    except IOError:
        print("No existe un archivo de contactos")

# Funcion para mostrar opciones del menu postVenta
def opcionMenuPostVenta():
    while True:

        operando = mostrar_menu_postVenta()

        # Compruebo las diferentes opciones y en cada una de ellas se realiza la función correspondiente
        if operando == "a":
            mostrarDevoluciones()
        elif operando == "b":

            num = str(input("Introduce el número de devolución a mostrar: "))
            verDevolucion(num)

        elif operando == "c":
            numero = str(input("Introduzca número de devolución a borrar: "))

            borrarDevolucionBd(numero)

            borrarDevolucionPdf(numero)



        elif operando == "d":

            generarDevolucionBd()

        elif operando == "e":
            break

        # En caso de introducir un dato erroneo se retorna al inicio del bucle
        else:
            input("Error, seleccione una opción correcta, pulsa INTRO/RETURN  para continuar... ")

# Funcion que muestra las devoluciones
def mostrarDevoluciones():
    rootDir = '.'
    for dirName, subdirList, fileList in os.walk(rootDir):
        if "devoluciones" in dirName:
            print("Lista de {}: ".format("devoluciones"))
            for fname in fileList:
                print('\t%s' % fname)

# Funcion para eliminar devoluciones
def borrarDevolucion(numero):
    # Cargo el archivo
    archivo = "devoluciones/" + "facturaDevolucion" + numero + ".csv"
    try:
        # Elimino el archivo
        os.remove(archivo)
        print("Eliminida devolución correctamente.")
    except IOError:
        print("Archivo no encontrado")

# Funcion que extrae lainformacion de una devolucion concreta
def obtenerInfoDevolucion(numero):
    try:
        # Cargo el archivo
        archivo = "devoluciones/" + "facturaDevolucion" + numero + ".csv"

        # Leo el archivo csv y cargo los datos en una variable
        datos = leer_csv(archivo)

        print("------- Información de facturaDevolución {}".format(numero) + " --------")

        for i in datos:
            if len(i) == 2:
                print("Producto: " + i[0], " Precio: " + i[1])
            elif len(i) == 5:
                print("Fecha: " + i[0], " Nombre: " + i[1], " Móvil: " + i[2], " Mail: " + i[3], " Total: " + i[4])


    except IOError:
        print("Archivo no encontrado")

    print("")

# Funcion para generar facturaDevolucionProveedor
def generarDevolucionProveedor(orden):
    try:
        # Busco la orden
        archivo = "devoluciones/" + "facturaDevolucion" + orden + ".csv"

        # Leo el archivo y creo una lista de datos
        datos = leer_csv(archivo)

        # Elimino el archivo
        os.remove(archivo)

        with open("reclamacionesProveedores/" + "facturaDevolucionProveedor" + orden + ".csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(datos)
        print("Creada correctamente facturaDevoluciónProveedor nº {}".format(orden))

    except IOError:

        print("Factura no encontrada")

# Funcion para distribuir las acciones del menu Administracion
def opcionMenuAdministracion():
    while True:
        operando = mostrar_menu_Administracion()
        # Compruebo las diferentes opciones y en cada una de ellas se realiza la función correspondiente
        if operando == "a":
            # n = input("Introduce el número de factura a contabilizar: ")
            # buscarFacturaYcontabilizar(n)
            generarContabilizacionFacturaBd()

        elif operando == "b":
            generarOfertaTrabajo()
        elif operando == "c":
            opcionSubmenuGestionUsuarios()
        elif operando == "d":
            listado_facturas()
        elif operando == "e":
            break
        # En caso de introducir un dato erroneo se retorna al inicio del bucle
        else:
            input("Error, seleccione una opción correcta, pulsa INTRO/RETURN  para continuar... ")

# Funcion para generar una oferta de trabajo
def generarOfertaTrabajo():
    fecha = time.strftime("%d/%m/%y")
    puesto = input("Puesto de trabajo: ")
    descripcion = input("Descripción de oferta: ")
    remuneracion = input("Remuneración: ")

    comprobar_numero_usuario(remuneracion)

    lineaOferta = [fecha, puesto, descripcion, remuneracion]

    if puesto == "" or descripcion == "":
        print("Error, revise los datos")
    else:

        n = int(ultimo_numero_oferta())

        dirFichero = 'administracion/empleo/ofertaEmpleo' + puesto + '.txt'
        fichero = open(dirFichero, 'w')
        for l in lineaOferta:
            fichero.write(l + ",")
        fichero.close()
        print("Creada la oferta de empleo {} correctamente".format(puesto))

# Funcion que busca una factura
def buscarFacturaYcontabilizar(numero):
    try:
        # Cargo el archivo
        archivo = "facturas/" + "factura" + numero + ".csv"

        # Leo el archivo csv y cargo los datos en una variable
        datos = leer_csv(archivo)

        # Variables para el rellenar el csv
        iT = ""
        f = ""
        c = ""

        # Cargo los datos correspondientes
        for i in datos:
            if len(i) == 5:
                iT = i[4]
                f = i[0]
                c = i[1]
            elif len(i) == 4:
                f = i[0]
                c = i[1]
            elif len(i) == 1:
                iT = i[0]

        # Cargo el archivo
        with open('contabilidad/detalleAsientos.csv', 'a', newline="") as csvfichero:
            campos = ['4309 CLIENTES FACTURAS PENDIENTES DE FORMALIZAR', 'numeroFactura', 'fecha', 'importe']
            writer = csv.DictWriter(csvfichero, fieldnames=campos)

            # Insertos los nuevos datos
            writer.writerow({'4309 CLIENTES FACTURAS PENDIENTES DE FORMALIZAR': c, 'numeroFactura': numero, 'fecha': f,
                             'importe': iT})

        # Elimino la factura
        os.remove(archivo)

        print("Factura contabilizada correctamente")
    except IOError:
        print("Factura no encontrada")

# Funcion que genera una factura en pdf
def generarFacturaPdf(Factura, directorio, usuario):

    aleatorio = str(random.randint(0, 10000))
    now = datetime.now()

    # accedo a los datos de la factura
    bild = Factura
    c = bild.client
    totalFactura = 0
    date = bild.fecha
    d = bild.lineas
    codigo = bild.cod + aleatorio + strftime("%b") + str(now.year)
    enunciado = bild.head
    documentoDni = c.dni

    strftime("%b")

    pdf = FPDF()
    pdf.add_page(orientation='P')
    pdf.set_font('arial', '', 13.0)

    pdf.set_xy(105.0, 8.0)
    pdf.cell(ln=0, h=22.0, align='C', w=75.0, txt=enunciado, border=0)
    pdf.set_line_width(0.0)
    pdf.rect(15.0, 15.0, 170.0, 245.0)
    pdf.set_line_width(0.0)
    pdf.rect(95.0, 15.0, 10.0, 10.0)

    # descomentar para poner imagen
    # pdf.image("BikeLogo.png", 10.0, 10.0, type="png", w=13.0, h=13.0)
    # pdf.image("BikeLogo.png", x=None, y=None, w=0, h=0, type='png', link='')

    pdf.set_font('arial', 'B', 16.0)
    pdf.set_xy(95.0, 18.0)
    pdf.cell(ln=0, h=2.0, align='C', w=10.0, txt='X', border=0)
    pdf.set_font('arial', '', 8.0)
    pdf.set_xy(105.0, 21.0)
    pdf.cell(ln=0, h=4.0, align='C', w=75.0, txt='Original', border=0)
    pdf.set_font('arial', 'B', 7.0)
    pdf.set_xy(95.0, 21.5)
    pdf.cell(ln=0, h=4.5, align='C', w=10.0, txt='COD.00', border=0)
    pdf.set_line_width(0.0)
    pdf.line(100.0, 25.0, 100.0, 57.0)
    pdf.set_font('arial', 'B', 14.0)
    pdf.set_xy(125.0, 25.5)
    pdf.cell(ln=0, h=9.5, align='L', w=60.0, txt=codigo, border=0)
    pdf.set_xy(115.0, 27.5)
    pdf.cell(ln=0, h=5.5, align='L', w=10.0, txt='N\xba: ', border=0)
    pdf.set_font('arial', 'B', 12.0)
    pdf.set_xy(17.0, 32.5)

    # confeccion zona datos empresa
    pdf.cell(ln=0, h=5.0, align='L', w=98.0, txt='BICICLETAS EGIBIDE', border=0)
    pdf.set_xy(17.0, 38.5)
    pdf.cell(ln=0, h=5.0, align='L', w=98.0, txt='C/Arriaga, 5 - bajo', border=0)
    pdf.set_xy(17.0, 44.5)
    pdf.cell(ln=0, h=5.0, align='L', w=98.0, txt='01001 - Vitoria-Gasteiz', border=0)
    pdf.set_xy(17.0, 50.5)
    pdf.cell(ln=0, h=5.0, align='L', w=98.0, txt='CIF: B-0125693', border=0)

    pdf.set_font('arial', '', 12.0)
    pdf.set_xy(115.0, 33.0)
    pdf.cell(ln=0, h=7.0, align='L', w=60.0, txt='Fecha:', border=0)
    pdf.set_xy(135.0, 33.0)
    pdf.cell(ln=0, h=7.0, align='L', w=40.0, txt=date, border=0)
    pdf.set_line_width(0.0)
    pdf.line(15.0, 57.0, 185.0, 57.0)
    pdf.set_font('arial', '', 10.0)
    pdf.set_xy(17.0, 59.0)
    pdf.cell(ln=0, h=6.0, align='L', w=13.0, txt='Sr.(s):', border=0)
    pdf.set_xy(35.0, 59.0)
    pdf.cell(ln=0, h=6.0, align='L', w=140.0, txt=c.nameClient, border=0)
    pdf.set_xy(17.0, 64.0)
    pdf.cell(ln=0, h=6.0, align='L', w=18.0, txt='Mail:', border=0)
    pdf.set_xy(35.0, 64.0)
    pdf.cell(ln=0, h=6.0, align='L', w=125.0, txt=c.email, border=0)
    pdf.set_xy(17.0, 69.0)
    pdf.cell(ln=0, h=6.0, align='L', w=18.0, txt='Tel\xe9fono:', border=0)
    pdf.set_xy(35.0, 69.0)
    pdf.cell(ln=0, h=6.0, align='L', w=80.0, txt=c.telefono, border=0)
    pdf.set_xy(115.0, 69.0)
    # pdf.cell(ln=0, h=6.0, align='L', w=18.0, txt='Localidad:', border=0)
    # pdf.set_xy(133.0, 69.0)
    # pdf.cell(ln=0, h=6.0, align='L', w=42.0, txt='Vitoria', border=0)
    pdf.set_line_width(0.0)
    pdf.line(15.0, 77.0, 185.0, 77.0)
    pdf.set_xy(17.0, 80.0)
    pdf.cell(ln=0, h=5.0, align='L', w=15.0, txt='', border=0)
    pdf.set_xy(35.0, 80.0)
    pdf.cell(ln=0, h=5.0, align='L', w=70.0, txt='', border=0)
    pdf.set_xy(115.0, 80.0)
    pdf.cell(ln=0, h=5.0, align='L', w=20.0, txt='', border=0)
    pdf.set_xy(135.0, 80.0)
    pdf.cell(ln=0, h=5.0, align='L', w=40.0, txt='', border=0)
    pdf.set_line_width(0.0)
    pdf.line(15.0, 88.0, 185.0, 88.0)
    pdf.set_xy(17.0, 90.0)
    pdf.cell(ln=0, h=5.0, align='L', w=48.0, txt='Fecha de Vencimiento Pago:', border=0)
    pdf.set_xy(65.0, 90.0)
    pdf.cell(ln=0, h=5.0, align='L', w=20.0, txt='', border=0)
    pdf.set_xy(92.0, 90.0)
    pdf.cell(ln=0, h=5.0, align='L', w=43.0, txt='Per\xedodo Facturado', border=0)
    pdf.set_xy(125.0, 90.0)
    pdf.cell(ln=0, h=5.0, align='L', w=20.0, txt=date, border=0)
    pdf.set_xy(150.0, 90.0)
    pdf.cell(ln=0, h=5.0, align='L', w=20.0, txt='', border=0)
    pdf.set_line_width(0.0)
    pdf.line(15.0, 95.0, 185.0, 95.0)
    pdf.set_line_width(0.0)
    pdf.line(155.0, 95.0, 155.0, 230.0)
    pdf.set_xy(20.0, 97.0)
    pdf.cell(ln=0, h=5.0, align='L', w=125.0, txt='Descripci\xf3n', border=0)
    pdf.set_xy(160.0, 97.0)
    pdf.cell(ln=0, h=5.0, align='R', w=20.0, txt='Importe', border=0)
    pdf.set_line_width(0.0)
    pdf.line(15.0, 102.0, 185.0, 102.0)

    posicion = 103.0

    posicionador = 1
    for i in d:
        # linea 1 factura posicion
        pdf.set_xy(20.0, posicion)
        pdf.cell(ln=0, h=7.0, align='L', w=125.0, txt=i[0], border=0)

        pdf.set_xy(160.0, posicion)
        pdf.cell(ln=0, h=7.0, align='R', w=20.0, txt=str(i[1]), border=0)

        totalFactura = totalFactura + i[1]

        posicion = posicion + 4.0

    # linea 2 posicion
    # .set_xy(20.0, 108.0)
    # pdf.cell(ln=0, h=7.0, align='L', w=125.0, txt='articulo 2', border=0)
    # posiciono donde voy a escribir el importe
    # pdf.set_xy(160.0, 108.0)
    # pdf.cell(ln=0, h=7.0, align='R', w=20.0, txt='200,00', border=0)

    pdf.set_line_width(0.0)
    pdf.line(15.0, 230.0, 185.0, 230.0)
    pdf.set_xy(20.0, 233.0)
    pdf.cell(ln=0, h=5.0, align='L', w=95.0, txt='CAE N\xba', border=0)
    pdf.set_xy(45.0, 233.0)
    pdf.cell(ln=0, h=5.0, align='L', w=30.0, txt='01234567890', border=0)
    pdf.set_font('arial', '', 12.0)
    pdf.set_xy(105.0, 234.0)
    pdf.cell(ln=0, h=9.0, align='R', w=45.0, txt='IMPORTE NETO:', border=0)
    pdf.set_font('arial', 'B', 12.0)
    pdf.set_xy(145.0, 234.0)
    pdf.cell(ln=0, h=9.0, align='R', w=33.0, txt=str(totalFactura), border=0)
    pdf.set_font('arial', '', 10.0)
    pdf.set_xy(20.0, 238.0)
    pdf.cell(ln=0, h=5.0, align='L', w=95.0, txt='Fecha Vto. CAE:', border=0)
    pdf.set_xy(55.0, 238.0)
    pdf.cell(ln=0, h=5.0, align='L', w=30.0, txt='', border=0)
    pdf.set_font('arial', '', 12.0)
    pdf.set_xy(125.0, 241.0)
    pdf.cell(ln=0, h=9.0, align='R', w=25.0, txt='IVA 21%:', border=0)
    pdf.set_font('arial', 'B', 12.0)
    pdf.set_xy(145.0, 241.0)
    pdf.cell(ln=0, h=9.0, align='R', w=33.0, txt='21,00', border=0)
    pdf.interleaved2of5('012345678905', 20.0, 243.5, w=0.75)
    pdf.set_font('arial', 'B', 12.0)
    pdf.set_xy(105.0, 251.0)
    pdf.cell(ln=0, h=9.0, align='R', w=73.0, txt=str(totalFactura + totalFactura * 0.21), border=0)
    pdf.set_font('arial', '', 12.0)
    pdf.set_xy(125.0, 251.0)
    pdf.cell(ln=0, h=9.0, align='R', w=25.0, txt='Total:', border=0)
    pdf.set_line_width(0.0)
    pdf.rect(155.0, 252.0, 25.0, 7.0)
    pdf.set_font('arial', '', 10.0)
    pdf.set_xy(20.0, 253.0)
    pdf.cell(ln=0, h=7.0, align='L', w=120.0, txt='012345678905', border=0)

    # guardo el documento en la ruta indicada
    pdf.output(".\\" + directorio + "\\" + codigo + ".pdf", "F")

    # muestro en pdf el documento generado
    os.system(".\\" + directorio + "\\" + codigo + ".pdf")

    if bild.dep == "ve":
        # inserto la factura de venta en bd
        insertarFacturaVentaBD(date, codigo, documentoDni, usuario)

    elif bild.dep == "ta":

        insertarFacturaTallerBD(date, codigo, documentoDni, usuario)

    print("Creada correctamente  {}".format(codigo))

# Funcion que muestra el menu de de opcion de departamento
def mostrar_menu_departamento():
    print("A qué departamento corresponde el usuario:\n"
          "a) Marketing\n"
          "b) Ventas/tienda\n"
          "c) Post-Venta\n"
          "d) Taller")
    opcion = input("Opción: ")
    return opcion

# funcion que muestra opcion de departamento
def opcionDepartamento():
    while True:

        departamento = None

        # recojo departamento
        opcion = mostrar_menu_departamento()

        if opcion == "a":
            departamento = "ma"

            return departamento
        elif opcion == "b":
            departamento = "ve"
            return departamento
        elif opcion == "c":
            departamento = "pv"
            return departamento
        elif opcion == "d":
            departamento = "ta"
            return departamento
        else:
            # En caso de introducir un dato erroneo se retorna al inicio del bucle
            print("Error, introduzca departamento correcto.")

# funcion para ver factura de reparacion en pdf
def verFacturaReparacion(numeroreparacion):
    # archivo = str(numeroreparacion)

    try:
        # muestro en pdf el documento generado
        os.system(".\\reparaciones\\" + numeroreparacion + ".pdf")

    except IOError as e:
        print("Numero de reparación incorrecto, introduzca dato correcto", e)

# funcion para buscar orden de reparacion
def buscarOrden(datoArchivo):
    busqueda = False

    # Cargo el archivo
    archivo = ".\\reparaciones\\" + datoArchivo + ".pdf"
    try:
        # os.remove(archivo)
        if os.path.isfile(archivo):

            verFacturaReparacion(datoArchivo)

        else:
            print("Introduzca archivo correcto")

    except IOError:
        print("Archivo no encontrado")
        # busqueda = False

    # return busqueda

# función que elimina el archivo de factura de reparacion
def borrarOrdenTaller(datoArchivo):
    # Cargo el archivo
    archivo = ".\\reparaciones\\" + datoArchivo + ".pdf"
    try:
        # Elimino el archivo
        os.remove(archivo)
        print("Eliminida factura de venta correctamente.")
    except IOError:
        print("Archivo no encontrado")

# funcion que copia un archivo
def copiarArchivo(documento, procedencia):
    fuente = ".\\" + procedencia + "\\" + documento + ".pdf"
    destino = ".\\devoluciones\\" + documento + ".pdf"

    shutil.copyfile(fuente, destino)

    print("Generada devolución correctamente")

    return True

# funcion para crear una devolucion
def generarDevolucionBd():
    opcion = input("¿ Devolución de reparaciones (a) o facturas de venta (b) ? :")

    if opcion == "a":

        ar = str(input("Introduzca numero de la factura: "))

        try:

            procedencia = "reparaciones"

            if copiarArchivo(ar, procedencia):

                insertarDevolucionBD(ar)

        except IOError:
            print("Error, revise los datos")


    elif opcion == "b":

        ar = str(input("Introduzca numero de la factura: "))

        try:

            procedencia = "facturas"

            insertarDevolucionBD(ar)

            copiarArchivo(ar, procedencia)



        except IOError:
            print("Error, revise los datos")


    else:
        print("Error, inserte a/b")

# funcion para ver el archivo pdf de la devolucion
def verDevolucion(archivo):
    try:

        # muestro en pdf el documento generado
        os.system(".\\devoluciones\\" + archivo + ".pdf")




    except IOError:
        print("Archivo no encontrado")

# funcion para borrar devolucion
def borrarDevolucionPdf(archivo):
    # Cargo el archivo
    archivo = ".\\devoluciones\\" + archivo + ".pdf"
    try:
        # Elimino el archivo
        os.remove(archivo)
        print("Eliminida devolución correctamente.")
    except IOError:
        print("Archivo no encontrado")

# funcion para generar contabilizacion
def generarContabilizacionFacturaBd():
    opcion = input("¿Contabilizar facturas de reparaciones (a) o de facturas de venta (b)? :")

    if opcion == "a":

        ar = str(input("Introduzca numero de la factura: "))

        try:

            procedencia = "reparaciones"

            contabilizarFaturaBd(ar)

            copiarArchivoAcontabilidad(ar, procedencia)



        except IOError:
            print("Error, revise los datos")


    elif opcion == "b":

        ar = str(input("Introduzca numero de la factura: "))

        try:

            procedencia = "facturas"

            contabilizarFaturaBd(ar)

            copiarArchivoAcontabilidad(ar, procedencia)

        except IOError:
            print("Error, revise los datos")



    else:
        print("Error, inserte a/b")

# funcion que copia el archivo para pegarlo en contabilidad
def copiarArchivoAcontabilidad(documento, procedencia):
    fuente = ".\\" + procedencia + "\\" + documento + ".pdf"
    destino = ".\\contabilidad\\" + documento + ".pdf"

    shutil.copyfile(fuente, destino)

    print("Generada contabilización correctamente")
