from clases.clase_celda import celda
import random
# clase tablero -> tablero de juego 
class tablero():
    # altura = numero de celdas de abajo a arriba
    # ancho = numero de celdas de izquierda a derecha 
    # celdas= comienzo de celdas en 0 
    altura = 0
    ancho = 0
    celdas = []
    # iniciar
    def __init__(self):
        self
    # funcion para crear tablero llenando de 0 cada casilla en la celda 
    def crearTablero(self):
        self.celdas = []
        for j in range(0,self.altura):
            arreglo2 = []
            for i in range(0,self.ancho):
                if i == 0:
                    celda1 = celda()
                    celda1.setEstado()
                    celda1.setValor(str(j))
                elif j == 0:
                    celda1 = celda()
                    celda1.setEstado()
                    celda1.setValor(str(i))
                else:
                    celda1 = celda()
                arreglo2.append(celda1)
            self.celdas.append(arreglo2)
    # funcion para generar minas aleatoreamente
    def generarMinas(self,nMinas):
        # nminas= numero de minas
        # cont = contadot que busca en que estado del juego uno se encuentra 
        cont = 0
        while (cont <= nMinas):
            filas = random.randrange(self.altura-1)+1
            columnas = random.randrange(self.ancho-1)+1
            # print('mejecuto')
            if self.celdas[filas][columnas].getValor() != "*":
                print(filas,columnas)
                self.celdas[filas][columnas].setValor('*')
                cont+=1

    # funcion que genra el tablero 
    def generar_tablero(self):
        retorno = ''
        for i in self.celdas:
            mostrar = ''
            for j in i:
                # print('mejecuto')
                val = j.getValor()
                mostrar = mostrar + val + '     '
            retorno = retorno + mostrar + '\n'
        # print(retorno)
        return retorno
    # funcion para destapar celdas s 
    def destapar_celda(self,coordX,coordY):
        self.celdas[coordX][coordY].setEstado()
        return self.celdas[coordX][coordY].getValor()
    # funcion para marcar las celddas segun las corrdenadas dadas por el jugador
    def marcar_celda(self,coordX,coordY):
        self.celdas[coordX][coordY].set_bandera()
        retorno = self.generar_tablero()
        return retorno

    # funcion para cambiar la dificultad 
    def setDificultad(self,dificultad):
        nivelDificultad = dificultad.get_nivelDificultad()
        if (nivelDificultad == 'Facil'):
            self.altura = 6
            self.ancho = 6
        elif (nivelDificultad == 'Normal'):
            self.altura = 8
            self.ancho = 8
        elif (nivelDificultad == 'Dificil'):
            self.altura = 10
            self.ancho = 10
