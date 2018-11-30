#clase dificultad -> esta clase muestra las dificultades que se pueden escoger en el juego
class dificultad():
    #numeroMinas = numero de minas segun la dificultad del juego
    #nivelDificultad = se despliega en el juego una serie de opciones de dificultad de juego
    numeroMinas = 0
    nivelDificultad = ''

    # iniciar dificultaf
    def __init__(self):
        self
    # ver minas 
    def get_nMinas(self):
        return self.numeroMinas
    # ver dificultad
    def get_nivelDificultad(self):
        return self.nivelDificultad
    # cambiar dificultad 
    def setDificultad(self,dificultad):
        self.nivelDificultad = dificultad;
        if (self.nivelDificultad == 'Facil'):
            self.numeroMinas = 5
        elif (self.nivelDificultad == 'Normal'):
            self.numeroMinas = 14
        elif (self.nivelDificultad == 'Dificil'):
            self.numeroMinas = 20
