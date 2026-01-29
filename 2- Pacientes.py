#Pacientes

class Paciente:
    def __init__(self,n:str="",e:str="",s:str="",p:str=""):
        self.nombre = n
        self.edad = e
        self.sintomas = s
        self.prioridad = p

    def __str__(self):
        return f"{self.nombre =} {self.edad =} "
    
class Lista:
    def __init__(self):
        self.m = []

    def mostrar(self):
        for i,t in enumerate(self.m):
            print(t)

    def agregar(self):
        print("Hola, ahora puedes agregar un paciente\n")
        dat_n = input("Ingresa el Nombre: ")
        dat_e = input("Ingresa la edad: ")
        dat_s = input("Ingrese los sintomas: ")
        dat_p = input("Ingresa la prioridad 1-Alta 2-media 3-baja: ")
        novo = Paciente(dat_n,dat_e,dat_s,dat_p)
        self.m.append(novo)

    def submenu(self):
        opp = "p"
        while opp != "c":
            print("Seleccione la opcion de tipo de emergencia:\n")
            print("a-Mostrar pacientes de mayor urgencia")
            print("b-Mostrar pacientes de prioridad baja")
            print("c-Salir")
            opp = input("Ingresa la opcion: \n")

    def altaprio(self):
        print("\n--- Pacientes de ALTA Prioridad ---")
        encontrados = False
        for paciente in self.m:
            if paciente.prioridad == "1":
                print(paciente) 
                encontrados = True

            
            




a = Lista()
def main():
    opcion='0'
    while opcion !='4':
    
        print("---------Menu--------\n")
        print("1-Mostrar Todos los Pacientes")
        print("2-Agregar nuevo Paciente")
        print("3-Tipo de urgencia")
        print("4-Salir")
        opcion = input("\nSelecciona una opcion: ")

        if opcion == '1':
            a.mostrar()
        elif opcion == '2':
            a.agregar()
        elif opcion == '3':
            opp = "p"
            while opp != "c":
                print("Seleccione la opcion de tipo de emergencia:\n")
                print("a-Mostrar pacientes de mayor urgencia")
                print("b-Mostrar pacientes de prioridad baja")
                print("c-Salir")
                opp = input("Ingresa la opcion: \n")
                if opp == "a":
                    a.altaprio()
                elif opp == "b":
                    print("b")
                elif opp == "c":
                    break
        elif opcion == '5':
            break

main()