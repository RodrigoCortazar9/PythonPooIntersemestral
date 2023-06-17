from cosas import *
def main():
    p1 = Persona("Jose",19)
    print(p1)

    print("------------herencia alumno----------")
    al1 = Alumno("Jose", 19, "231331313","ICO")
    print(al1)
    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "juan"
    print(al2)
    al2.dormir()
    print("\n------------herencia Profesor----------")

    pr1 = Profesor("Jesus",30+16,35432,"Ingene Soft")
    print(pr1)
    pr1.dormir()

    print("\n------------herencia Profesor----------")
    ayudante = AyudanteProfesor()


main()