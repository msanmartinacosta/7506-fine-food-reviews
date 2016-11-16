# URL para buscar numeros primos: http://primes.utm.edu/lists/small/millions/
from random import randint

# numero de funciones de hash por grupo
r = 2

# numero de tablas
b = 2

# numero total de funciones de hashing
N = r * b

# Numero primo (ver de buscar uno mas grande)
p = 32416187567


# Funcion de Carter-Weigman para numeros
# @params:
#   x: dato a hashear
#   n: valor para particularizar la funcion
# @returns:
#   el hash
def h_cw_int(x, n):
    a = 1
    c = 1
    return (a * x + c % p) % n


# Funcion de Carter-Weigman para strings
# @params:
#   x: dato a hashear
#   n: valor para particularizar la funcion
# @returns:
#   el hash
def h_cw_str(x, n):
    h = 0
    a = randint(1, p - 1)
    for c in x:
        h = (h * a + c) % p

    # c = randint(1, p-1)
    # for i in (0,len(x)-1):
    #     h += c*(a**i)
    # return h_cw_int(h % p, n)
    return h


# Funcion de Carter Weigman para vectores
# @params:
#   x: dato a hashear
#   n: valor para particularizar la funcion
# @returns:
#   el hash
def h_cw_vec(x, n):
    accum = 0
    a = [randint(1, p - 1) for _ in range(0, len(x) - 1)]

    for i in (0, len(x) - 1):
        accum += a(i) * x(i)
    h = (accum % p) % n
    return h


# Funcion que obtiene el vector de minhashes de un dato
# @params:
#   d: dato a hashear, el texto
#   n_vec: Contiene los valores de N para las funciones de hashing universal
# @returns:
#   el vector de minhashes del dato
def get_minhashes(d, n_vec):
    mh = []
    for i in (0, len(n_vec) - 1):
        mh.append(h_cw_str(d, n_vec(i)))
    return mh


# Funcion que calcula los hashes (posicion) en cada tabla de las r tablas
# para los grupos de r funciones de hash
# @params:
#   d: dato a hashear
#   n_vec: Contiene los valores de N para las funciones de hashing universal
# @returns:
#   Vector con los hash de cada grupo de minhashes
def get_hash_of_minhashes(d, n_vec):
    minhashes = get_minhashes(d, n_vec)
    group_of_minhashes = get_group_of_minhashes(minhashes, r)
    hashes = []
    n = 1  # TODO cambiar
    for group in group_of_minhashes:
        hashes.append(h_cw_vec(group, n))
    return hashes


# Divide los minhashes en grupos de r funciones
# Cortesia de: http://stackoverflow.com/questions/4119070/how-to-divide-a-list-into-n-equal-parts-python
# @params:
#   lst: lista con los minhashes
#   sz: tamaño maximo de cada grupo
# @returns:
#   vector de vector de minhashes
def get_group_of_minhashes(lst, sz):
    return [lst[i:i + sz] for i in range(0, len(lst), sz)]