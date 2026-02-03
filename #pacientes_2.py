#pacientes_2

class Paciente:
    def __init__(self,n:str="",e:str="",s:str=""):
        self.nombre = n
        self.edad = e
        self.sintomas = s
    def __str__(self):
        return f"nombre: {self.nombre } edad: {self.edad }\n"


class Lista:
    def __init__(self):
        self.m = []

    def mostrar(self):
        for i,t in enumerate(self.m):
            print(t)

    def agregar(self):
        print("Ahora puedes agregar un paciente\n")
        dat_n = input("Ingresa el Nombre: ")
        dat_e = input("Ingresa la edad: ")
        dat_s = input("Ingrese los sintomas: ")
        novo = Paciente(dat_n,dat_e,dat_s)
        self.m.append(novo)

    def prest(self):
        for i,r in enumerate(self.m):
            print(i+1)

    def atend(self):
        for i,r in enumerate(self.m):
            rem=i
            self.m.pop(r)
            print(r)


a = Lista()
def main():
    opcion='0'
    while opcion !='5':
    
        print("---------Menu--------\n")
        print("1-Mostrar Todos los Pacientes")
        print("2-Agregar nuevo Paciente")
        print("3-Pacientes restantes")
        print("4-Atender Paciente")
        print("5-Salir")
        opcion = input("\nSelecciona una opcion: ")

        if opcion == '1':
            a.mostrar()
        elif opcion == '2':
            a.agregar()
        elif opcion == '3':
            a.prest()
        elif opcion == '4':
            a.atend()

main()
