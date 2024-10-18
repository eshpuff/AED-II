class Nodo:
    def __init__(self,info):
        self.info = info
        self.left = None
        self.right = None

class binaryTree:
    def __init__(self):
        self.root = None

    def search(self, value, nodo=None):
        if nodo is None:
            nodo = self.root
        if nodo is None or nodo.info == value:
            return nodo
        elif value < nodo.info:
            return self.search(value, nodo.left)
        else:
            return self.search(value, nodo.right)

    def insert(self, value):
        new_nodo = Nodo(value)
        if self.root is None:
            self.root = new_nodo
        else:
            self._insert_aux(self.root, new_nodo)

    def _insert_aux(self, current_nodo, new_nodo):
        if new_nodo.info < current_nodo.info:
            if current_nodo.left is None:
                current_nodo.left = new_nodo
            else:
                self._insert_aux(current_nodo.left, new_nodo)
        else:
            if current_nodo.right is None:
                current_nodo.right = new_nodo
            else:
                self._insert_aux(current_nodo.right, new_nodo)

    def remove(self, value):
        self.root = self._remove_aux(self.root, value)

    def _remove_aux(self, nodo, value):
        if nodo is None:
            return nodo
        if value < nodo.info:
            nodo.left = self._remove_aux(nodo.left, value)
        elif value > nodo.info:
            nodo.right = self._remove_aux(nodo.right, value)
        else:
            if nodo.left is None:
                return nodo.right
            elif nodo.right is None:
                return nodo.left
            temp = self._min_nodo(nodo.right)
            nodo.info = temp.info
            nodo.right = self._remove_aux(nodo.right, temp.info)
        return nodo

    def _min_nodo(self, nodo):
        current = nodo
        while current.left is not None:
            current = current.left
        return current

    def imprime(self, tipo='central'):
        if tipo == 'central':
            self._imprime_central(self.root)
        elif tipo == 'pre':
            self._imprime_pre_fixado(self.root)
        elif tipo == 'pos':
            self._imprime_pos_fixado(self.root)


    def _imprime_central(self, nodo):
        if nodo is not None:
            self._imprime_central(nodo.left)
            print(nodo.info, end=" ")
            self._imprime_central(nodo.right)

    def _imprime_pre_fixado(self, nodo):
        if nodo is not None:
            print(nodo.info, end=" ")
            self._imprime_pre_fixado(nodo.left)
            self._imprime_pre_fixado(nodo.right)

    def _imprime_pos_fixado(self, nodo):
        if nodo is not None:
            self._imprime_pos_fixado(nodo.left)
            self._imprime_pos_fixado(nodo.right)
            print(nodo.info, end=" ")

arvore = binaryTree()
arvore.insert(50)
arvore.insert(30)
arvore.insert(20)
arvore.insert(40)
arvore.insert(70)
arvore.insert(60)
arvore.insert(80)

print("central:")
arvore.imprime(tipo='central')

print("\npre-fixado:")
arvore.imprime(tipo='pre')

print("\npós-fixado:")
arvore.imprime(tipo='pos')

print("\nremove 20:")
arvore.remove(20)
arvore.imprime(tipo='central')

# arvore.remove(30)
# arvore.imprime(tipo='central')

# arvore.remove(50)
# arvore.imprime(tipo='central')