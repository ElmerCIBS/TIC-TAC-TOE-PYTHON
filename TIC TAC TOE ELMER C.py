# Para el juego, usamos " " para espacio vacío
tablero = [[" " for i in range(3)] for j in range(3)]

def mostrar_bienvenida():
    print("***************************")
    print("* VAMOS A JUGAR GATOOOO :)*")
    print("* Proyecto Final Python  1*")
    print("***************************")

def mostrar_tablero_referencia():
    print("\nEste es el tablero de referencia (1-9):")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")

def imprimir_tablero():
    # Tablero con las jugadas actuales
    print(f"\n {tablero[0][0]} | {tablero[0][1]} | {tablero[0][2]} ")
    print("---+---+---")
    print(f" {tablero[1][0]} | {tablero[1][1]} | {tablero[1][2]} ")
    print("---+---+---")
    print(f" {tablero[2][0]} | {tablero[2][1]} | {tablero[2][2]} \n")

def verificar_ganador():
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] and tablero[i][0] != " ":
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] != " ":
            return tablero[0][i]
    
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
        return tablero[0][2]
    
    if not any(" " in fila for fila in tablero):
        return "EMPATE"
    return "SIGUE JUGANDO VAMOS!!"

def validar_jugada(posicion, jugador):
    mapeo = {
        "1": (0, 0), "2": (0, 1), "3": (0, 2),
        "4": (1, 0), "5": (1, 1), "6": (1, 2),
        "7": (2, 0), "8": (2, 1), "9": (2, 2)
    }
    
    if posicion in mapeo:
        f, c = mapeo[posicion]
        if tablero[f][c] == " ":
            tablero[f][c] = jugador
            return True
        else:
            print("ESA POSICION ESTA OCUPADA ELIJE OTRA VAMOS!!.")
    else:
        print("ESA POSICION NO ES LOGICA, ELIJE OTRA VAMOS !!, ELIJE UNA DEL 1 AL 9.")
    return False

def juego():
    mostrar_bienvenida()
    
    while True: # Bucle para reiniciar todo el juego
        # Limpiar tablero al iniciar una nueva partida
        for f in range(3):
            for c in range(3):
                tablero[f][c] = " "
        
        mostrar_tablero_referencia()
        jugador = "X"
        primera_jugada = True 
        
        while True:
            if not primera_jugada:
                imprimir_tablero()
            
            pos = input(f"Jugador {jugador}, elige una posición (1-9): ")
            
            if validar_jugada(pos, jugador):
                primera_jugada = False 
                
                estado = verificar_ganador()
                if estado == "X" or estado == "O":
                    imprimir_tablero()
                    print(f"¡EL GANADOR ES: {estado}!")
                    break
                elif estado == "EMPATE":
                    imprimir_tablero()
                    print("¡ES UN EMPATE!")
                    break
                
                jugador = "O" if jugador == "X" else "X"
        
        # Preguntar si desea jugar de nuevo
        otra = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
        if otra != 's':
            print("¡Gracias por jugar! Adiós.")
            break

if __name__ == "__main__":
    juego()
