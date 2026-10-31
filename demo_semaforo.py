"""Demostracion del modulo de semaforos con los PCB existentes."""
from procesos import PCB, GestorProcesos
from semaforo import SemaforoBinario


def main():
    gestor = GestorProcesos()
    for pid in (1, 2, 3):
        gestor.agregar_proceso(PCB(pid, "LISTO", 10, 5, 5))
    p1, p2, p3 = gestor.procesos
    semaforo = SemaforoBinario()

    print("\n--- PRUEBA DE EXCLUSION MUTUA ---")
    semaforo.wait(p1)
    semaforo.wait(p2)
    semaforo.wait(p3)
    semaforo.modificar_variable(p2, 10)  # Se debe rechazar
    semaforo.modificar_variable(p1, 5)
    semaforo.mostrar_estado()

    semaforo.signal(p1)  # Entra automaticamente p2
    semaforo.modificar_variable(p2, 3)
    semaforo.signal(p2)  # Entra automaticamente p3
    semaforo.modificar_variable(p3, 2)
    semaforo.signal(p3)
    print("\n--- ESTADO FINAL ---")
    semaforo.mostrar_estado()


if __name__ == "__main__":
    main()
