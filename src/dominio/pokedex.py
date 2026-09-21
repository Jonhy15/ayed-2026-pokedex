class Pokemon:
def __init__(self, nombre, hp, ataque):
self.nombre = nombre
self.hp = hp
self.ataque = ataque
def resumen(self):
return f"{self.nombre} (hp {self.hp})
