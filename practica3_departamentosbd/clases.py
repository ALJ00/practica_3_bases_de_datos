import pymysql
import time
from pymysql import Error
from datetime import datetime


# Clase para dar color al texto
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# clase que genera un objeto UsuarioBD
class UsuarioBd:

    def __init__(self, usuario, contrasenya, departamento):
        self.nameUser = usuario
        self.passUser = contrasenya
        self.depart = departamento

# clase que genera un objeto cliente
class ClienteBd:

    def __init__(self, name, phone, mail, document):
        self.nameClient = name
        self.telefono = phone
        self.email = mail
        self.dni = document

# clase que genera un objeto factura
class Factura():
    fecha = time.strftime('%x')

    def __init__(self, lineasFactura, Cliente, departamento, codigo, cabecera):
        self.client = Cliente
        self.lineas = lineasFactura
        self.codigoFactura = time.strftime('')
        self.dep = departamento
        self.cod = "factura" + codigo + self.codigoFactura
        self.head = cabecera

# clase que genera un objeto orden
class OrdenReparacion():
    fecha = time.strftime('%x')

    def __init__(self, lineasOrden, Cliente, departamento, codigo, cabecera):
        self.client = Cliente
        self.lineas = lineasOrden
        self.codigoFactura = time.strftime('')
        self.dep = departamento
        self.cod = "factura" + codigo + self.codigoFactura
        self.head = cabecera

# clase que genera un objeto linea
class LineaFactura():
    def __init__(self, producto, importe):
        self.nombreProducto = producto
        self.imp = importe

# funcion para insertar un usuario en la bd
def insertarUsuarioBD(usuario):
    try:

        # Conexión a base de datos
        db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)
        # Preparar el cursor
        cursor = db.cursor()
        # Consulta SQL para insertar datos de un empleado
        sql = "INSERT INTO usuarios(usuario, password, departamento) VALUES (%s, %s, %s)"
        val = (usuario.nameUser, usuario.passUser, usuario.depart)
        try:
            # Ejecutar el comando SQL
            cursor.execute(sql, val)
            # Aceptar cambios con commit
            db.commit()
            print("Usuario creado correctamente")
        except:
            print("Usuario o contraseña existentes")
            # Rollback en caso de haber algún error
            db.rollback()
            # Desconexión
        db.close()

    except Error as e:
        print("Error base de datos mysql", e)

# funcion para insertar un cliente en la bd
def insertarClienteBD(cliente):
    try:
        # Conexión a base de datos
        db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)
        # Preparar el cursor
        cursor = db.cursor()
        # Consulta SQL para insertar datos de un empleado
        sql = "INSERT INTO clientes(nombreCliente, telefono, mail, dni) VALUES (%s, %s, %s, %s)"
        val = (cliente.nameClient, cliente.telefono, cliente.email, cliente.dni)
        try:
            # Ejecutar el comando SQL
            cursor.execute(sql, val)
            # Aceptar cambios con commit
            db.commit()
        except:

            # Rollback en caso de haber algún error
            db.rollback()
            # Desconexión
        db.close()
    except Error as e:
        print("Error base de datos mysql", e)

# funcion para recuperar mostrar los clientes de la bd
def recuperarClientesBd():
    listClient = []

    try:

        # Conexión a base de datos
        db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)

        # Preparar el cursor
        cursor = db.cursor()

        sql = "SELECT * FROM clientes"

        try:
            # Ejecutar comando SQL
            cursor.execute(sql)
            # Conseguir los datos y guardarlos en una lista de listas
            results = cursor.fetchall()
            for row in results:
                id = row[0]
                n = row[1]
                t = row[2]
                m = row[3]

                # Now print fetched result
                print("Nombre: " + id, end=" Teléfono: " + n + " Mail: " + t + " Dni: " + m)
                print("")
                print("-------------------------------------------------------------------------------")


        except:
            print("Error: no se han podido recuperar datos")

        # disconnect from server
        db.close()

    except Error as e:
        print("Error base de datos mysql", e)

    return listClient

