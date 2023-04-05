def find_one(list, needle):
    """
    Devuelve True si encuentra una o más ocurrencias de needle en list
    """
    return find_n(list, needle, 1)


def find_n(list, needle, times): 
    """
    Devuelve True si en list hay times o mas ocurrencias de needle
    False si hay menos o si n < 0
    """
    # Si times < 0 devolvemos False
    if times < 0:
        return False
    
    # Inicializamos el indice y el contador
    acum = 0
    index = 0
    
    # Mientras no hayamos encontrado al elemento n veces o no hayamos terminado la lista
    while acum < times and index < len(list):
        # SI lo encontramos, actualizamos el contador
        if list[index] == needle:
            acum += 1
        # Avanzamos al siguiente elemento
        index += 1
    # Devolvemos el resultado igualado a times
    return acum == times

def find_streak(list, needle, times): 
    """
    Devuelve True si en list hay times o mas ocurrencias de needle seguidas
    False si hay menos o si n < 0
    """
    
    # Si times < 0 devolvemos False
    if times < 0:
        return False
    # Inicializamos el indice y el contador
    acum = 0
    index = 0
    # Mientras no hayamos encontrado al elemento n veces seguidas o no hayamos terminado la lista
    while acum < times and index < len(list):
        # SI lo encontramos, aumentamos en uno el acumulador de coincidencias
        if list[index] == needle:
            acum += 1
        # Si no encontramos el elemento ponemos el acumulador de coincidencias a 0, y rompemos la racha siempre que acum sea < que times
        else:
            acum = 0
        # Avanzamos al siguiente elemento
        index += 1
    # Devolvemos el resultado igualado a times
    return acum == times

#    assert find_n([1, 2, 3, 4, 5], 42, 2) == False

def first_elements(matriz):
    """
    Devuelve en una lista los primeros elementos de una matriz (la primera columna)
    """
    return any_element(matriz, 0)

def any_element(matriz, n):
    """
    Devuelve en una lista los elementos de la columna n
    """
    # Coge el elemento n de cada fila de la matriz y lo mete en una lista
    elements = list(map(lambda element: element[n], matriz))
    return elements

def transpose(matriz):
    """
    Devuelve una matriz transpuesta
    """
    # Matriz vacia
    transpose_matriz = []
    # Para cada fila que tenga matriz 
    for n in range(len(matriz[0])):
        # Añade a la fila de matriz transpuesta los primeros elementos de la columna n de matriz
        transpose_matriz.append(any_element(matriz, n))
    return transpose_matriz

def positive_displace(l, distance, filler):
    """
    Devuelve la lista l con sus elementos desplazados distance posiciones y rellenando los huecos con filler
    """
    n = 0
    # Mientras que n sea menor a la distancia
    while n < distance:
        # Sacamos el ultimo item e intruducimos el filtro en el primero
        l.pop()
        l.insert(0, filler)
        # Incrementamos el contador
        n += 1
    # Devolvemos la lista transformada
    return l
    
    
def displace(l, distance, filler=None):
    """
    Devuelve una lista con los elementos desplazados por distancia y reelenando con filler
    """
    # Si la distancia es 0 o la lista esta vacia devuelve la lista
    if distance == 0 or len(l) == 0:
        return l
    # Si la distancia es positiva
    elif distance > 0:
    # Movemos los items distance posiciones a la derecha y rellenamos con filler
        return positive_displace(l, distance, filler)
    else:
        # Si el desplazamiento es negativo damos la vuelta a la lista
        l.reverse()
        # Aplicamos un despazamiento positivo
        l = positive_displace(l, abs(distance), filler)
        # Le volvemos a dar la vuelta
        l.reverse()
        # La devolvemos
        return l
        
def displace_matrix(m, filler=None):
    # creamos una matriz vacia
    matrix = []
    # por cada columna de la matriz original la desplazamos su indice -1
    # añadimos la columna desplazada a m
    for i in range(len(m)):
        matrix.append(displace(m[i], i-1, filler))
    # devolvemos m
    return matrix







