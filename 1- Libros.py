#libro
class Libro:
    def __init__(self,titulo:str="ninguno",autor:str="ninguno",editorial:str="ninguno",precio:int=0):
        self.titulo=titulo
        self.autor=autor
        self.editorial=editorial
        self.precio=precio

    #def pedirDatos(self):
        #title = input("ingrese el titulo del libro: ")
        #self.titulo = (title)
        #self.autor = input("Ingrese el autor del libro: ")
        #self.editorial = input("Ingrese la editorial: ")
        #self.precio = int(input("Ingrese el precio: ")) 

    def actualizarPrecio(self):
        nuevoP = int(input("Ingrese el nuevo precio: "))
        self.precio = (nuevoP)
        print(f"El precio se a actualizado a {self.precio}")

    def info(self):
        print(f"\n{self.titulo=}")
        print(f"{self.autor=}")
        print(f"{self.editorial=}")
        print(f"{self.precio=}\n")


    #def libroCaro(self):

class Lista:
    def __init__(self):
        self.m = []
    
    def tomadeval(self):
        i = Libro()
        self.m.append(i)
        i.info()
        

    #def insertarfinal(self):
        #self.m.append("nada")

    def mostrar(self):
        print(self.m)

    def buscar(self):
        self.a=input("Ingresa el titulo a buscar: ")
        if self.a in self.m:
            print(f"El elemento que busca se encuentra en {Lista}")
        else:
            print("El elemento no se encuentra en la lista!!")
    def quitar(self):
        mimir = input("Ingresa el titulo a remover: ")
        self.m.remove(mimir)
        print(f"El libro {mimir} a sido borrado!!")

x = Libro("El principito","ant","nose",100)
x.info()
x.actualizarPrecio()
x.info()
print("--------------------------------------------------------------")

y = Libro("La peste","camus","sise",50)
y.info()
print("--------------------------------------------------------------")

z = Libro("El puente de los peluches","alem","talvez",30)
z.info()
print("--------------------------------------------------------------")

w = Lista()
w.tomadeval()
