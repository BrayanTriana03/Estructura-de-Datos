import controlador as ctrl

def estadisticas(lista_est: list, info_personaje: list, num_enemigos: int):
    num_enemigos_derrotados = lista_est[0]
    PV_restante = info_personaje[0]
    pociones_usada = lista_est[1]
    dano_inflingido = lista_est[2]
    print("")
    print("######################################################")
    print("Estadíticas del jugador")
    print("Enemigos totales: " + str(num_enemigos))
    print("Enemigos derrotados: " + str(num_enemigos_derrotados))
    print("PV restante: " + str(PV_restante))
    print("Pociones utilizada: " + str(pociones_usada))
    print("Daño inflingido: " + str(dano_inflingido))
    print("######################################################")



def mostar_personaje(info_personaje: list):
    PV_personaje= str(info_personaje[0])
    PV_max_personaje = str(info_personaje[1])
    ataque_personaje = str(info_personaje[2])
    num_pociones = str(info_personaje[3])
    prob_critico = str(info_personaje[4])

    print("")
    print("######################################################")
    print("Estado del personaje:")
    print("Puntos de vida (PV): " + PV_personaje)
    print("Puntos de vida máximo: " + PV_max_personaje)
    print("Puntos de ataque: " + ataque_personaje)
    print("Número de pociones: " + num_pociones)
    print("Probabilidad de daño crítico: " + prob_critico)
    print("######################################################")

def mostrar_info(info_personaje: list, info_enemigo: list):
    PV_personaje= str(info_personaje[0])
    PV_max_personaje = str(info_personaje[1])
    ataque_personaje = str(info_personaje[2])
    num_pociones = str(info_personaje[3])
    prob_critico = str(info_personaje[4])

    PV_enemigo = str(info_enemigo[0])
    ataque_enemigo = str(info_enemigo[1])

    print("")
    print("######################################################")
    print("Estado del personaje:")
    print("Puntos de vida (PV): " + PV_personaje)
    print("Puntos de vida máximo: " + PV_max_personaje)
    print("Puntos de ataque: " + ataque_personaje)
    print("Número de pociones: " + num_pociones)
    print("Probabilidad de daño crítico: " + prob_critico)
    print("######################################################")

    print("")
    print("######################################################")
    print("Estado del enemigo:")
    print("Puntos de vida (PV): " + PV_enemigo)
    print("Puntos de ataque: " + ataque_enemigo)
    print("######################################################")

def mostar_enemigos(lista_enemigos: list):
    n = 1

    for info_enemigo in lista_enemigos:
        PV_enemigo = str(info_enemigo[0])
        ataque_enemigo = str(info_enemigo[1])

        print("######################################################")
        print("Estado del enemigo " + str(n))
        print("Puntos de vida (PV): " + PV_enemigo)
        print("Puntos de ataque: " + ataque_enemigo)
        print("######################################################")
        n += 1
    
def menu_acciones():

    continuar = True

    while continuar:
        print("")
        print("////////////////////////////////////////////////////")
        print("Menu de acciones")
        print("////////////////////////////////////////////////////")
        print("Acciones:")
        print("1. Atacar")
        print("2. Usar poción")
        print("3. Intentar huir")
        print("4. Rendirse")
        print("")
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1" or opcion == "2" or opcion == "3" or opcion == "4":
            continuar = False
        else:  
            print("Ingrese un opción válida")

    return opcion

def menu_creacion_personaje():

    continuar = True

    while continuar:
        print("")
        print("////////////////////////////////////////////////////")
        print("Creación de personaje")
        print("////////////////////////////////////////////////////")
        print("Tipos de personaje:")
        print("1. Guerrero (+10 ataque, +20 PV máximos)")
        print("2. Mago (+15 ataque, pero -20 PV máximos)")
        print("3. Pícaro (0.15 de probabilidad de golpe crítico (doble daño))")
        print("")
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1" or opcion == "2" or opcion == "3":
            continuar = False
        else:  
            print("Opción válida")

    return opcion


def menu():
    continuar = True

    while continuar:
        print("")
        print("////////////////////////////////////////////////////")
        print("Bienvenido al juego de combate")
        print("////////////////////////////////////////////////////")
        print("Opciones diponibles:")
        print("1. Crear personaje")
        print("2. Jugar")
        print("3. Finalizar juego")
        print("")
        opcion = input("Ingrese una opción: ")

        # lista_est[0] = "Enemigos derrotados
        # lista_est[1] = "Pociones usadas"
        # lista_est[2] = "Daño total inflingido"

        lista_est = [0,0,0]

        if opcion == "1":
            opcion = menu_creacion_personaje()
            info_personaje = ctrl.crear_personaje(opcion)

            print("")
            print("////////////////////////////////////////////////////")
            print("Se creó el personaje:")
            mostar_personaje(info_personaje)
            print("////////////////////////////////////////////////////")

        elif opcion == "2":
            continuar_juego = True

            lista_enemigos = ctrl.crear_lista_enemigos()
            num_enemigos = len(lista_enemigos)
            contador = 0

            print("")
            print("////////////////////////////////////////////////////")
            print("Se creó la lista de enemigos:")
            mostar_enemigos(lista_enemigos)
            print("////////////////////////////////////////////////////")

            while continuar_juego and contador < num_enemigos:
                info_enemigo = lista_enemigos[contador]

                continuar_pelea_enemigo = True

                while continuar_pelea_enemigo:
                    opcion = menu_acciones()
                    continuar_pelea_enemigo, continuar_juego = ctrl.turno(opcion, info_personaje, info_enemigo, lista_est)
                    mostrar_info(info_personaje, info_enemigo)

                contador += 1

            print("---------------------------------------------------")
            print("Juego terminado")
            print("---------------------------------------------------")

            num_enemigos = len(lista_enemigos)
            estadisticas(lista_est, info_personaje, num_enemigos)
            
        elif opcion == "3":
            continuar = False
            print("---------------------------------------------------")
            print("Gracias por jugar")
            print("---------------------------------------------------")
        else:  
            print("Opción válida")


menu()