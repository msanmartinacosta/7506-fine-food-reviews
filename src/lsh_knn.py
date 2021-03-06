import knn

from src import lsh

n_vec = [461, 599, 733, 827, 103, 997]
k = 10
b = 5


# Funcion que realiza el proceso para todos los datos
# @params:
#   data: todos los puntos de prueba
#   test: todos los puntos de test
#   n_vec: vector con los valores pra las funciones de hashing universal
#   k: k optimo
#   distance: distancia optima
#   b: cantidad de tablas
# @returns:
#   [{'Id','Prediction'}]
# def do_lsh_knn(data, test):
#    tables = load_test_file(test)
#    data['Prediction'] = data.apply(lambda row: lsh_knn(row['Text'], tables), axis=1)
#    return data


# Funcion que realiza el proceso para un dato
# @params:
#   d: punto de prueba
#   tables: tablas precargadas con el archivo de test
#   n_vec: lista de valores para las funciones de hashing universal
#   k: valor optimo de k
#   distance: la distancia optima
# @returns:
#   diccionario con {'Id','Prediction'}
def do_lsh_knn(d, tables):
    hash_values = lsh.get_hash_of_minhashes(d, n_vec)
    candidates = lsh.get_candidates_from_tables(hash_values, tables)
    k_nearest_neighbours = knn.knn(d, candidates, k, knn.jaccard_distance)
    prediction = knn.calculate_prediction(k_nearest_neighbours)
    return prediction


# Funcion que carga las tablas con los datos de entrenamiento
# @params:
#   test: datos de entrenamiento
#   b: numero de tablas
# @returns:
#   lista de tablas con hashes y candidatos
def load_test_file(test):
    tables = create_tables()
    test.apply(lambda row: lsh.add_data_to_tables(tables, row, n_vec), axis=1)
    return tables


# Crea las tablas
# Cada tabla es un diccionario [clave, valor]
# Se guardan las b tablas en un arreglo de b dimensiones
# @params
#   b: numero de tablas
# @returns:
#   tablas
def create_tables():
    tables = []
    for i in range(0, b):
        tables.append({})
    return tables
