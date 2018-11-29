class dificultad():

    numeroMinas = 0
    nivelDificultad = ''

    def __init__(self):
        self

    def get_nMinas(self):
        return self.numeroMinas

    def get_nivelDificultad(self):
        return self.nivelDificultad

    def setDificultad(self,dificultad):
        self.nivelDificultad = dificultad;
        if (self.nivelDificultad == 'Facil'):
            self.numeroMinas = 5
        elif (self.nivelDificultad == 'Normal'):
            self.numeroMinas = 14
        elif (self.nivelDificultad == 'Dificil'):
            self.numeroMinas = 20