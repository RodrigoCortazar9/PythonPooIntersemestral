class Autor:
    def __init__(self,nom,pseudo):
        self.__nombre = nom
        self.__pseudonimo = pseudo

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nom):
        self.__nombre = nom
    @property
    def pseudonimo(self):
        return self.__pseudonimo
    @pseudonimo.setter
    def pseudonimo(self,pse):
        self.__pseudonimo = pse

    def escribir(self):
        print(f"{self.__nombre} esta escribiendo su siguiente libro")


class Libro:
    def __init__(self,titulo,an,edit,autor):
        self.__titulo = titulo
        self.__año = an
        self.__editorial = edit
        self.__autor = autor

    @classmethod
    def libro_planeta(cls,titulo,autor,año):
        return cls(titulo,autor,"LP",año)

    def leer(self,m):
        print(f"Leyendo por {m} minutos")


class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

class Alumno(Persona):
    def __init__(self,nombre,edad,numero_cuenta,carrera,promedio):
        super().__init__(nombre,edad)
        self.__numero_cuenta = numero_cuenta
        self.__carrera = carrera
        self.__promedio = promedio

