class Equipo:

    def __init__(self):
        self.pokemones = []

    def agregar(self, pokemon):
        self.pokemones.append(pokemon)

    def listar(self):
        return self.pokemones