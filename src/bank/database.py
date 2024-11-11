import mysql.connector
import time

# Clase para manejar la base de datos MySQL
class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",      # Cambia esto a tu usuario de MySQL
            password="tu_contraseña",  # Cambia esto a tu contraseña de MySQL
            database="banco"
        )
        self.cursor = self.conn.cursor()
        self.crear_tablas()

    def crear_tablas(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cuenta (
                id INT AUTO_INCREMENT PRIMARY KEY,
                saldo DECIMAL(10, 2),
                pin INT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transacciones (
                id INT AUTO_INCREMENT PRIMARY KEY,
                fecha_hora DATETIME,
                tipo VARCHAR(50)
            )
        ''')
        self.conn.commit()

    def ejecutar_consulta(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.conn.commit()

    def fetch_uno(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchone()

    def fetch_todos(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def cerrar(self):
        self.cursor.close()
        self.conn.close()