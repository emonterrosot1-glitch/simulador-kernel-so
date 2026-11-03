# Simulador de funciones del kernel de un sistema operativo

## ¿De qué trata nuestro proyecto?

En este proyecto desarrollamos un simulador en Python que nos permite mostrar cómo funcionan algunas de las tareas más importantes que realiza el kernel de un sistema operativo.

La idea principal fue llevar a la práctica varios de los temas que aprendimos durante el curso de Sistemas Operativos, ya que muchas veces es más fácil entenderlos cuando podemos observar cómo funcionan en un programa.

Nuestro simulador permite trabajar con procesos, administrar memoria RAM, utilizar semáforos y detectar situaciones de bloqueo entre procesos.

Todo funciona desde un menú en la terminal, donde podemos elegir qué parte del simulador queremos ejecutar.

## ¿Cuál es nuestro objetivo?

Nuestro objetivo fue crear un programa que nos ayudara a comprender mejor cómo un sistema operativo administra sus recursos y organiza la ejecución de diferentes procesos.

También buscamos poner en práctica nuestros conocimientos de programación en Python y aprender a trabajar con diferentes módulos dentro de un mismo proyecto.

## ¿Qué puede hacer nuestro simulador?

### 1. Planificación de procesos con Round Robin

En esta parte simulamos cómo el sistema operativo organiza varios procesos para que puedan utilizar el procesador.

Utilizamos el algoritmo Round Robin, que consiste en darle a cada proceso un tiempo determinado para ejecutarse.

En nuestro caso, utilizamos un quantum de 3 unidades de tiempo.

Si un proceso no termina durante ese tiempo, vuelve a la cola para esperar otro turno. Esto continúa hasta que todos los procesos terminan.

También utilizamos los PCB, que son estructuras donde guardamos información importante de cada proceso, como su identificador, estado y tiempo de ejecución.

### 2. Semáforo binario

En este módulo trabajamos con un semáforo binario, que sirve para controlar cuándo un proceso puede utilizar un recurso compartido.

Por ejemplo, si un proceso está utilizando un recurso, los demás deben esperar hasta que esté disponible.

Para representar esto utilizamos las funciones `wait()` y `signal()`.

La primera permite solicitar acceso al recurso y la segunda permite liberarlo.

También agregamos una variable compartida que únicamente puede ser modificada por el proceso que tenga el permiso del semáforo.

Con esta prueba pudimos observar cómo se evita que varios procesos entren a una misma sección crítica al mismo tiempo.

### 3. Detección de deadlock

En esta parte simulamos una situación conocida como deadlock o interbloqueo.

Esto sucede cuando varios procesos quedan esperando recursos que están siendo utilizados por otros procesos y ninguno puede continuar.

Para demostrarlo creamos dos procesos y dos recursos.

El primer proceso utiliza el recurso A y necesita el B, mientras que el segundo utiliza el recurso B y necesita el A.

Como ambos están esperando al otro, se produce un bloqueo.

Nuestro programa analiza esta situación y muestra un mensaje cuando detecta el deadlock, indicando cuáles son los procesos involucrados.

### 4. Gestión de memoria RAM

En este módulo simulamos cómo se administra la memoria RAM de una computadora.

Para hacerlo utilizamos una memoria de 100 MB, que se reparte entre diferentes procesos.

El programa permite asignar memoria, comprobar cuánto espacio queda disponible y liberar memoria cuando un proceso ya no la necesita.

También realizamos una prueba donde un proceso solicita más memoria de la disponible.

En ese caso, el programa muestra que no hay suficiente espacio. Después liberamos memoria de otro proceso y volvemos a realizar la asignación.

Esto nos permitió comprender mejor cómo se controla el uso de la memoria.

## Herramientas que utilizamos

Para desarrollar nuestro proyecto utilizamos:

- Python, para programar el simulador.
- Visual Studio Code, para escribir y ejecutar el código.
- Git, para guardar los cambios que realizamos.
- GitHub, para compartir el proyecto y trabajar con los archivos.

## Archivos de nuestro proyecto

Organizamos el programa en diferentes archivos para que fuera más fácil trabajar con cada función.

```text
simulador-kernel-so/
│
├── main.py
├── procesos.py
├── semaforo.py
├── demo_semaforo.py
├── deadlock.py
├── memoria.py
├── menu.py
├── README.md
└── .gitignore
```

