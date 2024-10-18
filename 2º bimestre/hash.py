class HashTable:
    def __init__(self, maxSize):
        self.key = [None] * maxSize
        self.value = [None] * maxSize
        self.size = 0
        self.maxSize = maxSize

    def hash_function(self, key):
        return hash(key) % self.maxSize

    def vazia(self):
        return self.size == 0

    def insert(self, key, value):
        if self.size >= self.maxSize:
            return False

        index = self.hash_function(key)
        original_index = index

        while self.key[index] is not None:
            if self.key[index] == key:
                self.value[index] = value
                return True
            index = (index + 1) % self.maxSize
            if index == original_index:
                return False

        self.key[index] = key
        self.value[index] = value
        self.size += 1
        return True

    def get(self, key):
        index = self.hash_function(key)
        original_index = index

        while self.key[index] is not None:
            if self.key[index] == key:
                print(self.value[index])
                return self.value[index]
            index = (index + 1) % self.maxSize
            if index == original_index:
                break
        return None

    def position(self, key):
        index = self.hash_function(key)
        original_index = index

        while self.key[index] is not None:
            if self.key[index] == key:
                print(index)
                return index
            index = (index + 1) % self.maxSize
            if index == original_index:
                break
        return None

    def remove(self, key):
        index = self.position(key)
        if index is None:
            return False 

        self.key[index] = None
        self.value[index] = None
        self.size -= 1

        next_index = (index + 1) % self.maxSize
        while self.key[next_index] is not None:
            rehash_key = self.key[next_index]
            rehash_value = self.value[next_index]
            self.key[next_index] = None
            self.value[next_index] = None
            self.size -= 1
            self.insert(rehash_key, rehash_value)
            next_index = (next_index + 1) % self.maxSize

        return True

    def destroy(self):
        self.key = [None] * self.maxSize
        self.value = [None] * self.maxSize
        self.size = 0

tabela = HashTable(3)
tabela.insert(164431, 'teste')
tabela.position(164431)
tabela.get(164431)