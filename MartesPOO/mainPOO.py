from cosas import Alumno , Profesor



def main():
    al1 = Alumno() #Creacion de un objeto
    print(al1)
    #Para imprimir las varibales de un objeto
    print(vars(al1))
    #Agregar un atributo. intancia al objeto
    al1.rango = "Master"
    print(vars(al1))


    p1 = Profesor("Calr",30,"ICO")
    print(vars(p1))




main()