Cada archivo tiene una función:

- `main.py`: contiene las pruebas de Round Robin y del semáforo.
- `procesos.py`: administra los procesos y ejecuta el algoritmo Round Robin.
- `semaforo.py`: controla el acceso a recursos compartidos.
- `demo_semaforo.py`: permite probar el funcionamiento del semáforo por separado.
- `deadlock.py`: detecta situaciones de interbloqueo entre procesos.
- `memoria.py`: administra la asignación y liberación de memoria RAM.
- `menu.py`: reúne las diferentes funciones del simulador en un menú principal.

## ¿Cómo ejecutar nuestro proyecto?

Para ejecutar el simulador es necesario tener Python 3 instalado en la computadora.

Primero debemos descargar el proyecto desde GitHub o clonarlo utilizando este comando:

```bash
git clone https://github.com/emonterrosot1-glitch/simulador-kernel-so.git
```

Después entramos a la carpeta del proyecto:

```bash
cd simulador-kernel-so
```

Finalmente, ejecutamos el programa con:

```bash
python menu.py
```

Al iniciar aparecerá un menú parecido a este:

```text
=============================================
 SIMULADOR DE FUNCIONES DEL KERNEL
=============================================
1. Gestion de procesos - Round Robin
2. Semaforo binario
3. Deteccion de Deadlock
4. Gestion de memoria RAM
5. Salir
=============================================

Seleccione una opcion:
```

Solo debemos escribir el número de la opción que queremos probar y presionar Enter.

Cuando termina una prueba, el programa vuelve a mostrar el menú para que podamos seleccionar otra opción.

## Pruebas que realizamos

Durante el desarrollo fuimos probando las diferentes partes del programa para comprobar que funcionaran como esperábamos.

**Prueba de Round Robin**

Ejecutamos tres procesos utilizando un quantum de 3 unidades. Pudimos observar cómo se turnaban para utilizar el procesador hasta finalizar todos.

En nuestra prueba, el tiempo total de CPU fue de 17 unidades.

**Prueba del semáforo**

Creamos tres procesos que intentaban acceder a una variable compartida.

El programa permitió que solo uno tuviera acceso al recurso mientras los demás esperaban.

Al finalizar, la variable compartida tenía un valor de 10 y el semáforo quedó libre.

**Prueba de deadlock**

Creamos dos procesos que necesitaban recursos que estaban siendo utilizados por el otro.

El programa logró identificar el bloqueo y mostró cuáles eran los procesos involucrados.

**Prueba de memoria RAM**

Simulamos una memoria de 100 MB y realizamos varias asignaciones.

Primero asignamos 30 MB y 40 MB a dos procesos. Después intentamos asignar 50 MB a un tercero, pero no había suficiente memoria.

Luego liberamos 30 MB y repetimos la solicitud. Esta vez el programa permitió realizar la asignación.

Al finalizar quedaron 90 MB utilizados y 10 MB disponibles.

## ¿Qué aprendimos con este proyecto?

Durante el desarrollo de este simulador pudimos comprender mejor varios temas que habíamos estudiado en clase.

Aprendimos cómo se organizan los procesos para utilizar el procesador, por qué es importante controlar el acceso a los recursos compartidos y cómo pueden ocurrir bloqueos cuando varios procesos necesitan los mismos recursos.

También entendimos mejor cómo funciona la asignación de memoria RAM y qué sucede cuando no hay suficiente espacio disponible.

Otra parte importante fue aprender a organizar nuestro código en diferentes archivos y después unirlos para que funcionaran desde un mismo programa.

Aunque nuestro simulador no controla directamente el sistema operativo de la computadora, nos permitió representar de una forma sencilla varios de los mecanismos que utiliza un kernel.

## Integrantes del proyecto

Este proyecto fue desarrollado para el curso de Sistemas Operativos.

- Integrante 1(Edwin Daniel Monterroso Tupul): desarrollo de la planificación Round Robin e integración del simulador.
- Integrante 2(Henry Alexander Mendoza Ortiz): desarrollo del módulo de semáforo binario.
- Integrante 3(César Alex Gilberto López Bulnes): pruebas y documentación del proyecto.

## Repositorio de GitHub

Aquí se encuentra el código de nuestro proyecto:

https://github.com/emonterrosot1-glitch/simulador-kernel-so