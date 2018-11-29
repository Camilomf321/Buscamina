
class celda():

    estado = False
    esMina = False
    bandera = False
    minasCerca = 0
    valor = ''

    def __init__(self,mina):
        self.esMina = mina
        if self.esMina:
            valor = '*'
        else:
            valor = '#'

    def setEstado(self):
        self.estado = True

        self.set_bandera()

    def set_bandera(self):
        if (self.bandera):
            self.bandera = False
        else:
            self.bandera = True

    def getValor(self):
        if self.estado:
            return self.valor
        else:
            return '?'