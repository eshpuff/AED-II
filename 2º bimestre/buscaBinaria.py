lista = [2, 17, 40, 67, 143, 274, 505, 2000]

def buscaBinaria(lista, valor, ini=0, fim=None, tam=None):
    if fim is None:
        fim = len(lista) - 1
    if tam is None:
        tam = len(lista)
    
    print(lista, valor, ini, fim, tam)

    if fim < ini or tam == 0:
        return -1

    meio = tam // 2

    if lista[meio] == valor:
        return meio
    elif valor > lista[meio]:
        listaNova = lista[meio + 1:]  
        pos = buscaBinaria(listaNova, valor, ini, len(listaNova) - 1, len(listaNova))
        if pos == -1:
            return -1
        return meio + 1 + pos
    else:
        listaNova = lista[:meio] 
        pos = buscaBinaria(listaNova, valor, ini, len(listaNova) - 1, len(listaNova))
        return pos
    

print(buscaBinaria(lista, 40))