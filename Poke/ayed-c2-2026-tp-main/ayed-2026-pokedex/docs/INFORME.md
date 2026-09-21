# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Pokedex
- Por qué lo eligieron (5–8 líneas): Elegimos el tema pokedex porque nos interesa y gusta un catagolo de pokemo y sus estad, parece un tema mas claro y entretenido para aplicar los conceptos de algoritmos y estructuras de datos. Además, permite organizar información de cada Pokémon de manera sencilla y el catálogo nos permitirá realizar búsquedas, ordenamientos y diferentes operaciones a medida que avancemos con las entregas, también consideramos que es un dominio fácil de comprender y de utilizar para demostrar los conceptos aprendidos durante la materia en un juego popular y lo hace mas llevadero y divertido.

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

```markdown
## 2. Modelo

Cada ítem del catálogo representa un Pokémon con datos como identificador, nombre, tipos, puntos de vida, ataque, defensa, velocidad y generación.

El catálogo es una lista mutable porque puede modificarse agregando, eliminando o cambiando elementos. Los datos de cada Pokémon se representan mediante diccionarios, que también son estructuras mutables.

Los valores individuales como el identificador, el nombre y las estadísticas se almacenan como datos simples. Los textos y números son inmutables en Python.

Durante las próximas entregas, el catálogo se relacionará con una colección principal de Pokémon, una pila para representar el historial y una cola para administrar elementos pendientes.

```text
Catálogo
   |
   +----> Pokémon 1
   +----> Pokémon 2
   +----> Pokémon 3
   |
   +----> Colección principal
   |
   +----> Pila (historial)
   |
   +----> Cola
```

## 3. Recursión (E2)

- Función:
- Caso base:
- Caso recursivo:
- Traza de un ejemplo real del dataset:

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
