import random

# Variables globales del juego
vida = 100
puntuacion = 0
armadura = 50

def mostrar_estado():
    """Muestra el estado actual del jugador."""
    print(f"vida: {vida}")
    print(f"puntuacion: {puntuacion}")
    print(f"armadura: {armadura}")

def explorar_habitacion():
    """Simula la exploración de una habitación y los eventos que pueden ocurrir."""
    global vida

    enemigo_presente = random.choice([True, False])

    if enemigo_presente:
        print("Enemigo encontrado en la habitación.")
        hablar_con_profesor()
    else:
        print("La habitación está vacía. Sigue explorando.")

def hablar_con_profesor():
    """Simula un encuentro con un profesor que realiza una pregunta de multiplicación."""
    global vida, puntuacion

    print("Te encuentras con un profesor de matemáticas en la habitación.")
    print("El profesor te pregunta sobre las tablas de multiplicar.")

    respuesta_correcta = False

    while not respuesta_correcta and vida > 0:
        multiplicador = random.randint(1, 10)
        multiplicando = random.randint(1, 10)
        resultado_esperado = multiplicador * multiplicando

        respuesta = input(f"¿Cuánto es {multiplicando} X {multiplicador}?: ")

        if respuesta.isdigit() and int(respuesta) == resultado_esperado:
            print("¡Respuesta correcta! El profesor te da 20 puntos.")
            puntuacion += 20
            respuesta_correcta = True
        else:
            print("Respuesta incorrecta. Perdiste 10 de vida. Tienes una nueva oportunidad.")
            vida -= 10

def evento_aleatorio():
    """Genera un evento aleatorio durante la exploración."""
    global vida, puntuacion, armadura

    evento = random.choice(['Encontraste un cofre con tesoros', 'Te caíste y perdiste vida', 'Descubriste un atajo seguro'])

    if evento == 'Encontraste un cofre con tesoros':
        print("Encontraste un cofre con tesoro. Obtuviste 20 puntos.")
        puntuacion += 20
    elif evento == 'Te caíste y perdiste vida':
        print("Perdiste 10 de vida y 10 de armadura.")
        vida -= 10
        armadura -= 10
    elif evento == 'Descubriste un atajo seguro':
        print("Has encontrado un atajo seguro que te lleva a la habitación del jefe final.")
        jugar_piedra_papel_tijera()

def jugar_piedra_papel_tijera():
    """Simula un juego de piedra, papel o tijeras contra el jefe final."""
    global puntuacion

    print("\nHas llegado a la habitación del jefe final.")
    print("El jefe final te desafía a un juego de piedra, papel o tijeras.")

    opciones = ['piedra', 'papel', 'tijeras']

    while True:
        eleccion_jugador = input("Elige tu jugada (piedra, papel o tijeras): ").lower()
        eleccion_jefe = random.choice(opciones)

        print(f"El jefe elige {eleccion_jefe}.")

        if eleccion_jugador == eleccion_jefe:
            print("Es un empate. Inténtalo de nuevo.")
        elif (eleccion_jugador == 'piedra' and eleccion_jefe == 'tijeras') or \
             (eleccion_jugador == 'papel' and eleccion_jefe == 'piedra') or \
             (eleccion_jugador == 'tijeras' and eleccion_jefe == 'papel'):
            print("¡Ganaste!")
            puntuacion += 100
            break
        else:
            print("Perdiste. El jefe final te derrotó.")
            print("El juego comenzará de nuevo.")
            reiniciar_juego()
            break

def reiniciar_juego():
    """Reinicia el juego a los valores iniciales."""
    global vida, puntuacion, armadura
    vida = 100
    puntuacion = 0
    armadura = 50

def jugar_juego():
    """Función principal para jugar el juego."""
    global vida, puntuacion, armadura

    while vida > 0:
        print("\nTe encuentras en un pasillo del castillo.")
        mostrar_estado()

        opcion = input("¿Qué deseas hacer? \n1. Entrar en una habitación\n2. Seguir explorando\n3. Consultar el estado\n4. Salir del juego\nElige una opción (1/2/3/4): ")

        if opcion == '1':
            explorar_habitacion()
        elif opcion == '2':
            evento_aleatorio()
        elif opcion == '3':
            mostrar_estado()
        elif opcion == '4':
            print("Decidiste salir del juego.")
            break
        else:
            print("Opción no válida.")

        if vida <= 0:
            print("\nHas perdido.")
            mostrar_estado()
        elif puntuacion >= 100:
            print("¡Felicidades! Has ganado el juego.")
            mostrar_estado()
            break
        elif armadura <= 0:
            print("Armadura rota.")
            mostrar_estado()
            break

# Inicia el juego
jugar_juego()
