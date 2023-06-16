from cosas import Alumno
from Perro import Perro
def main():
    al1 = Alumno("Jijija",19,"ICO")
    al1.set_edad(999)
    print(vars(al1))
    print(al1)
    al1.estudiar()
def mainPerro():
    p1 = Perro("Pit",1,8.2)
    print(p1)
    print(vars(p1))
    p1.estatura = 2
    p1.edad = 3
    p1.raza = "Juo"
    print(p1)
    p2 = Perro("Bull",5,10.5)
    print(p2)
    print(Perro.es_cachorro(p1.edad))
    Perro.dormir(50)
    danes = Perro.perro_grande(0.8)
    print(danes)
mainPerro()