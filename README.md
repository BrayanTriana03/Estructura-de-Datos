# Clases de Estructura de Datos
En este espacio abarcaremos todas las clases he investigaciones que se hagan sobre **Estructura de Datos**
## Clase1 - Codigo Sistema de Calificación
#09/08/2026

#Clase 3 (Reposición)

#Ejercicio 1 - Sistema de Calificaciones con Estadísticas
#Parte A - Entrada de Datos
#   1. Preguntar al usuario cuántos estudiantes va a ingresar 
#   2. Por cada estudiante, pedir:
#       2.1. Nombre completo (no puede estar vacío).
#       2.2. Tres notas parciales (números entre 0.0 y 5.0).
#   3.	Validar que cada nota esté en el rango correcto; si no, volver a pedirla.       

#Parte B - Procesamiento
#   1. Calcular para cada estudiante:
#       1.1 Nota final
#       1.2 Estado (Aprovado, Reprobado)
#       1.3 Clasificación
#           1.3.1 Nota final ≥ 4.5: "Excelente"
#   	    1.3.2 Nota final entre 4.0 y 4.49: "Sobresaliente"
#           1.3.3 Nota final entre 3.0 y 3.99: "Aceptable"
#           1.3.4 Nota final < 3.0: "Insuficiente"
#   2. Calcular estadísticas generales
#       2.1. Promedio del curso.
#       2.2. Número y porcentaje de aprobados y reprobados.
#       2.3. Nota más alta y nombre del estudiante que la obtuvo.
#       2.4. Nota más baja y nombre del estudiante que la obtuvo.
#       2.5. Cantidad de estudiantes en cada clasificación.

#Parte C - Salida Formateada
#   1. Reporte completo
#       1.1 Lista de estudiantes con nombre, nota final y clasificación.
#       1.2 Resumen estadístico al final.
#       1.3 Usar bordes y alineación para que sea legible.

#Parte D - Búsqueda
#Permitir al usuario buscar un estudiante por nombre parcial 

#Parte A - Entrada de Datos

def menu():
    continuar = True

    while continuar:
        print("----------------------------------------------------------------")
        print("Bienvenido usuario al sistema de califición automatizado")
        print("----------------------------------------------------------------")
        print("Opción a elegir")
        print("1 - Ingresar estudiantes")
        print("2 - Buscar estudiantes")
        print("3 - Terminar programa")

        eleccion = int(input())
        
        if eleccion == 1:
            dicc_est = {}

            dicc_est_act, num_estudiantes = ingreso_estudiantes(dicc_est)

            dicc_est_procesado, lista_resultados = procesamiento(dicc_est_act, num_estudiantes)

            exposicion(dicc_est_procesado, lista_resultados)
            
        elif eleccion == 2:
            busqueda(dicc_est_procesado)

        elif eleccion == 3:
            continuar = False

        else:
            print("Respuesta inválida")

def busqueda(dicc_est_procesado):
    print("¿Cuál es el nombre del estudiante")
    nombre_bus = input()

    encontrado = False

    for nombre_est, lista_resultados_est in dicc_est_procesado.items():
        if nombre_bus in nombre_est:
            nota_final = str(lista_resultados_est[0])
            clasificación = lista_resultados_est[2]
            print("//////////////////////////////////////////////////////////////////")
            print("Nombre - Nota Final - Clasificación")
            print("//////////////////////////////////////////////////////////////////") 

            print(nombre_est + " - " + nota_final + " - " + clasificación)

            encontrado = True

    if not encontrado:
        print("No se encontro estudiante")



def ingreso_estudiantes(dicc_est: dict):
    print("¿Cuánto estudiantes desea ingresar al curso?")
    num_estudiantes = int(input())

    for i in range(1, num_estudiantes + 1):

        resp_correcta = False
        while not resp_correcta:
            print("Nombre del estudiante:")
            nombre = input()
        
            if nombre == "":
                print("Respuesta invalida")
            else:
                resp_correcta = True

        resp_correcta = False
        while not resp_correcta:
            print("Nota parcial 1:")
            nota_parcial_1 = float(input())

            if 0 <= nota_parcial_1 and nota_parcial_1 <= 5:
                resp_correcta = True
            else:
                print("Respuesta invalida")


        resp_correcta = False
        while not resp_correcta:
            print("Nota parcial 2:")
            nota_parcial_2 = float(input())

            if 0 <= nota_parcial_2 and nota_parcial_2 <= 5:
                resp_correcta = True
            else:
                print("Respuesta invalida")

        resp_correcta = False
        while not resp_correcta:
            print("Nota parcial 3:")
            nota_parcial_3 = float(input())

            if 0 <= nota_parcial_3 and nota_parcial_3 <= 5:
                resp_correcta = True
            else:
                print("Respuesta invalida")


        lista_notas = [nota_parcial_1, nota_parcial_2, nota_parcial_3]
        dicc_est[nombre] = lista_notas

    return dicc_est, num_estudiantes

