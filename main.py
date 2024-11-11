import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from bank.database import Database
from bank.cuenta import Cuenta
from bank.cajeroautomatico import CajeroAutomatico

# Función principal para iniciar el programa
def main():
    db = Database()
    print("Conexión a la base de datos exitosa")
    db.cerrar()

if __name__ == "__main__":
    cajero = CajeroAutomatico()
    cajero.menu()