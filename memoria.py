
class GestorMemoria:
    def __init__(self, total=100):
        self.total = total
        self.disponible = total
        self.asignaciones = {}

    def asignar(self, pid, cantidad):
        if not isinstance(cantidad, int) or isinstance(cantidad, bool) or cantidad <= 0:
            print("Error: la cantidad debe ser un entero positivo.")
            return False

        if pid in self.asignaciones:
            print(f"El proceso {pid} ya tiene memoria asignada.")
            return False

        if cantidad > self.disponible:
            print(f"Memoria insuficiente para el proceso {pid}.")
            return False

        self.asignaciones[pid] = cantidad
        self.disponible -= cantidad

        print(f"Proceso {pid}: asignados {cantidad} MB de RAM.")
        return True

    def liberar(self, pid):
        if pid not in self.asignaciones:
            print(f"El proceso {pid} no tiene memoria asignada.")
            return False

        cantidad = self.asignaciones.pop(pid)
        self.disponible += cantidad

        print(f"Proceso {pid}: liberados {cantidad} MB.")
        return True

    def mostrar_estado(self):
        print("\n=== ESTADO DE MEMORIA RAM ===")
        print(f"Memoria total: {self.total} MB")
        print(f"Memoria disponible: {self.disponible} MB")
        print(f"Memoria utilizada: {self.total - self.disponible} MB")

        print("\nAsignaciones:")
        if not self.asignaciones:
            print("No hay procesos con memoria asignada.")
        else:
            for pid, cantidad in self.asignaciones.items():
                print(f"Proceso {pid}: {cantidad} MB")


if __name__ == "__main__":
    memoria = GestorMemoria(100)

    print("=== PRUEBA DE GESTION DE RAM ===")

    memoria.asignar(1, 30)
    memoria.asignar(2, 40)
    memoria.asignar(3, 50)

    memoria.mostrar_estado()

    memoria.liberar(1)
    memoria.asignar(3, 50)

    memoria.mostrar_estado()
