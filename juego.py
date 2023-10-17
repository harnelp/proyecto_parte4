from typing import List, Tuple
import os

# 1. Función para convertir el mapa de cadena a matriz.
def convertir_mapa(laberinto: str) -> List[List[str]]:
    # Divide el laberinto por líneas y convierte cada línea en una lista de caracteres
    return [list(linea) for linea in laberinto.split("\n")]

# 2. Función para limpiar la pantalla y mostrar la matriz.
def mostrar_mapa(mapa: List[List[str]]):
    # Limpia la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Muestra el mapa
    for linea in mapa:
        print(''.join(linea))

# 3. Función principal que implementa el bucle principal del juego.
def main_loop(mapa: List[List[str]], pos_inicial: Tuple[int, int], pos_final: Tuple[int, int]):
    # Inicializa las coordenadas del jugador
    px, py = pos_inicial

    # Bucle principal del juego
    while (px, py) != pos_final:
        mostrar_mapa(mapa)
        
        # Recibe la entrada del usuario para moverse
        key = input("Usa las teclas WASD para moverte: ").lower()
        
        # Define las coordenadas tentativas basadas en la entrada del usuario
        tx, ty = px, py
        if key == 'w':  # arriba
            tx -= 1
        elif key == 's':  # abajo
            tx += 1
        elif key == 'a':  # izquierda
            ty -= 1
        elif key == 'd':  # derecha
            ty += 1

        # Verifica si la nueva posición es válida
        if (0 <= tx < len(mapa) and 0 <= ty < len(mapa[0]) and mapa[tx][ty] != '#'):
            # Restaura la posición anterior a un punto
            mapa[px][py] = '.'
            # Actualiza las coordenadas del jugador
            px, py = tx, ty
            # Coloca al jugador en la nueva posición
            mapa[px][py] = 'P'

    print("¡Has llegado al final del laberinto!")

# Código principal
laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

# Convierte la cadena del laberinto a una matriz
mapa = convertir_mapa(laberinto)

# Define las coordenadas de inicio y fin
inicio = (0, 0)
final = (len(mapa)-1, len(mapa[0])-1)

# Coloca al jugador en la posición de inicio
mapa[inicio[0]][inicio[1]] = 'P'

# Inicia el bucle principal del juego
main_loop(mapa, inicio, final)
