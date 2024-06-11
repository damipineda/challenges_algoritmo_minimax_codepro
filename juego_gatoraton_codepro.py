import random #Se importa random para generar movimientos aleatorios
import time #importamos time
#Definicion de tabler
tablero_medida = 5 #Medida del tablero
tablero = [['.'] * tablero_medida for _ in range(tablero_medida) ] #Creacion del tablero
#Posiciones
raton_posicion = (0, random.randint(0, tablero_medida -1))
gato_posicion = (-1,random.randint(1, tablero_medida -1))
numero_gato = random.randint(1,5)
numero_raton = random.randint(1,9)
#Actualizacion del tablero
raton_perfil = 'R'
gato_perfil = 'G'

#Posicion de jugadores
tablero[raton_posicion [0]][raton_posicion[1]] = raton_perfil
tablero[gato_posicion [0]][gato_posicion[1]] = gato_perfil

#imprimir tablero
def imprimir_tablero(tablero):
    for fila in tablero: #for anidado para imprimir correctamente el tablero
     print('.'.join(fila))
    print()
    
    #Funcion para mover al raton
def movimiento_raton(tablero, raton_posicion, movimiento):
    #obtener filas y columnas
    fila_actual, columna_actual = raton_posicion
    #Declaramos los movimientos
    if movimiento == 'arriba':
        fila_nueva = fila_actual -1
        columna_nueva = columna_actual
    elif movimiento == 'abajo':
        fila_nueva = fila_actual +1
        columna_nueva = columna_actual
    elif movimiento == 'izquierda':
        fila_nueva = fila_actual
        columna_nueva = columna_actual -1
    elif movimiento == 'derecha':
        fila_nueva = fila_actual
        columna_nueva = columna_actual +1
    else: #Si los movimietos no son validos no se mueve el raton
        return raton_posicion
    
    #Verificamos si el movimimiento es dentro del tablero
    
    if fila_actual < 0 or fila_nueva >= len(tablero) or columna_nueva < 0 or columna_nueva >= len(tablero):
        return (fila_nueva, columna_nueva)
    
    #Verificar que la nueva posicion esta vacia
    if tablero[fila_nueva][columna_nueva] != ".":
        return raton_posicion
    #Si la poscion esta ocupada no hacer nada
    
    #Actualizar la posicion en el tablero
    tablero[fila_actual][columna_actual]= "."
    tablero[fila_nueva][columna_nueva]= 'R'
    #Se actualiza la posicion del raton
    return(fila_nueva, columna_nueva)
    
        
  #Movimiento del gato (Turno)
  
def movimiento_gato(tablero, gato_posicion, movimiento):
    #optener filas y columnas
    fila_actual, columna_actual = gato_posicion
    #Declarramos los movimientos
    if movimiento == 'arriba':
        fila_nueva = fila_actual -1
        columna_nueva = columna_actual
    elif movimiento == 'abajo':
        fila_nueva = fila_actual +1
        columna_nueva = columna_actual
    elif movimiento == 'izquierda':
        fila_nueva = fila_actual
        columna_nueva = columna_actual -1
    elif movimiento == 'derecha':
        fila_nueva = fila_actual
        columna_nueva = columna_actual +1
    else: #Si los movimietos no son validos no se mueve el raton
        return gato_posicion
    #Verificamos si el movimimiento es dentro del tablero
    
    if fila_actual < 0 or fila_nueva >= len(tablero) or columna_nueva < 0 or columna_nueva >= len(tablero):
        return (fila_nueva, columna_nueva)
    
    #Verificar que la nueva posicion esta vacia
    if tablero[fila_nueva][columna_nueva] != ".":
        return gato_posicion
    #Si la poscion esta ocupada no hacer nada
    
    #Actualizar la posicion en el tablero
    tablero[fila_actual][columna_actual]="."
    tablero[fila_nueva][columna_nueva]= "G"
    
    #Se actualiza la posicion del raton
    return(fila_nueva, columna_nueva)


#Funcion para evaluar el tablero

def evaluar (tablero, raton_posicion, gato_posicion):
    return abs(raton_posicion[0] - gato_posicion[0]) + abs(raton_posicion[1] - gato_posicion[1])

#Movimientos posibles en el tablero
    #Funcion de movimiento del  juego
    #Actualizamos el tablero
