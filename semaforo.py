"""Semaforo binario simulado para el proyecto Kernel/SO."""
from collections import deque


class SemaforoBinario:
    def __init__(self):
        self.valor = 1  # 1 = libre, 0 = ocupado
        self.propietario = None
        self.cola_espera = deque()
        self.variable_compartida = 0

    def wait(self, proceso):
        """Solicita acceso; si esta ocupado, bloquea y encola el PCB."""
        if proceso.estado == "TERMINADO":
            print(f"Proceso {proceso.pid}: no puede entrar porque termino.")
            return False
        if self.propietario is proceso:
            print(f"Proceso {proceso.pid}: ya tiene el semaforo.")
            return True
        if proceso in self.cola_espera:
            print(f"Proceso {proceso.pid}: ya esta esperando.")
            return False
        if self.valor == 1 and not self.cola_espera:
            self.valor = 0
            self.propietario = proceso
            proceso.estado = "EJECUTANDO"
            print(f"Proceso {proceso.pid} ingreso a la seccion critica.")
            return True
        proceso.estado = "BLOQUEADO"
        self.cola_espera.append(proceso)
        print(f"Proceso {proceso.pid} bloqueado; agregado a la cola de espera.")
        return False

    def modificar_variable(self, proceso, cantidad=1):
        """Solo el propietario puede modificar la variable compartida."""
        if self.propietario is not proceso:
            print(f"Acceso denegado al proceso {proceso.pid}: no tiene el semaforo.")
            return False
        if type(cantidad) is not int:
            print("Error: la cantidad debe ser un entero.")
            return False
        self.variable_compartida += cantidad
        print(f"Proceso {proceso.pid} modifico la variable: {self.variable_compartida}.")
        return True

    def signal(self, proceso):
        """Libera el recurso y concede acceso al siguiente PCB en espera."""
        if self.propietario is not proceso:
            print(f"Proceso {proceso.pid} no puede liberar un semaforo ajeno.")
            return False
        print(f"Proceso {proceso.pid} salio de la seccion critica.")
        if proceso.estado != "TERMINADO":
            proceso.estado = "LISTO"
        self.propietario = None
        self.valor = 1
        if self.cola_espera:
            siguiente = self.cola_espera.popleft()
            self.valor = 0
            self.propietario = siguiente
            siguiente.estado = "EJECUTANDO"
            print(f"Proceso {siguiente.pid} sale de la espera e ingresa a la seccion critica.")
        return True

    def mostrar_estado(self):
        print(f"Semaforo: {'LIBRE' if self.valor else 'OCUPADO'}")
        print(f"Propietario: {self.propietario.pid if self.propietario else 'Ninguno'}")
        print(f"Cola de espera: {[p.pid for p in self.cola_espera]}")
        print(f"Variable compartida: {self.variable_compartida}")
