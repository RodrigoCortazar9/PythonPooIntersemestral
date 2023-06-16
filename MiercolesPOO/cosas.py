class Alumno:
    facultad = "FES Aragón"

    def __init__(self, nom, ed, carr):
        self.__nombre = nom
        self.__edad = ed
        self.__carrera = carr

    def set_nombre(self,nom):
        self.__nombre = nom #Variable privada local

    def get_nombre(self):
        return self.__nombre

    def set_edad(self,edad):
        if edad >=8 and edad<=120:
            self.__edad = edad
        else:
            print("Edad incorrecta")
            self.__edad=0

    def get_edad(self):
        return self.__edad

    def set_carrera(self,carrera):
        self.__carrera = carrera

    def get_carrera(self):
        return self.__carrera

    def estudiar(self,horas=1):
        print(f"El alumno {self.__nombre} esta estudiando {horas} horas")

    def __str__(self):
        cadena  = f"Nombre: {self.__nombre}, Edad; {self.__edad}, Carrera: {self.__carrera}"
        return cadena