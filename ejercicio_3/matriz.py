
class Mapa:

    mapa = [['#',' ','#','#','#','#','#','#','#','#','#','#','#',' ','#','#','#','#','#','#','#','#','#','#','#'],
            ['#',' ','#','#','#','#','#','#','#','#','#','#','#',' ',' ','#','#','#','#','#','#','#','#','#','#'],
            ['#',' ','#','#','#','#','#','#','#','#','#','#',' ',' ',' ','#','#','#','#','#','#','#','#','#','#'],
            ['#',' ','#','#','#','#','#','#','#','#','#','#','#',' ','#','#','#','#','#','#','#','#','#','#','#'],
            ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#','#','#',' ','#','#','#','#',' ',' ',' ',' ',' ',' ','#'],
            ['#',' ','#','#','#','#','#','#',' ','#','#','#','#',' ','#','#','#','#',' ','#','#','#','#',' ','#'],
            ['#',' ','#','#','#','#','#','#',' ','#','#','#','#',' ','#','#','#','#','+','#','#','#','#',' ','#'],
            ['#',' ','#','#','#','#','#','#','+','#','#','#','#',' ','#','#','#','#',' ','#','#','#','#',' ','#'],
            [' ',' ','#','#','#','#','#','#',' ','#','#','#','#',' ','#','#','#','#',' ',' ',' ',' ',' ',' ',' '],
            ['#',' ','#','#','#','#','#','#',' ','#','#','#','#',' ','#','#','#','#',' ','#','#','#','#','#','#'],
            ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+',' ',' ',' ','#','#','#','#','#','#'],
            ['#','#','#','#',' ','#','#','#',' ','#','#','#','#',' ','#','#','#','#',' ','#','#','#','#','#','#'],
            ['#','#','#','#',' ','#','#','#',' ','#','#','#','#',' ','#','#','#','#',' ','#','#','#','#','#','#'],
            [' ',' ',' ',' ','+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            ['#','#','#','#','#','#','#','#',' ','#','#','#','#',' ','#','#','#','#',' ','#','#','#','#','#','#'],
            ['#','#','#','#','#','#','#','#',' ','#','#','#','#',' ','#','#','#','#',' ','#','#','#','#','#','#'],
            ['#','#','#','#','#','#','#','#','+','#','#','#','#',' ','#','#','#','#',' ','#','#','#','#','#','#'],
            ['#','#','#','#','#','#','#','#',' ','#','#','#','#',' ','#','#','#','#',' ','#','#','#','#','#','#'],
            ['#','#','#','#','#','#','#','#',' ','#','#','#','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            ['#','#','#','#','#','#','#','#',' ',' ',' ',' ',' ',' ','#','#','#','#','#','#','#','#','#',' ','#'],
            ['#','#','#','#','#','#','#','#',' ','#','#','#','#',' ','#','#','#','#','#','#','#','#','#',' ','#'],
            ['#','#','#','#','#','#','#','#',' ','#','#','#','#',' ',' ','+','+','#','#','#','#','#','#',' ','#'],
            ['#','#','#','#',' ',' ',' ',' ',' ','#','#','#','#','#','#','#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
            ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
            ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],]
            
    
    mapa_auto = []


    filas = len(mapa)
    columnas = len(mapa[0])

    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(' ')
        mapa_auto.append(fila)


