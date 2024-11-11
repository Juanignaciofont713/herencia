from .bank import Database
from .bank import Cuenta

# Clase para interactuar con el usuario
class CajeroAutomatico:
    def __init__(self):
        self.db = Database()
        self.cuenta = Cuenta(self.db)

    def menu(self):
        pin_actual = self.cuenta.leer_pin()
        pin_ingresado = int(input("Ingrese su PIN: "))

        if pin_ingresado == pin_actual:
            print("Hola. Bienvenida/o al cajero automático.")
            while True:
                print("\nOpciones:\n"
                      "1. Consultar Saldo\n"
                      "2. Retirar Dinero\n"
                      "3. Depositar Dinero\n"
                      "4. Cambiar PIN\n"
                      "5. Salir")
                opcion = int(input("Seleccione una opción: "))

                if opcion == 1:
                    self.consultar_saldo()
                elif opcion == 2:
                    self.retirar_saldo()
                elif opcion == 3:
                    self.depositar_saldo()
                elif opcion == 4:
                    self.cambiar_pin()
                elif opcion == 5:
                    print("Gracias por usar el cajero automático. ¡Buen día!")
                    break
                else:
                    print("Opción inválida. Por favor seleccione una opción válida.")
        else:
            print("PIN Incorrecto. No se puede acceder.")

    def consultar_saldo(self):
        saldo = self.cuenta.consultar_saldo()
        print(f"Saldo Actual: ${saldo:.2f}")
        self.cuenta.registrar_transaccion("Consulta de Saldo")

    def retirar_saldo(self):
        cantidad = float(input("Ingrese la cantidad a retirar: $"))
        saldo = self.cuenta.consultar_saldo()
        if 0 < cantidad <= saldo:
            nuevo_saldo = saldo - cantidad
            self.cuenta.actualizar_saldo(nuevo_saldo)
            print(f"Retiro realizado. Su saldo actual es de: ${nuevo_saldo:.2f}")
            self.cuenta.registrar_transaccion("Retiro")
        else:
            print("El saldo en la cuenta es insuficiente para el retiro.")

    def depositar_saldo(self):
        cantidad = float(input("Ingrese la cantidad a depositar: $"))
        if cantidad > 0:
            saldo = self.cuenta.consultar_saldo()
            nuevo_saldo = saldo + cantidad
            self.cuenta.actualizar_saldo(nuevo_saldo)
            print(f"Depósito realizado. Su saldo actual es de: ${nuevo_saldo:.2f}")
            self.cuenta.registrar_transaccion("Depósito")
        else:
            print("Cantidad no válida para realizar el depósito.")

    def cambiar_pin(self):
        nuevo_pin = int(input("Ingrese el nuevo PIN: "))
        self.cuenta.guardar_pin(nuevo_pin)
        print("El PIN ha sido actualizado.")
        self.cuenta.registrar_transaccion("Cambio de PIN")