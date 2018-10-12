__autor__ = 'Victor Hugo Vergara Jr'

class memDinamica:
    __lista = []

    def __init__(self, lista):
        self.__lista = lista

    def getAutos(self):
        return self.__lista

    def recorrerArreglo(self):
        for x in self.getAutos():
            print (self.getAutos().index(x)+1, x)

    def agregarelementoarray(self, elemento): #Metodo que permite agregar mas elementos a las listas al final de estas
        self.__listas.append(elemento)

    def ordenarListas(self):
        self.__listas.sort()

    def eliminarNElementos(self, num):
        self.__listas.pop(num)

    def eliminarElemento(self, elemento):
        self.__listas.remove(elemento)

    def insertarNPosicion(self, num, elemento):
        self.__listas.insert(num, elemento)

    def imprimirListas(self): #Este metodo puede imprimir si es llamado
        print (self.__listas)

    def eliminarElemento(self):
        self.__listas.pop