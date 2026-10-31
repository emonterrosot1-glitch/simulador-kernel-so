
from dataclasses import dataclass
from collections import deque


@dataclass
class PCB:
    pid: int
    estado: str
    memoria_mb: int
    rafaga_total: int
    rafaga_restante: int


class GestorProcesos:
    def __init__(self):
        self.procesos = []
        self.quantum = 3

    def agregar_proceso(self, proceso):
        # Validar que sea un PCB
        if not isinstance(proceso, PCB):
            print("Error: El proceso debe ser un PCB.")
            return False

        # Validar identificador
        if type(proceso.pid) is not int or proceso.pid <= 0:
            print("Error: El PID debe ser un entero positivo.")
            return False

        # Evitar procesos con PID repetido
        if any(p.pid == proceso.pid for p in self.procesos):
            print("Error: El PID ya existe.")
            return False

        # Validar memoria solicitada
        if type(proceso.memoria_mb) is not int or proceso.memoria_mb <= 0:
            print("Error: La memoria debe ser un entero positivo.")
            return False

        # Validar rafaga de CPU
        if type(proceso.rafaga_total) is not int or proceso.rafaga_total <= 0:
            print("Error: La rafaga total debe ser positiva.")
            return False

        if proceso.rafaga_restante != proceso.rafaga_total:
            print("Error: La rafaga restante inicial debe coincidir con la total.")
            return False

        # Registrar proceso
        proceso.estado = "LISTO"
        self.procesos.append(proceso)

        print(f"Proceso {proceso.pid} agregado correctamente.")
        return True

    def round_robin(self):
        # Cola de procesos listos
        cola = deque(
            proceso for proceso in self.procesos
            if proceso.estado == "LISTO"
        )

        tiempo = 0

        if not cola:
            print("No hay procesos listos para ejecutar.")
            return

        print("\nINICIANDO PLANIFICACION ROUND ROBIN")
        print(f"Quantum: {self.quantum}\n")

        while cola:
            proceso = cola.popleft()

            # Cambio de estado a EJECUTANDO
            proceso.estado = "EJECUTANDO"

            # Ejecutar maximo un quantum
            ejecucion = min(
                self.quantum,
                proceso.rafaga_restante
            )

            print(
                f"Proceso {proceso.pid} ejecutando "
                f"{ejecucion} unidades"
            )

            proceso.rafaga_restante -= ejecucion
            tiempo += ejecucion

            # Verificar si termino
            if proceso.rafaga_restante > 0:
                proceso.estado = "LISTO"
                cola.append(proceso)

                print(
                    f"Proceso {proceso.pid} vuelve a la cola"
                )

            else:
                proceso.estado = "TERMINADO"

                print(
                    f"Proceso {proceso.pid} finalizado "
                    f"en tiempo {tiempo}"
                )

        print("\nTodos los procesos finalizaron.")
        print(f"Tiempo total de CPU: {tiempo} unidades")
