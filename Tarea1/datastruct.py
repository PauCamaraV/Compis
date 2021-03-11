# datastuct.py by Paulina Cámara (2021)
# Creacion de estructura de datos: nodo, stack, queue y hash 

#Clase Nodo
class Nodo:
    def __init__(self, valor = None):
        self.valor = valor
        self.next = None

#Clase Stack
class Stack:
    def __init__(self):
        self.head = Nodo()
    
#Añadir valor al stack
    def push(self, val):
        nodo = Nodo(val)
        aux = self.head
        self.head = nodo
        self.head.next = aux

#Eliminar valor del stack
    def pop(self):
        if self.head.valor is None:
            return None
        else:
            val = self.head.valor
            self.head = self.head.next
            return val

#Obtener primer valor del stack
    def top(self):
        return self.head.valor

#Clase Queue
class Queue:
    def __init__(self):
        self.head = Nodo()
        self.tail = None
    
#Añadir valor a la queue
    def push(self, val):
        if self.head.valor is None:
            self.head.valor = val
            self.tail = self.head

        else:
            self.tail.next = Nodo(val)
            self.tail = self.tail.next

#Eliminar valor de la queue
    def pop(self):
        if self.head.valor is None:
            return None
        else:
            val = self.head.valor
            self.head.valor = None
            self.head = self.head.next
            return val

#Obtener primer valor de la queue
    def front(self):
        if self.head.valor is None:
            return None
        else:
            return self.head.valor

#Clase Hash
class Hash:
    def __init__(self):
        self.cap = 601
        self.tabla = [None for n in range(601)]

#Funcion Hash
    def hashfunc(self, clave):
        sum = 0
        for char in clave:
            sum += ord(char) 
        return sum % self.cap
    
#Añadir elemento al Hash
    def add(self, clave, valor):
        self.tabla[self.hashfunc(clave)] = valor

#Eliminar elemento del Hash
    def delete(self, clave):
        self.tabla[self.hashfunc(clave)] = None

#Obtener valor guardado en Hash
    def getVal(self, clave):
        return self.tabla[self.hashfunc(clave)]
