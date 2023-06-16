
class Perro:

    nPerro = 1
    def __init__(self,raza,edad,estatura):
        self.__raza = raza
        self.__edad = edad
        self.__estatura = estatura
        self.__id = Perro.nPerro
        Perro.nPerro = Perro.nPerro+1

    #Metodo de acceso get
    @property
    def raza(self):
        return self.__raza
    #Metodo de acceso set
    @raza.setter
    def raza(self,raza):
        self.__raza = raza

    @property
    def edad(self):
        return self.__edad
    @edad.setter

    def edad(self,edad):
        if edad>=1 and edad<20:
            self.__edad = edad
        else:
            self.__edad = 0

    @property
    def estatura(self):
        return self.__estatura
    @estatura.setter
    def estatura(self,e):
        self.__estatura = e

    def __str__(self):
        return f"""--------------------
Id: {self.__id}
Raza:{self.__raza} 
Edad: {self.__edad}
Estatura: {self.__estatura}
--------------------
        """
    #Los metodos staticos no nesesitan de una instancia para ser llamados
    @staticmethod
    def es_cachorro(edad):
        return edad < 3
    @staticmethod
    def dormir(veces=5):
        for n in range(veces):
            print(f"Dando vuelta {n+1}")

    #Pueden acceder a las variables de clase
    @classmethod
    def perro_grande(cls,est):
        if est > 0.79:
            # cls = Perro
            return cls("",0,est)#Forma diferente de llamar al constructor
            #return Perro("",0,est)

    @classmethod
    def constructor_dos(cls,raz,ed):
        if ed > 0 and ed >20:
            return cls(raz,ed,0.0)
        else:
            return cls(raz, 0, 0.0)