#clase que representa un nodo en el arbol binario
class Node:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

#Clase que representa el arbol binario
class BinaryTree:
    def __init__(self):
        self.root=None

#funcion para insertar los datos en el arbol
    def insert(self, value):  
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert_recursiva(self.root, value)

    def _insert_recursiva(self, nodo_actual, value):
        #insertar nodo al lado izquierdo
        if value < nodo_actual.value:
            if nodo_actual.left is None:
                nodo_actual.left = Node(value)
            else:
                self._insert_recursiva(nodo_actual.left, value)
        #insertar nodo al lado derecho
        elif value> nodo_actual.value:
            if nodo_actual.right is None:
                nodo_actual.right=Node(value)
            else:
                self._insert_recursiva(nodo_actual.right, value)