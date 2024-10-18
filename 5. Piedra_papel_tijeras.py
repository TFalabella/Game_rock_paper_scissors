#Programa un simple juego de piedra, papel o tijera
# donde el usuario juegue contra la computadora
# (usando la función random para generar la elección de la computadora).


#Pedir al usuario que ingrese su eleccion: (Piedra, Papel, Tijera) o (1,2,3).

#Generar aleatoreamente una eleccion del ordenador.

#Comparar las elecciones y marcar quien gana, definiendo de ante mano y usando luego if.

#Mostrar el resultado y preguntar si quiere hacer otra ronda más.

import random
import time

gestos = ['piedra', 'papel', 'tijera'] #Lista de opciones a seleccionar

# gesto_aleatorio = random.choice(gestos) #Aca le estamos diciendo a la funcion random.choice
                                        # que busque dentro de esa lista y devuelva una opcion.



ppt = True
while ppt:
    print ("\n>>> Haz tu elección <<<")
#    print ("\n(Piedra - Papel - Tijeras - Salir)")
#    print ("\n1. Piedra.")
#    print ("\n2. Papel.")
#    print ("\n3. Tijeras.")
#    print ("\n4. Salir.")

    eleccion = input ("\nPiedra  \nPapel  \nTijera  \nSalir\n\n>>>").strip().lower()

    if eleccion == 'salir': #usar la comparacion en minusculas ya que estoy usando strip y lower.
                ppt = False
                print ("Saliendo...")
                time.sleep(2)
                break
    
    if eleccion not in gestos:  # Validación si la elección no es válida
        print("Opción no válida. Por favor, elige 'piedra', 'papel', 'tijera' o 'salir'.")
        continue

    gesto_aleatorio = random.choice(gestos) #para que sea siempre diferente se debe usar dentro del bucle
    
    print (f"\nTu elección es: {eleccion}")

    print (f"El ordenador elige: {gesto_aleatorio}") #Si uso "gesto_aleatorio"
                                                                      #siempre repite el mismo.

    if eleccion == gesto_aleatorio:
        print("\n**¡Empate! Habrá que intentarlo de nuevo...**") #depende la terminal los **ponen en negrita
    elif (eleccion == 'piedra' and gesto_aleatorio == 'tijera') or \
         (eleccion == 'papel' and gesto_aleatorio == 'piedra') or \
         (eleccion == 'tijera' and gesto_aleatorio == 'papel'):
        print("\n**¡¡¡Ganaste!!!**")
    else:
        print("\n**Jaja ¡Perdiste! Mejor suerte la proxima.**")

    time.sleep(1)
    print (f"\n¿Te atreves a otra?")
    time.sleep(1.5)   

 
 
            


           