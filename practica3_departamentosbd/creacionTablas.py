import pymysql
from pymysql import Error
import pymysql


# Funciones para crear las tablas
def crear_tabla_usuarios():
    # Conexión a la base de datos
    db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)
    # Preparar el cursor
    cursor = db.cursor()
    # Eliminar tabla (drop) si ya existe
    cursor.execute("DROP TABLE IF EXISTS USUARIOS")
    # SQL para crear tabla
    sql = """CREATE TABLE USUARIOS (
        usuario CHAR(20) PRIMARY KEY,
        password CHAR(30) NOT NULL UNIQUE,
        departamento CHAR(20) NOT NULL UNIQUE)"""

    cursor.execute(sql)
    # Desconectar del servidor
    db.close()

def crear_tabla_clientes():
    # Conexión a la base de datos
    db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)
    # Preparar el cursor
    cursor = db.cursor()
    # Eliminar tabla (drop) si ya existe
    cursor.execute("DROP TABLE IF EXISTS CLIENTES")
    # SQL para crear tabla
    sql = """CREATE TABLE CLIENTES (
        nombreCliente CHAR(20) NOT NULL UNIQUE,
        telefono CHAR(30) NOT NULL UNIQUE,
        mail CHAR(20) NOT NULL UNIQUE,
        dni CHAR(12) PRIMARY KEY)"""
    cursor.execute(sql)
    # Desconectar del servidor
    db.close()

def crear_tabla_facturas():
    # Conexión a la base de datos
    db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)
    # Preparar el cursor
    cursor = db.cursor()
    # Eliminar tabla (drop) si ya existe
    cursor.execute("DROP TABLE IF EXISTS FACTURAS")
    # SQL para crear tabla
    sql = """CREATE TABLE FACTURAS (
    fecha CHAR(20) NOT NULL,
    factura CHAR(30) PRIMARY KEY,
    dni_cliente CHAR(12),
    usuario CHAR(20),
    FOREIGN KEY (dni_cliente) REFERENCES clientes(dni),
    FOREIGN KEY (usuario) REFERENCES usuarios(usuario))"""
    cursor.execute(sql)
    # Desconectar del servidor
    db.close()

def crear_tabla_ofertasEmpleo():
    # Conexión a la base de datos
    db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)
    # Preparar el cursor
    cursor = db.cursor()
    # Eliminar tabla (drop) si ya existe
    cursor.execute("DROP TABLE IF EXISTS OFERTASEMPLEO")
    # SQL para crear tabla
    sql = """CREATE TABLE ofertasempleo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha CHAR(20) NOT NULL,
    puesto CHAR(20),
    descripcion CHAR(20),
    sueldo FLOAT,
    usuario CHAR(20),
    FOREIGN KEY (usuario) REFERENCES USUARIOS(usuario))"""
    cursor.execute(sql)
    # Desconectar del servidor
    db.close()

def crear_tabla_reparaciones():
    # Conexión a la base de datos
    db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)
    # Preparar el cursor
    cursor = db.cursor()
    # Eliminar tabla (drop) si ya existe
    cursor.execute("DROP TABLE IF EXISTS REPARACIONES")
    # SQL para crear tabla
    sql = """CREATE TABLE REPARACIONES (
                fecha CHAR(20) NOT NULL,
                factura CHAR(30) PRIMARY KEY,
                dni_cliente CHAR(12),
                usuario CHAR(20),
                FOREIGN KEY (dni_cliente) REFERENCES clientes(dni),
                FOREIGN KEY (usuario) REFERENCES usuarios(usuario))"""

    cursor.execute(sql)
    # Desconectar del servidor
    db.close()

def crear_tabla_ofertaVenta():
    try:

        # Conexión a la base de datos
        db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)
        # Preparar el cursor
        cursor = db.cursor()
        # Eliminar tabla (drop) si ya existe
        cursor.execute("DROP TABLE IF EXISTS OFERTAVENTAS")
        # SQL para crear tabla
        sql = """CREATE TABLE OFERTAVENTAS (
                  id INT AUTO_INCREMENT PRIMARY KEY,
                  fecha CHAR(20) NOT NULL,    
                  producto CHAR(20), 
                  descripcion CHAR(20),
                  descuento FLOAT,
                  usuario CHAR(20),
                  FOREIGN KEY (usuario) REFERENCES usuarios(usuario))"""

        cursor.execute(sql)
        # Desconectar del servidor
        db.close()

    except Error as e:
        print("Error de conexión BD Mysql")

def crear_tabla_devoluciones():
    try:

        # Conexión a la base de datos
        db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)
        # Preparar el cursor
        cursor = db.cursor()
        # Eliminar tabla (drop) si ya existe
        cursor.execute("DROP TABLE IF EXISTS DEVOLUCIONES")
        # SQL para crear tabla
        sql = """CREATE TABLE DEVOLUCIONES (
                  fecha CHAR(20) NOT NULL,
                  informacion CHAR(50) NOT NULL,   
                  devolucion CHAR(30) PRIMARY KEY,
                  usuario CHAR(20),
                  FOREIGN KEY (usuario) REFERENCES usuarios(usuario))"""

        cursor.execute(sql)
        # Desconectar del servidor
        db.close()

    except Error as e:
        print("Error de conexión BD Mysql")

def crear_tabla_facturas_contabilizadas():
    try:

        # Conexión a la base de datos
        db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)
        # Preparar el cursor
        cursor = db.cursor()
        # Eliminar tabla (drop) si ya existe
        cursor.execute("DROP TABLE IF EXISTS FACTURASCONTABILIZADAS")
        # SQL para crear tabla
        sql = """CREATE TABLE FACTURASCONTABILIZADAS (
                  fecha CHAR(20) NOT NULL,
                  factura CHAR(30) PRIMARY KEY,
                  usuario CHAR(20),
                  FOREIGN KEY (usuario) REFERENCES usuarios(usuario))"""

        cursor.execute(sql)
        # Desconectar del servidor
        db.close()

    except Error as e:
        print("Error de conexión BD Mysql")

def insertarUsuarios(user, password, dep):
    # Conexión a base de datos
    db = pymysql.connect(host="127.0.0.1", user="root", db="erpbicicletasegibide", port=3306)
    # Preparar el cursor
    cursor = db.cursor()
    # Consulta SQL para insertar datos de un empleado
    sql = "INSERT INTO usuarios(usuario, password, departamento) VALUES (%s, %s, %s)"
    val = (user, password, dep)

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



# Ejecuto las funciones para crear las tablas
crear_tabla_usuarios()
crear_tabla_clientes()
insertarUsuarios("ventas", "ventas", "ve")
insertarUsuarios("marketing", "marketing", "ma")
insertarUsuarios("postventa", "postventa", "pv")
insertarUsuarios("taller", "taller", "ta")
crear_tabla_ofertasEmpleo()
crear_tabla_facturas()
crear_tabla_reparaciones()
crear_tabla_ofertaVenta()
crear_tabla_devoluciones()
crear_tabla_facturas_contabilizadas()

