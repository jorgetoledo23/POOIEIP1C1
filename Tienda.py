from Model.Item import Item

Item1 = Item("Espada", 0, 100, 0, 600)
Item2 = Item("Daga", 0, 50, 0, 350)
Item3 = Item("Escudo", 100, 0, 10, 300)
Item4 = Item("Armadura", 30, 0 , 30, 200)
Item5 = Item("Pocion de Fuerza", 0, 30, 0, 100)
Item6 = Item("Pocion de Vida", 30, 0, 0, 100)
Item7 = Item(nombre="Arco", fuerza=75, coste=500, vida=0, armadura=0)
Item8 = Item("Mascota", 20,20,20, 100)

Tiendita = []

Tiendita.append(Item1)
Tiendita.append(Item2)
Tiendita.append(Item3)
Tiendita.append(Item4)
Tiendita.append(Item5)
Tiendita.append(Item6)
Tiendita.append(Item7)
Tiendita.append(Item8)

# for i in Tiendita:
#     print(i.getStats())