# funcion para mostrar los usuarios de la bd
def recuperarUsuariosBd():
    listUsuario = []

    try:

        # Conexión a base de datos
        db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)

        # Preparar el cursor
        cursor = db.cursor()

        sql = "SELECT * FROM usuarios"

        try:
            # Ejecutar comando SQL
            cursor.execute(sql)
            # Conseguir los datos y guardarlos en una lista de listas
            results = cursor.fetchall()
            for row in results:
                id = row[0]
                n = row[1]
                t = row[2]


                # Now print fetched result
                print("Usuario: " + id, end=" Contraseña: " + n + " Departamento: " + t)
                print("")
                print("-------------------------------------------------------------------------------")


        except:
            print("Error: no se han podido recuperar datos")

        # disconnect from server
        db.close()

    except Error as e:
        print("Error base de datos mysql", e)

    return listUsuario

# funcion para mostrar la factura seleccionada de la bd
def recuperarFacturaBd(id):
    # Conexión a base de datos
    db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)

    # Preparar el cursor
    cursor = db.cursor()

    sql = "SELECT * FROM facturas where idFactura = '%d'" % id

    archivo = None
    try:
        # Ejecutar comando SQL
        cursor.execute(sql)
        # Conseguir los datos y guardarlos en una lista de listas
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            n = row[1]
            archivo = n.decode()
            print(type(archivo))
            print(archivo)
            print("hola")

            # Creo la factura y la guardo en la carpeta



    except:
        print("Error: no se han podido recuperar datos")

    # disconnect from server
    db.close()

# funcion para insertar factura de venta en la bd
def insertarFacturaVentaBD(fecha, c, dniCliente, usuarioSistema):
    try:

        # Conexión a base de datos
        db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)
        # Preparar el cursor
        cursor = db.cursor()
        # Consulta SQL para insertar datos de un empleado
        sql = "INSERT INTO facturas(fecha, factura, dni_cliente, usuario) VALUES (%s, %s, %s, %s)"
        val = (fecha, c, dniCliente, usuarioSistema)
        try:
            # Ejecutar el comando SQL
            cursor.execute(sql, val)
            # Aceptar cambios con commit
            db.commit()
        except:

            # Rollback en caso de haber algún error
            db.rollback()
            # Desconexión
        db.close()


    except Error as e:
        print("Error base de datos mysql", e)

# funcion para comprobar usuario
def comprobarUsuarioContrasenyaBd(usuario, password, departamento):
    comprobacion = False

    try:

        # Conexión a base de datos
        db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)

        # Preparar el cursor
        cursor = db.cursor()

        sql = "SELECT usuario, password, departamento FROM usuarios where usuario = '%s'" % usuario
        try:
            # Ejecutar comando SQL
            cursor.execute(sql)

            # Conseguir los datos y guardarlos en una lista de listas
            results = cursor.fetchall()

            for row in results:
                n = row[0]
                t = row[1]
                e = row[2]

                print(n, t)

                if n == usuario and t == password and departamento == e:
                    comprobacion = True

                    print("Usuario correcto.")
                else:
                    print("Error, usuario o password incorrectos.")


        except:
            print("Error: no se han podido recuperar datos")

        # disconnect from server
        db.close()

    except Error as e:
        print("Error de base de datos mysql", e)

    return comprobacion

# funcion para comprobar existencia de cliente
def comprobarSiExisteClienteYrecuperarlo(d):
    de = str(d)

    existencia = False
    c = None

    # Conexión a base de datos
    db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)

    # Preparar el cursor
    cursor = db.cursor()

    sql = "SELECT nombreCliente, telefono, mail, dni FROM clientes where dni = %s"
    document = de

    try:
        # Ejecutar comando SQL
        cursor.execute(sql, document)
        # Conseguir los datos y guardarlos en una lista de listas

        if cursor.rowcount == 0:
            print("Cliente inexistente")

        else:
            results = cursor.fetchall()
            for row in results:
                name = row[0]
                phone = row[1]
                m = row[2]
                e = row[3]

                c = ClienteBd(name, phone, m, e)

            return c

    except:
        print("Error mysql")

    # disconnect from server
    db.close()

# funcion para insertar factura de reparacion en la bd
def insertarFacturaTallerBD(fecha, c, dniCliente, usuarioSistema):
    try:

        # Conexión a base de datos
        db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)
        # Preparar el cursor
        cursor = db.cursor()
        # Consulta SQL para insertar datos de un empleado
        sql = "INSERT INTO reparaciones(fecha, factura, dni_cliente, usuario) VALUES (%s, %s, %s, %s)"
        val = (fecha, c, dniCliente, usuarioSistema)
        try:
            # Ejecutar el comando SQL
            cursor.execute(sql, val)
            # Aceptar cambios con commit
            db.commit()
        except:

            # Rollback en caso de haber algún error
            db.rollback()
            # Desconexión
        db.close()


    except Error as e:
        print("Error base de datos mysql", e)

