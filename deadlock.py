
from procesos import PCB


class DetectorDeadlock:
    def __init__(self):
        self.recursos = {}
        self.esperando = {}

    def asignar_recurso(self, proceso, recurso):
        if recurso in self.recursos:
            print(f"Recurso {recurso} ocupado.")
            return False

        self.recursos[recurso] = proceso.pid
        print(f"Recurso {recurso} asignado al proceso {proceso.pid}")
        return True

    def solicitar_recurso(self, proceso, recurso):
        if recurso not in self.recursos:
            return self.asignar_recurso(proceso, recurso)

        propietario = self.recursos[recurso]

        if propietario == proceso.pid:
            print(f"Proceso {proceso.pid} ya tiene {recurso}")
            return True

        self.esperando[proceso.pid] = recurso
        proceso.estado = "BLOQUEADO"

        print(
            f"Proceso {proceso.pid} bloqueado: "
            f"esperando recurso {recurso}"
        )
        return False

    def detectar_deadlock(self):
        print("\n--- DETECCION DE DEADLOCK ---")

        grafo = {}

        for pid, recurso in self.esperando.items():
            propietario = self.recursos.get(recurso)

            if propietario is not None and propietario != pid:
                grafo[pid] = propietario

        visitados = set()

        for inicio in grafo:
            actual = inicio
            camino = []
            posiciones = {}

            while actual in grafo:
                if actual in posiciones:
                    ciclo = camino[posiciones[actual]:]

                    print("DEADLOCK DETECTADO")
                    print(f"Procesos involucrados: {ciclo}")
                    return ciclo

                if actual in visitados:
                    break

                posiciones[actual] = len(camino)
                camino.append(actual)
                actual = grafo[actual]

            visitados.update(camino)

        print("No se detecto deadlock.")
        return []

    def liberar_recurso(self, proceso, recurso):
        if self.recursos.get(recurso) != proceso.pid:
            print("El proceso no posee ese recurso.")
            return False

        del self.recursos[recurso]
        print(f"Proceso {proceso.pid} libero {recurso}")
        return True


if __name__ == "__main__":
    detector = DetectorDeadlock()

    p1 = PCB(1, "LISTO", 10, 5, 5)
    p2 = PCB(2, "LISTO", 10, 5, 5)

    detector.asignar_recurso(p1, "A")
    detector.asignar_recurso(p2, "B")

    detector.solicitar_recurso(p1, "B")
    detector.solicitar_recurso(p2, "A")

    detector.detectar_deadlock()