def movimiento_posibles (tablero,posicion):
    fila, columna = posicion
    #Movimiento del raton
    movimientos = [(fila - 1, columna), (fila +1, columna), (fila, columna - 1), (fila, columna + 1)]
    return[(nueva_fila, nueva_columna) for nueva_fila, nueva_columna in movimientos if 0 <= nueva_fila < len(tablero) and 0 <= nueva_columna < len(tablero[0]) 
           and tablero[nueva_fila][nueva_columna]!= gato_perfil]

#Definimios la funcion minimax para que los jugadores puedan definir su mejor movimiento de forma inteligente

def minimax(tablero, profundidad, jugador_maximizador, raton_posicion, gato_posicion):
    if profundidad == 0 or raton_posicion == gato_posicion:
        return evaluar(tablero, raton_posicion, gato_posicion)
    
    if jugador_maximizador: #El jugador maximizador es el raton
        max_eval = float('-inf')
        for movimientos in  movimiento_posibles(tablero, raton_posicion):
            nueva_raton_posicion = movimientos
            eval = minimax(tablero, profundidad - 1, False, nueva_raton_posicion, gato_posicion)
            max_eval = max(max_eval, eval)
        return max_eval
    
    else: #El gano minimiza
        min_eval = float('inf')
        for movimientos in movimiento_posibles(tablero, gato_posicion):
            nueva_gato_posicion = movimientos
            eval = minimax(tablero, profundidad -1, True, raton_posicion, nueva_gato_posicion)
            min_eval = min(min_eval, eval)
        return min_eval
    
#En esta funcion se define los mejores movimientos para cada jugador

def mejor_movimiento(tablero, profundidad, jugador_maximizador, raton_posicion, gato_posicion):
    mejor_movimiento = None
    if jugador_maximizador:
        max_eval = float('-inf')
        for movimientos in movimiento_posibles(tablero, raton_posicion):
            nueva_raton_posicion = movimientos
            eval = minimax(tablero, profundidad -1, False, nueva_raton_posicion, gato_posicion)
            if eval > max_eval:
                max_eval = eval
                mejor_movimiento = movimientos

    else:
        min_eval = float('inf')
        for movimientos in movimiento_posibles(tablero, gato_posicion):
            nueva_gato_posicion = movimientos
            eval = minimax(tablero, profundidad -1, True, raton_posicion, nueva_gato_posicion)
            if eval < min_eval:
                min_eval = eval
                mejor_movimiento = movimientos
    return mejor_movimiento

#Funcion que ejecuta el juego

def  main():
    tablero = [['.'] * tablero_medida for _ in range(tablero_medida)]
    raton_posicion = (0, random.randint(1, tablero_medida -1))
    gato_posicion = (-1,random.randint(1, tablero_medida -1))
    tablero[raton_posicion[0]][raton_posicion[1]] = 'R'
    tablero[gato_posicion[0]][gato_posicion[1]] = 'G'
    
     
    while True:
        imprimir_tablero(tablero)
        
        #Movimiento del raton (Turno del raton)
        print('Turno del raton')
        movimiento_raton = mejor_movimiento(tablero, numero_raton, True, raton_posicion, gato_posicion)
        if movimiento_raton:
            tablero[raton_posicion [0]][raton_posicion[1]] = '.'
            raton_posicion = movimiento_raton
            tablero[raton_posicion [0]][raton_posicion[1]] = 'R'
        imprimir_tablero(tablero)
            
        if raton_posicion == gato_posicion:
            print('El gato atrapo al raton!!')
            break
        time.sleep(1)
        
        #Movimiento del gato (Turno del gato)
        print('Turno del gato')
        movimiento_gato = mejor_movimiento(tablero, numero_gato, False, raton_posicion, gato_posicion)
        if movimiento_gato:
            tablero[gato_posicion [0]][gato_posicion[1]] = '.'
            gato_posicion = movimiento_gato
            tablero[gato_posicion [0]][gato_posicion[1]] = 'G'
        imprimir_tablero(tablero)
        
        #Verificar si el raton ha sido atrapado
        if raton_posicion == gato_posicion:
            print('El gato atrapo al raton!!!')
            break
        time.sleep(1)
        
if __name__ == "__main__":
    main()