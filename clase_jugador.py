#Se define la clase Jugador ()
class Jugador():

#Se definen los atributos de la clase jugador
    nombre = ""
    puntuacion = 0
    dificultad = ""

#Se define la función con la que se crea el objeto que recibe el nombre y la dificultad con la que va a jugar el usuario
    def __init__(self,nombre, dificultad):

        # Se asigna el nombre recibido por la función al atributo nombre del objeto,igual el de dificultad
        self.nombre = nombre
        self.dificultad = dificultad

#Se define la función que retorna el usuario
    def get_usuario(self):
        datos=[]
        datos.append(self.nombre)
        datos.append(self.dificultad)
        datos.append(self.puntuacion)
        return datos


#Se define la función  que guarda la puntuación del usuario
    def Guardar_puntuacion(self, nueva):
        self.puntuacion = nueva

#Se define la función que muestra la ultima puntuación del usuario
    def Mostrar_puntuacion(self):
        print("su puntuacion es " + str(self.puntuacion))
