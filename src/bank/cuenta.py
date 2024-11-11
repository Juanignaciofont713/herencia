import mysql.connector
import time

# Clase para manejar operaciones de cuenta bancaria
class Cuenta:
    def __init__(self, db):
        self.db = db
        self.inicializar_cuenta()

    def inicializar_cuenta(self):
        if not self.db.fetch_uno('SELECT COUNT(*) FROM cuenta'):
            self.db.ejecutar_consulta('INSERT INTO cuenta (saldo, pin) VALUES (%s, %s)', (250000.0, 1234))

    def leer_pin(self):
        resultado = self.db.fetch_uno('SELECT pin FROM cuenta WHERE id = 1')
        return resultado[0] if resultado else None

    def guardar_pin(self, nuevo_pin):
        self.db.ejecutar_consulta('UPDATE cuenta SET pin = %s WHERE id = 1', (nuevo_pin,))

    def consultar_saldo(self):
        resultado = self.db.fetch_uno('SELECT saldo FROM cuenta WHERE id = 1')
        return resultado[0] if resultado else 0.0

    def actualizar_saldo(self, nuevo_saldo):
        self.db.ejecutar_consulta('UPDATE cuenta SET saldo = %s WHERE id = 1', (nuevo_saldo,))

    def registrar_transaccion(self, tipo):
        fecha_hora = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.db.ejecutar_consulta('INSERT INTO transacciones (fecha_hora, tipo) VALUES (%s, %s)', (fecha_hora, tipo))