# funcion que elimina una factura de la Bd
def borrarReparacionBd(archivo):
    try:

        # Conexión a base de datos
        db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)
        # Preparar el cursor
        cursor = db.cursor()
        # Consulta SQL para insertar datos de un empleado
        sql = "DELETE FROM reparaciones WHERE factura = %s"
        val = (archivo,)
        try:
            # Ejecutar el comando SQL
            cursor.execute(sql, val)
            # Aceptar cambios con commit
            db.commit()
            print("Eliminada factura de BD correctamente")
        except:

            # Rollback en caso de haber algún error
            db.rollback()

            print("Error, no se ha eliminado la factura de la base de datos, revise los datos")
            # Desconexión
        db.close()


    except Error as e:
        print("Error base de datos mysql", e)

# funcion para insertar devoluciones en la Bd
def insertarDevolucionBD(devolucion):
    reclamacion = input("Inserte reclamación del cliente: ")
    now = datetime.now()
    fecha = str(now.date())

    try:
        # Conexión a base de datos
        db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)
        # Preparar el cursor
        cursor = db.cursor()
        # Consulta SQL para insertar datos de un empleado
        sql = "INSERT INTO devoluciones(fecha, informacion, devolucion) VALUES (%s, %s, %s)"
        val = (fecha, reclamacion, devolucion)
        try:
            # Ejecutar el comando SQL
            cursor.execute(sql, val)
            # Aceptar cambios con commit
            db.commit()
            print("Insertada correctamente devolución en la base de datos")
        except:
            # Rollback en caso de haber algún error
            db.rollback()
            # Desconexión
        db.close()
    except Error as e:
        print("Error base de datos mysql", e)

# funcion que elimina una factura de la Bd
def borrarDevolucionBd(archivo):
    try:

        # Conexión a base de datos
        db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)
        # Preparar el cursor
        cursor = db.cursor()
        # Consulta SQL para insertar datos de un empleado
        sql = "DELETE FROM devoluciones WHERE devolucion = %s"
        val = (archivo,)
        try:
            # Ejecutar el comando SQL
            cursor.execute(sql, val)

            if cursor.rowcount > 0:
                print("Eliminada factura de BD correctamente")
            else:
                print("Revise datos, no se ha eliminado ningún registro.")

            # Aceptar cambios con commit
            db.commit()

        except:

            # Rollback en caso de haber algún error
            db.rollback()

            print("Error, no se ha eliminado la devolucion de la base de datos, revise los datos")
            # Desconexión
        db.close()


    except Error as e:
        print("Error base de datos mysql", e)

# funcion para eliminar usuario de la bd
def eliminarUsuarioBd(usuario):
    try:

        # Conexión a base de datos
        db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)
        # Preparar el cursor
        cursor = db.cursor()
        # Consulta SQL para insertar datos de un empleado
        sql = "DELETE FROM USUARIOS WHERE usuario = %s"
        val = (usuario,)

        try:
            # Ejecutar el comando SQL
            cursor.execute(sql, val)

            if cursor.rowcount > 0:
                print("Eliminado usuario de BD correctamente")
            else:
                print("No se ha eliminado el usuario")

            # Aceptar cambios con commit
            db.commit()


        except:

            # Rollback en caso de haber algún error
            db.rollback()

            print("Error, no se ha eliminado el usuario de la base de datos, revise los datos")
            # Desconexión
        db.close()

    except Error as e:
        print("Error base de datos mysql", e)

# funcion para contabilizar factura en la bd
def contabilizarFaturaBd(archivo):

    now = datetime.now()
    fecha = str(now.date())

    try:
        # Conexión a base de datos
        db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)
        # Preparar el cursor
        cursor = db.cursor()
        # Consulta SQL para insertar datos de un empleado
        sql = "INSERT INTO facturascontabilizadas(fecha, factura) VALUES (%s, %s)"
        val = (fecha, archivo)
        try:
            # Ejecutar el comando SQL
            cursor.execute(sql, val)
            # Aceptar cambios con commit
            db.commit()
            print("Contabilizada correctamente factura en la base de datos")

        except:
            # Rollback en caso de haber algún error
            db.rollback()
            print("Error, revise los datos")

        # Desconexión
        db.close()
    except Error as e:
        print("Error base de datos mysql", e)

