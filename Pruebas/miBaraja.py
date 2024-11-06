from baraja import Baraja

mibaraja = Baraja()
#mibaraja.mostrarCartas()

#mibaraja.barajar()
#mibaraja.mostrarCartas()

if mibaraja.quedanCartas():
    print("Hay cartas")
else:
    print("No hay cartas")

while mibaraja.quedanCartas():
    carta = mibaraja.sacarCarta()
    numCartas = mibaraja.contar()
    print(f"{carta} Quedan {numCartas}")