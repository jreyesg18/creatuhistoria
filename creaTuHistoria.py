import random

vida = 100
puntuacion = 0
armadura = 50

def mostrar_estado():
    print(f"vida: {vida}")
    print(f"puntuacion: {puntuacion}")
    print(f"armadura: {armadura}")

def explorar_habitacion():

    global vida

    enemigo_presente = random.choice([True, False])

    if enemigo_presente:
        print("Enemigo encontrado en la habitacion: ")
        hablar_con_profesor()
    else:
        print("La habitacion esta vacia. Sigue explorando")

def hablar_con_profesor():

    global vida, puntuacion

    print("Te encuentras con un profesor de matematicas en la habitacion")
    print('El profesor te pregunta sobre las tablas de multiplicar')

    respuesta_correcta = False

    while not respuesta_correcta and vida > 0:

        multiplicador = random.randint(1,10)
        multiplicando = random.randint(1, 10)
        resultado_esperado = multiplicador * multiplicador

        respuesta = input(f'cuanto es {multiplicando} X {multiplicador}?: ')

        if respuesta.isdigit() and int(respuesta) == resultado_esperado:
            print('Respuesta correcta!. El profesor te da 2- puntos')
            puntuacion += 20
            respuesta_correcta=True
        else:
            print("Respuesta incorrecta. Perdiste 10 de vida, Tienes una nueva oportunidad")
            vida -= 10

def evento_aleatorio():
    global vida, puntuacion, armadura

    evento = random.choice(['Encontraste un cofre con tesoros','Te caiste y perdiste otra vida','Descubriste un atajo seguro'])

    if evento == 'Encontraste un cofre con tesoros':
        print("Encontraste un cofre con tesoro. Obtuviste 20 puntos")
        puntuacion += 20
    elif evento == 'Te caiste y perdiste otra vida':
        print("perdiste-10 de vida y -10 de armadura")
        vida -= 10
        armadura -= 10
    elif evento == 'Descubriste un atajo seguro'
        print('Has encontrado un atajo seguro que te lleva a la habitacion del jefe final.')
        jugar_piedra_papel_tijera()

def jugar_piedra_papel_tijera():

    global puntuacion

    print("\nHas llegado a la habitacion del jefe final.\nEl jefe final te desafia a un papel, piedra, tijera")

    opciones = ['piedra', 'papel', 'tijeras']

    while True:
        eleccion_jugador = input('Elige tu jugada (Piedra, papel o tijera): '.lower())
        eleccion_jefe = random.choice(opciones)

        print(f'el jefe elige {eleccion_jefe}.')

        if eleccion_jugador == eleccion_jefe:
            print('Es un empate. Intentalo de nuevo')

        elif(eleccion_jugador == 'piedra' and eleccion_jefe == 'tijeras') or \
            (eleccion_jugador == 'papel' and eleccion_jefe == 'piedra') or \
            (eleccion_jugador == 'tijeras' and eleccion_jefe == 'papel'):
            print("Ganaste")
            puntuacion +=100
            break
        else:
            print('Perdiste. El jefe final te derroto')
            print('El juego comenzara de nuevo')
            reiniciar_juego()
            break


def reiniciar_juego():
    global vida, puntuacion, armadura
    vida = 100
    puntuacion = 0
    armadura = 50


def jugar_juego():

    while vida > 0:

        print('\n Te encuentras en un pasillo del castillo')
        mostrar_estado()

        opcion = input('Que deseas hacer? \n 1.Entrar en una habitacion\n2.Seguir explorando\n3.Consultar de Estado\n 4. Salir del juego\nElija una opcion (1/2/3/4): ')

        if opcion == '1':
            explorar_habitacion()
        elif opcion == '2':
            evento_aleatorio()
        elif opcion == '3':
            mostrar_estado()
        elif opcion == '4':
            print('Decidiste salir del juego')
            break;
        else:
            print('Opcion no valida')

        if vida <= 0:
            print('\n Has perdido')
            mostrar_estado()
        elif puntuacion >= 100:
            print("Felicidades has ganado el juego")
            mostrar_estado()
            break:
        elif armadura <= 0:
            print("Armadura rota")
            mostrar_estado()
            break:

