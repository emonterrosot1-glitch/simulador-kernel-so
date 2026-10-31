from procesos import PCB, GestorProcesos

gestor = GestorProcesos()

gestor.agregar_proceso(PCB(1, "LISTO", 20, 5, 5))
gestor.agregar_proceso(PCB(2, "LISTO", 30, 8, 8))
gestor.agregar_proceso(PCB(3, "LISTO", 10, 4, 4))

print("SIMULADOR DE FUNCIONES DEL KERNEL")
print("Algoritmo Round Robin - Quantum = 3")

gestor.round_robin()