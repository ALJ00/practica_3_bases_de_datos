import pymysql
from pymysql import Error


# Funciones para crear las tablas
def crear_tabla_usuarios():
    # Conexión a la base de datos
    db = pymysql.connect(host="127.0.0.1", user="dockerbox", db="dockerbox", port=3306)
    # Preparar el cursor
    cursor = db.cursor()
    # Eliminar tabla (drop) si ya existe
    cursor.execute("DROP TABLE IF EXISTS USUARIOS")
    # SQL para crear tabla
    sql = """CREATE TABLE USUARIOS (
        idUsuario INT AUTO_INCREMENT PRIMARY KEY,
        usuario CHAR(20) NOT NULL UNIQUE,
        password CHAR(30) NOT NULL UNIQUE,
        departamento CHAR(20) NOT NULL UNIQUE)"""
    cursor.execute(sql)
    # Desconectar del servidor
    db.close()

def crear_tabla_clientes():
    # Conexión a la base de datos
    db = pymysql.connect(host="127.0.0.1", user="dockerbox", db="dockerbox", port=3306)
    # Preparar el cursor
    cursor = db.cursor()
    # Eliminar tabla (drop) si ya existe
    cursor.execute("DROP TABLE IF EXISTS CLIENTES")
    # SQL para crear tabla
    sql = """CREATE TABLE CLIENTES (
        idCliente INT AUTO_INCREMENT PRIMARY KEY,
        nombreCliente CHAR(20) NOT NULL UNIQUE,
        telefono CHAR(30) NOT NULL UNIQUE,
        mail CHAR(20) NOT NULL UNIQUE,
        dni CHAR(12) NOT NULL UNIQUE)"""
    cursor.execute(sql)
    # Desconectar del servidor
    db.close()

def crear_tabla_facturas():
    # Conexión a la base de datos
    db = pymysql.connect(host="127.0.0.1", user="dockerbox", db="dockerbox", port=3306)
    # Preparar el cursor
    cursor = db.cursor()
    # Eliminar tabla (drop) si ya existe
    cursor.execute("DROP TABLE IF EXISTS FACTURAS")
    # SQL para crear tabla
    sql = """CREATE TABLE FACTURAS (

    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha CHAR(20) NOT NULL,
    factura CHAR(30),
    CONSTRAINT cons_fk_idClie FOREIGN KEY (id) REFERENCES clientes(idCliente),
    CONSTRAINT cons_fk_idUser FOREIGN KEY (id) REFERENCES usuarios(idUsuario))"""
    cursor.execute(sql)
    # Desconectar del servidor
    db.close()

def crear_tabla_ofertasEmpleo():
    # Conexión a la base de datos
    db = pymysql.connect(host="127.0.0.1", user="dockerbox", db="dockerbox", port=3306)
    # Preparar el cursor
    cursor = db.cursor()
    # Eliminar tabla (drop) si ya existe
    cursor.execute("DROP TABLE IF EXISTS OFERTASEMPLEO")
    # SQL para crear tabla
    sql = """CREATE TABLE ofertasEmpleo (

    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha CHAR(20) NOT NULL,
    puesto CHAR(20),
    descripcion CHAR(20),
    sueldo FLOAT,
    CONSTRAINT fk_User FOREIGN KEY (id) REFERENCES usuarios(idUsuario))"""
    cursor.execute(sql)
    # Desconectar del servidor
    db.close()

def crear_tabla_reparaciones():
    # Conexión a la base de datos
    db = pymysql.connect(host="127.0.0.1", user="dockerbox", db="dockerbox", port=3306)
    # Preparar el cursor
    cursor = db.cursor()
    # Eliminar tabla (drop) si ya existe
    cursor.execute("DROP TABLE IF EXISTS REPARACIONES")
    # SQL para crear tabla
    sql = """CREATE TABLE REPARACIONES (
                id INT AUTO_INCREMENT PRIMARY KEY,
                fecha CHAR(20) NOT NULL,
                factura CHAR(30),
                CONSTRAINT cons_fk_Client FOREIGN KEY (id) REFERENCES clientes(idCliente),
                CONSTRAINT cons_fk_User FOREIGN KEY (id) REFERENCES usuarios(idUsuario))"""

    cursor.execute(sql)
    # Desconectar del servidor
    db.close()

def crear_tabla_ofertaVenta():
    try:

        # Conexión a la base de datos
        db = pymysql.connect(host="127.0.0.1", user="dockerbox", db="dockerbox", port=3306)
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
                  CONSTRAINT c_fk_U FOREIGN KEY (id) REFERENCES usuarios(idUsuario))"""

        cursor.execute(sql)
        # Desconectar del servidor
        db.close()

    except Error as e:
        print("Error de conexión BD Mysql")

def crear_tabla_devoluciones():
    try:

        # Conexión a la base de datos
        db = pymysql.connect(host="127.0.0.1", user="dockerbox", db="dockerbox", port=3306)
        # Preparar el cursor
        cursor = db.cursor()
        # Eliminar tabla (drop) si ya existe
        cursor.execute("DROP TABLE IF EXISTS DEVOLUCIONES")
        # SQL para crear tabla
        sql = """CREATE TABLE DEVOLUCIONES (

                  id INT AUTO_INCREMENT PRIMARY KEY,
                  fecha CHAR(20) NOT NULL,
                  informacion CHAR(50) NOT NULL,   
                  devolucion CHAR(30) UNIQUE,
                  CONSTRAINT fk_U FOREIGN KEY (id) REFERENCES usuarios(idUsuario))"""

        cursor.execute(sql)
        # Desconectar del servidor
        db.close()

    except Error as e:
        print("Error de conexión BD Mysql")

def crear_tabla_facturas_contabilizadas():
    try:

        # Conexión a la base de datos
        db = pymysql.connect(host="127.0.0.1", user="dockerbox", db="dockerbox", port=3306)
        # Preparar el cursor
        cursor = db.cursor()
        # Eliminar tabla (drop) si ya existe
        cursor.execute("DROP TABLE IF EXISTS FACTURASCONTABILIZADAS")
        # SQL para crear tabla
        sql = """CREATE TABLE FACTURASCONTABILIZADAS (

                  id INT AUTO_INCREMENT PRIMARY KEY,
                  fecha CHAR(20) NOT NULL,
                  factura CHAR(30) NOT NULL UNIQUE,
                  CONSTRAINT c_fk_Ur FOREIGN KEY (id) REFERENCES usuarios(idUsuario))"""

        cursor.execute(sql)
        # Desconectar del servidor
        db.close()

    except Error as e:
        print("Error de conexión BD Mysql")


# Ejecuto las funciones para crear las tablas
crear_tabla_usuarios()
crear_tabla_clientes()
crear_tabla_ofertasEmpleo()
crear_tabla_facturas()
crear_tabla_reparaciones()
crear_tabla_ofertaVenta()
crear_tabla_devoluciones()
crear_tabla_facturas_contabilizadas()