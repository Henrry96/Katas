# coding: utf8
template = " {0} │ {1} │ {2} \n───┼───┼───\n {3} │ {4} │ {5} \n───┼───┼───\n {6} │ {7} │ {8} "
turn = 0
Ganador = ""

def GetTablero():
    return template.format(1,2,3,4,5,6,7,8,9)
    """
        Esta funcion debe regresar el tablero en forma de cadena
        Nota: Usar el template de arriba
    """
    
    raise NotImplementedError

def JuegoContinua():
    """
        Debe de regresar verdadero si el juego continua o false si ha terminado
    """
    global Ganador
    global template
    
    info = template.replace(" ","").replace("{","").replace("}","").replace("│","").replace("┼","").replace("─","").replace("\n","")
    infoGana = info.replace("X","").replace("O","")

    if  infoGana == "":
        Ganador = "Empate"
        return False
    elif (info[0]+info[1]+info[2]) == "XXX" or (info[3]+info[4]+info[5]) == "XXX" or (info[6]+info[7]+info[8]) == "XXX" or (info[0]+info[3]+info[6]) == "XXX" or (info[1]+info[4]+info[7]) == "XXX" or (info[2]+info[5]+info[8]) == "XXX" or (info[0]+info[4]+info[8]) == "XXX" or (info[2]+info[4]+info[6]) == "XXX":
        Ganador = "X"
        return False
    elif (info[0]+info[1]+info[2]) == "OOO" or (info[3]+info[4]+info[5]) == "OOO" or (info[6]+info[7]+info[8]) == "OOO" or (info[0]+info[3]+info[6]) == "OOO" or (info[1]+info[4]+info[7]) == "OOO" or (info[2]+info[5]+info[8]) == "OOO" or (info[0]+info[4]+info[8]) == "OOO" or (info[2]+info[4]+info[6]) == "OOO":
        Ganador = "O"
        return False
    else:
        return True
    raise NotImplementedError

def IntentarTirada(casilla):
    """
        Esta funcion recibe el intento del jugador por ocupar una casilla
        y regresa una cadena segun los siguientes criterios:
        Si esta fuera de rango: "La tirada debe de estar entre 1 y 9"
        Si la casilla esta ocupada: "La casilla ya esta ocupada"
        Si x a ganado: "Felicidades X as ganado. weeee"
        Si o a ganado: "Felicidades O as ganado. weeee"
        Si el juego a quedado empatado: "Juego empatado. :("
        Ninguna de las anteriores: "" (cadena vacia)
    """
    global turno
    global Ganador
    global template
    global error
    
    casilla = int(casilla)
    if (casilla) > 9 or (casilla) < 1:
        return "La tirada debe de estar entre 1 y 9"
    elif template.find(str(casilla)) == -1:
        return "La casilla ya esta ocupada"
    else:
        if turno % 2 == 0:
            template = template.replace(str(casilla),"X")
            turno += 1
            JuegoContinua()
            if Ganador == "X":
                return "Felicidades X as ganado. weeee"
        elif turno % 2 == 1:
            template = template.replace(str(casilla),"O")
            turno += 1
            JuegoContinua()
            if Ganador == "O":
                return "Felicidades O as ganado. weeee"
        if turno == 9:       
            return "Juego empatado. :("
        return ""
    
    
    raise NotImplementedError

def IniciaJuego():
    """
        Esta function se puede utilizar para re iniciar variables.
        Si no se usa se puede dejar vacia
    """
    global template
    global turno
    global Ganador
    template = " 1 │ 2 │ 3 \n───┼───┼───\n 4 │ 5 │ 6 \n───┼───┼───\n 7 │ 8 │ 9 "
    turno = 0
    Ganador = ""
    return None

if __name__ == '__main__':
    IniciaJuego() 
    while(JuegoContinua()):
        print(GetTablero())
        msg = ""
        casilla = int(input("Escoge una casilla: "))
        msg = IntentarTirada(casilla)
        if msg != "":
            print(msg)
