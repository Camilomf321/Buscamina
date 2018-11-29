# clase celda-> esta clase contiene los atributos de cada celda 
class celda():
    #estado = estado de la celda (abierta )
    #esMina = verifica si el estado de la celda es una mina
    #bandera = verifica si la celda es una bandera 
    #minasCerca =  numero de minas que van a estar cerca 

    estado = False
    esMina = False
    bandera = False
    minasCerca = 0
    valor = '#'

    def __init__(self,):
        self

    def setEstado(self):
        self.estado = True

    def set_bandera(self):
        if (self.bandera):
            self.bandera = False
        else:
            self.bandera = True

    def setValor(self,val):
        self.valor = val

    def getValor(self):
        if self.estado:
            return self.valor
        else:
            if self.bandera:
                return '^'
            else:
                return '?'
