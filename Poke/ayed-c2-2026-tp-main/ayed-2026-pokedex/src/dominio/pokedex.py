class Pokedex:

    def __init__(self):
        self.pokemones = []
        self.evoluciones = {}

    def agregar(self, pokemon):
        self.pokemones.append(pokemon)

    def buscar(self, id_pokemon):
        for pokemon in self.pokemones:
            if pokemon.id == id_pokemon:
                return pokemon
        return None

    def siguiente_evolucion(self, id_pokemon):
        return self.evoluciones.get(id_pokemon)

    def cadena_evolucion(self, id_pokemon):
        pokemon = self.buscar(id_pokemon)

        # CASO BASE
        if pokemon is None:
            return []

        siguiente = self.siguiente_evolucion(id_pokemon)

        # CASO BASE
        if siguiente is None:
            return [id_pokemon]

        # CASO RECURSIVO
        return [id_pokemon] + self.cadena_evolucion(siguiente)