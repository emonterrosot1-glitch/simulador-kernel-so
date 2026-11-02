
from procesos import PCB, GestorProcesos
from semaforo import SemaforoBinario


def probar_round_robin():
    print("\n=== PLANIFICACION ROUND ROBIN ===")

    gestor = GestorProcesos()

    gestor.agregar_proceso(PCB(1, "LISTO", 20, 5, 5))
    gestor.agregar_proceso(PCB(2, "LISTO", 30, 8, 8))
    gestor.agregar_proceso(PCB(3, "LISTO", 10, 4, 4))

    gestor.round_robin()


def probar_semaforo():
    print("\n=== PRUEBA DEL SEMAFORO BINARIO ===")

    gestor = GestorProcesos()

    for pid in (1, 2, 3):
        gestor.agregar_proceso(PCB(pid, "LISTO", 10, 5, 5))

    p1, p2, p3 = gestor.procesos
    semaforo = SemaforoBinario()

    semaforo.wait(p1)
    semaforo.wait(p2)
    semaforo.wait(p3)

    semaforo.modificar_variable(p2, 10)
    semaforo.modificar_variable(p1, 5)

    semaforo.signal(p1)
    semaforo.modificar_variable(p2, 3)

    semaforo.signal(p2)
    semaforo.modificar_variable(p3, 2)

    semaforo.signal(p3)
    semaforo.mostrar_estado()


def main():
    print("SIMULADOR DE FUNCIONES DEL KERNEL")

    probar_round_robin()
    probar_semaforo()

    print("\n=== PRUEBAS FINALIZADAS ===")


if __name__ == "__main__":
    main()
