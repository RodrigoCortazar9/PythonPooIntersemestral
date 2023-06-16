from cosas import *
def main():
    l1 = Libro.libro_planeta("El perfume",Autor("Patrik","PS"),999)
    print(vars(l1))

def main2():
    al1 = Alumno("Juan",22,323,"ICO",22)
    print(vars(al1))

main2()