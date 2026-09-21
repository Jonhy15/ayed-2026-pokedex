catalogo = [
    {
        "id": 1,
        "nombre": "Bulbasaur",
        "tipo1": "Planta",
        "tipo2": "Veneno",
        "hp": 45,
        "ataque": 49,
        "defensa": 49,
        "velocidad": 45,
        "generacion": 1
    },
    {
        "id": 2,
        "nombre": "Ivysaur",
        "tipo1": "Planta",
        "tipo2": "Veneno",
        "hp": 60,
        "ataque": 62,
        "defensa": 63,
        "velocidad": 60,
        "generacion": 1
    },
    {
        "id": 3,
        "nombre": "Venusaur",
        "tipo1": "Planta",
        "tipo2": "Veneno",
        "hp": 80,
        "ataque": 82,
        "defensa": 83,
        "velocidad": 80,
        "generacion": 1
    },
    {
        "id": 4,
        "nombre": "Charmander",
        "tipo1": "Fuego",
        "tipo2": None,
        "hp": 39,
        "ataque": 52,
        "defensa": 43,
        "velocidad": 65,
        "generacion": 1
    },
    {
        "id": 5,
        "nombre": "Charmeleon",
        "tipo1": "Fuego",
        "tipo2": None,
        "hp": 58,
        "ataque": 64,
        "defensa": 58,
        "velocidad": 80,
        "generacion": 1
    },
    {
        "id": 6,
        "nombre": "Charizard",
        "tipo1": "Fuego",
        "tipo2": "Volador",
        "hp": 78,
        "ataque": 84,
        "defensa": 78,
        "velocidad": 100,
        "generacion": 1
    },
    {
        "id": 7,
        "nombre": "Squirtle",
        "tipo1": "Agua",
        "tipo2": None,
        "hp": 44,
        "ataque": 48,
        "defensa": 65,
        "velocidad": 43,
        "generacion": 1
    },
    {
        "id": 8,
        "nombre": "Wartortle",
        "tipo1": "Agua",
        "tipo2": None,
        "hp": 59,
        "ataque": 63,
        "defensa": 80,
        "velocidad": 58,
        "generacion": 1
    },
    {
        "id": 9,
        "nombre": "Blastoise",
        "tipo1": "Agua",
        "tipo2": None,
        "hp": 79,
        "ataque": 83,
        "defensa": 100,
        "velocidad": 78,
        "generacion": 1
    },
    {
        "id": 10,
        "nombre": "Pikachu",
        "tipo1": "Eléctrico",
        "tipo2": None,
        "hp": 35,
        "ataque": 55,
        "defensa": 40,
        "velocidad": 90,
        "generacion": 1
    }
]
class Pokemon:
def __init__(self, nombre, hp, ataque):
self.nombre = nombre
self.hp = hp
self.ataque = ataque
def resumen(self):
return f"{self.nombre} (hp {self.hp})
