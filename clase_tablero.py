from clases.clase_celda import celda
class tablero():

    altura = 10
    ancho = 10
    n_minas = 0
    celdas = []

    def __init__(self):
        self

    def generar_tablero(self):

        for j in range(0,self.altura):
            arreglo_2 =  []
            for i in range(0,self.ancho):
                celda1=celda()
                arreglo_2.append(celda1)
            self.celdas.append(arreglo_2)

        for l  in self.celdas:
            for k  in l:
                print(k,"   ",end="")
            print("")

