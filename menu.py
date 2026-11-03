
from main import probar_round_robin, probar_semaforo
from procesos import PCB
from deadlock import DetectorDeadlock
from memoria import GestorMemoria


def probar_deadlock():
    print("\n=== PRUEBA DE DETECCION DE DEADLOCK ===")

    detector = DetectorDeadlock()

    p1 = PCB(1, "LISTO", 10, 5, 5)
    p2 = PCB(2, "LISTO", 10, 5, 5)

    detector.asignar_recurso(p1, "A")
    detector.asignar_recurso(p2, "B")

    detector.solicitar_recurso(p1, "B")
    detector.solicitar_recurso(p2, "A")

    detector.detectar_deadlock()


def probar_memoria():
    print("\n=== PRUEBA DE GESTION DE MEMORIA RAM ===")

    memoria = GestorMemoria(100)

    memoria.asignar(1, 30)
    memoria.asignar(2, 40)
    memoria.asignar(3, 50)

    memoria.mostrar_estado()

    memoria.liberar(1)
    memoria.asignar(3, 50)

    memoria.mostrar_estado()


def mostrar_menu():
    while True:
        print("\n" + "=" * 45)
        print(" SIMULADOR DE FUNCIONES DEL KERNEL")
        print("=" * 45)
        print("1. Gestion de procesos - Round Robin")
        print("2. Semaforo binario")
        print("3. Deteccion de Deadlock")
        print("4. Gestion de memoria RAM")
        print("5. Salir")
        print("=" * 45)

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            probar_round_robin()

        elif opcion == "2":
            probar_semaforo()

        elif opcion == "3":
            probar_deadlock()

        elif opcion == "4":
            probar_memoria()

        elif opcion == "5":
            print("\nSaliendo del simulador...")
            break

        else:
            print("\nOpcion invalida. Intente nuevamente.")


if __name__ == "__main__":
    mostrar_menu()
 