def procesamiento(dicc_est_act: dict, num_estudiantes: int):
    dicc_est_procesado = {}

    suma_notas = 0
    lista_estado = [0,0]
    lista_clasificacion = [0,0,0,0]
    lista_mejor_est = ["nombre", -1]
    lista_peor_est = ["nombre", 6]
    
    for nombre, lista_notas in dicc_est_act.items():
        parcial_1 = lista_notas[0]
        parcial_2 = lista_notas[1]
        parcial_3 = lista_notas[2]

        nota_final = (parcial_1 + parcial_2 + parcial_3)/3

        nota_final = round(nota_final, 2)

        nota_mejor_est = lista_mejor_est[1]
        nota_peor_est = lista_peor_est[1]

        if nota_mejor_est <= nota_final:
            lista_mejor_est[0] = nombre
            lista_mejor_est[1] = nota_final
        
        if nota_final <= nota_peor_est:
            lista_peor_est[0] = nombre
            lista_peor_est[1] = nota_final

        if 3 <= nota_final:
            estado = "Aprobado"
            lista_estado[0] += 1
        else:
            estado = "Reprobado"
            lista_estado[1] += 1

        if 4.5 <= nota_final:
            clasificacion = "Excelente"
            lista_clasificacion[0] += 1

        elif 4.0 <= nota_final and nota_final < 4.5:
            clasificacion = "Sobresaliente"
            lista_clasificacion[1] += 1

        elif 3.0 <= nota_final and nota_final < 4:
            clasificacion = "Aceptable"
            lista_clasificacion[2] += 1

        else:
            clasificacion = "Insuficiente"
            lista_clasificacion[3] += 1

        lista_resultados_est = [nota_final, estado, clasificacion]
        dicc_est_procesado[nombre] = lista_resultados_est

    
    promedio_general = suma_notas/num_estudiantes

    lista_resultados = [promedio_general, lista_estado, lista_clasificacion, lista_mejor_est, lista_peor_est]

    return dicc_est_procesado, lista_resultados


def exposicion(dicc_est_procesado: dict, lista_resultados: list):
    print("//////////////////////////////////////////////////////////////////")
    print("Resultados Académicos")
    print("//////////////////////////////////////////////////////////////////")
    print("Nombre - Nota Final - Clasificación")
    print("//////////////////////////////////////////////////////////////////")

    for nombre, lista_resultados_est in dicc_est_procesado.items():
        nota_final = str(lista_resultados_est[0])
        clasificación = lista_resultados_est[2]

        print(nombre + " - " + nota_final + " - " + clasificación)
        print("---------------------------------------------------------------------")
    promedio_general = lista_resultados[0]
    lista_estado =  lista_resultados[1]
    num_aprobados = lista_estado[0]
    num_reprobados = lista_estado[1]
    
    num_total_est = num_aprobados + num_reprobados

    porc_aprobados = (num_aprobados/num_total_est)*100
    porc_reprobados = (num_reprobados/num_total_est)*100

    mejor_est = lista_resultados[3]
    nom_mejor_est = mejor_est[0]
    nota_mejor_est = mejor_est[1]

    peor_est = lista_resultados[4]
    nom_peor_est = peor_est[0]
    nota_peor_est = peor_est[1]

    lista_clasificacion = lista_resultados[2]
    num_exc = str(lista_clasificacion[0])
    num_sob = str(lista_clasificacion[1])
    num_acep = str(lista_clasificacion[2])
    num_inc = str(lista_clasificacion[3])

    print("---------------------------------------------------------------------")
    print("Información general:")
    print("Promedio global:" + str(promedio_general))
    print("----------------------")
    print("Estadisticas de estado:")
    print("Aprobaron " + str(num_aprobados) + " (" + str(round(porc_aprobados,2)) + "%) ")
    print("Reprobaron " + str(num_reprobados) + " (" + str(round(porc_reprobados,2)) + "%) ")
    print("----------------------")
    print("El mejor estudiante fue " + nom_mejor_est + " con una nota de " + str(nota_mejor_est))
    print("----------------------")
    print("El peor estudiante fue " + nom_peor_est + " con una nota de " + str(nota_peor_est))
    print("----------------------")
    print("Cantidad de estudiantes por clasificación:")
    print("- Excelente: " + num_exc)
    print("- Sobresaliente: " + num_sob)
    print("- Aceptable: " + num_acep)
    print("- Inaceptable: " + num_inc)

menu()

#menu() -> Condicional -> Proceso
#                      -> Busco 
#                      -> Terminar


# Vista - Menu & Exposición
# Controlador - Secuencia de funciones
# Modelo - Proceso, busco

# Clase 2 juego 

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
 

