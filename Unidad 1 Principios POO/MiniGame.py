from Model.Personaje import Personaje

p1 = Personaje("Player 1", 100, 100, "Fuego", 0)
p2 = Personaje("Player 2", 100, 100, "Agua", 0)
turno = 1

while True:
    #Limpiar Consola
    import os
    os.system("cls")

    if turno % 2 != 0: 
        jugadorTurno = p1
        jugadorEspera = p2
    else: 
        jugadorTurno = p2
        jugadorEspera = p1 

    print(f"Turno: {turno}")
    print(f"Jugador de Turno: {jugadorTurno.getNombre()}\n")

    print(f"Stats: {p1.getStats()}\n")   
    print(f"Stats: {p2.getStats()}\n")

    print("[1] - Atacar\n")
    print("[2] - Comprar\n")

    jugada = input("Selecciona tu Jugada: ")

    if(jugada == "1"):
        jugadorTurno.Atacar(jugadorEspera)
        input("Ataque Exitoso! Presiona Enter para Continuar...")

    if(jugada == "2"):
        os.system("cls")
        import Tienda
        indice = 1
        for i in Tienda.Tiendita:
            print(f"{indice} - {i.getStats()}")
            indice+=1
        opcion = int(input("\nSelecciona el Item a Comprar: "))

        jugadorTurno.Comprar(Tienda.Tiendita[opcion-1])
        input("Item Comprado!")


    input("Turno Terminado! Presiona Enter para Continuar...")
    turno += 1