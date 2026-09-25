import random

class Jugador:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

    def tirar(self):
        opciones = ["Izquierda", "Centro", "Derecha"]

        while True:
            op = input("1.Izquierda  2.Centro  3.Derecha: ")
            if op in ("1", "2", "3"):
                return opciones[int(op)-1]

class Partido:
    def __init__(self, j1, j2):
        self.j1 = j1
        self.j2 = j2
        self.goles1 = 0
        self.goles2 = 0

    def turno(self, jugador, num):
        for i in range(3):
            tiro = jugador.tirar()
            portero = random.choice(["Izquierda", "Centro", "Derecha"])

            if tiro != portero:
                print("¡GOOOL!")
                if num == 1:
                    self.goles1 += 1
                else:
                    self.goles2 += 1
            else:
                print("¡ATAJADA!")

            print(f"Marcador: {self.goles1} - {self.goles2}")

    def jugar(self):
        self.turno(self.j1, 1)
        self.turno(self.j2, 2)

        if self.goles1 > self.goles2:
            print("Gana Jugador 1")
        elif self.goles2 > self.goles1:
            print("Gana Jugador 2")
        else:
            print("Empate")

paises = {
    "1": "Guatemala",
    "2": "Argentina",
    "3": "Brasil",
    "4": "España",
    "5": "México"
}

p1 = paises.get(input("País Jugador 1: "), "Guatemala")
p2 = paises.get(input("País Jugador 2: "), "Guatemala")

j1 = Jugador("Jugador 1", p1)
j2 = Jugador("Jugador 2", p2)

Partido(j1, j2).jugar()