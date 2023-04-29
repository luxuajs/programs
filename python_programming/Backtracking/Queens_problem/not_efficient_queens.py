# Here we created a program to solved the queen's problem

reinas = 0
N = 8
encontrada = False


solucion = [0 for i in range(8)]

def columna_libre(col_a, col_p):
    # col_a = columna anterior (reina anterior)
    # col_p = columna posterio (reina actual)
    if(col_a == col_p):
        return False
    else:
        return True

def diagonal_libre(fila_a, col_a, fila_p, col_p):
    if(abs(fila_p - fila_a) == abs(col_p - col_a)):
        return False
    else:
        return True

def verificar(fila, col):
    for i in range(fila):
        if(not columna_libre(solucion[i], col) or not diagonal_libre(i, solucion[i], fila, col)):
            return False
    return True


def reinas_en_tablero(solucion, reinas, fila=0):
    # La fila por default empieza en cero

    global encontrada
    # Variables internas
    col = 0
    while(not encontrada and col < N):
        # Alternativa posible
        flag = verificar(fila, col)
        if(flag):
            # Registramos el paso
            solucion[fila] = col
            reinas += 1
        
            if(reinas != N):
                reinas_en_tablero(solucion, reinas, fila + 1)
                if(not encontrada):
                    # Borrar paso
                    solucion[fila] = 0
                    reinas -= 1
            else:
                encontrada = True
                for i in range(8):
                    print(f"Reina {i+1} --- fila: {i+1} | columna {solucion[i]+1}" )

        col += 1
        
reinas_en_tablero(solucion, reinas)

    

