from carta import Carta

class Mano:
    def __init__(self):
        self.cartas = []
        self.valor = 0

    def añadirCarta(self,carta):
        self.cartas.append(carta)
        for carta in self.cartas:
            if carta.valor in ["Jota","Reina","Rey"]:
                self.valor = 10
            elif carta.valor == "As":
                self.valor += 11
            else:
                self.valor += int(carta.valor)
        return self.valor
    
    def mostrarMano(self):
        for carta in self.cartas:
            print(carta)
