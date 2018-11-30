#Se importa libreria de sistema para ejecutar el programa
import sys
#se importan las librerias QtWidgets y uic para que la clase ventana herede de QtWidgets
from PyQt5 import QtWidgets, uic
#Importas la clase tablero para luego crear la matriz dentro de la ventana
from clases.clase_tablero import tablero
from clases.clase_dificultad import dificultad

#se crea la clase ventana que hereda de QDialog de la libreria QtWidgets
class Ventana(QtWidgets.QDialog):

    tablero = ''
    nivelDificultad = dificultad()

#Se inicializa la clase,carga la interfaz uic y asigna funciones a los botones
    def __init__(self):
        super(Ventana, self).__init__()
        uic.loadUi('buscaminas.ui', self)
        self.Inicio.clicked.connect(self.iniciar)
        self.reiniciar.clicked.connect(self.reinicio)
        self.Destapar.clicked.connect(self.destapar)
        self.Marcar.clicked.connect(self.marcar)
        self.show()
    # iniciar buscaminas
    def iniciar(self):
        self.dificultadSeleccionada = self.Dificultad.currentText()
        self.nivelDificultad.setDificultad(self.dificultadSeleccionada)
        self.n_minas.setText(str(self.nivelDificultad.get_nMinas()))
        self.tablero = tablero()
        self.tablero.setDificultad(self.nivelDificultad)
        self.tablero.crearTablero()
        self.tablero.generarMinas(self.nivelDificultad.get_nMinas())
        nuevoTexto = str()
        nuevoTexto = self.tablero.generar_tablero()
        self.tabla.setText('')
        self.tabla.setText(str(nuevoTexto))
        # while True:
        #     for s in range(0,60):
        #         self.
    # reinicio juego 
    def reinicio(self):
        self.dificultadSeleccionada = self.Dificultad.currentText()
        self.nivelDificultad.setDificultad(self.dificultadSeleccionada)
        self.n_minas.setText(str(self.nivelDificultad.get_nMinas()))
        self.tablero = tablero()
        self.tablero.setDificultad(self.nivelDificultad)
        self.tablero.crearTablero()
        self.tablero.generarMinas(self.nivelDificultad.get_nMinas())
        nuevoTexto = str()
        nuevoTexto = self.tablero.generar_tablero()
        self.tabla.setText('')
        self.tabla.setText(str(nuevoTexto))
    # funcion para destapar la celda
    def destapar(self):
        coordX = int(self.coorX.text())
        coordY = int(self.coorY.text())
        destapado = self.tablero.destapar_celda(coordX,coordY)
        if destapado == '*':
            self.tablero = tablero()
            self.tabla.setText('')
            self.tabla.setText('Perdió Intentelo De Nuevo')
        else:
            nuevoTexto = self.tablero.generar_tablero()
            self.tabla.setText('')
            self.tabla.setText(str(nuevoTexto))
    # funcion para marcar bandera a la celda 
    def marcar(self):
        coordX = int(self.coorX.text())
        coordY = int(self.coorY.text())
        self.tablero.marcar_celda(coordX, coordY)
        nuevoTexto = self.tablero.generar_tablero()
        self.tabla.setText('')
        self.tabla.setText(str(nuevoTexto))



# En este if se llama la clase principal de ventana y se ejecuta el programa
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ventana()
    sys.exit(app.exec_())