# funcion para borrar oferta de ventas
def borrarOfertaMarketing(id):
    try:

        # Conexión a base de datos
        db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)
        # Preparar el cursor
        cursor = db.cursor()
        # Consulta SQL para insertar datos de un empleado
        sql = "DELETE FROM ofertaventas WHERE id = %s"
        val = (id,)
        try:
            # Ejecutar el comando SQL
            cursor.execute(sql, val)

            if cursor.rowcount > 0:
                print("Eliminada oferta de BD correctamente")
            else:
                print("Revise datos, no se ha eliminado ningún registro.")

            # Aceptar cambios con commit
            db.commit()

        except:

            # Rollback en caso de haber algún error
            db.rollback()

            print("Error, no se ha eliminado la oferta de la base de datos, revise los datos")
            # Desconexión
        db.close()


    except Error as e:
        print("Error base de datos mysql", e)

# funcion para insertas oferta de venta en la bd
def insertarOfertaVentaBD(producto, descripcion, descuento):

    now = datetime.now()
    fecha = str(now.date())

    try:
        # Conexión a base de datos
        db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)
        # Preparar el cursor
        cursor = db.cursor()
        # Consulta SQL para insertar datos de un empleado
        sql = "INSERT INTO ofertaventas(fecha, producto, descripcion, descuento) VALUES (%s, %s, %s, %s)"
        val = (fecha, producto, descripcion, descuento)
        try:
            # Ejecutar el comando SQL
            cursor.execute(sql, val)
            # Aceptar cambios con commit
            db.commit()
            print("Insertada correctamente la oferta en la base de datos")
        except:
            # Rollback en caso de haber algún error
            db.rollback()
            # Desconexión
        db.close()
    except Error as e:
        print("Error base de datos mysql", e)

# funcion para ver las facturas emitidas por un usuario
def verFacturasDeUsuario(usuario):

    try:

        # Conexión a base de datos
        db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)

        # Preparar el cursor
        cursor = db.cursor()

        sql = "SELECT f.factura, t.factura FROM facturas f, reparaciones t WHERE  %s = f.usuario and %s = t.usuario"
        val = (usuario, usuario)


        try:
            # Ejecutar comando SQL
            cursor.execute(sql, val)
            # Conseguir los datos y guardarlos en una lista de listas
            results = cursor.fetchall()
            for row in results:
                id = row[0]
                n = row[1]

                # Now print fetched result
                print("Usuario: " + usuario, end="/ FacturaVenta: " + id + " / Factura Taller: " + n )
                print("")
                print("-------------------------------------------------------------------------------")


        except:
            print("No hay facturas vinculadas al usuario introducido")

        # disconnect from server
        db.close()

    except Error as e:
        print("Error base de datos mysql", e)

# funcion para ver si exite un usuario
def comprobarUsuario(usuario):
    comprobacion = False
    try:

        # Conexión a base de datos
        db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)

        # Preparar el cursor
        cursor = db.cursor()

        sql = "SELECT usuario FROM usuarios where usuario = '%s'" % usuario
        try:
            # Ejecutar comando SQL
            cursor.execute(sql)

            # Conseguir los datos y guardarlos en una lista de listas
            results = cursor.fetchall()

            for row in results:
                n = row[0]

                if n == usuario :
                    comprobacion = True
                else:
                    print("Error, usuario o password incorrectos.")


        except:
            print("Error: no se han podido recuperar datos")

        # disconnect from server
        db.close()

    except Error as e:
        print("Error de base de datos mysql", e)

    return comprobacion

def insertarOfertaEmpleoBd(fecha, puesto, descripcion, sueldo):
    try:
        # Conexión a base de datos
        db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)
        # Preparar el cursor
        cursor = db.cursor()
        # Consulta SQL para insertar datos de un empleado
        sql = "INSERT INTO ofertasempleo(fecha, puesto, descripcion, sueldo) VALUES (%s, %s, %s, %s)"
        val = (fecha, puesto, descripcion, sueldo)
        try:
            # Ejecutar el comando SQL
            cursor.execute(sql, val)
            # Aceptar cambios con commit
            db.commit()
            print("Insertada correctamente la oferta en la base de datos")
        except:
            # Rollback en caso de haber algún error
            db.rollback()
            # Desconexión
        db.close()
    except Error as e:
        print("Error base de datos mysql", e)








