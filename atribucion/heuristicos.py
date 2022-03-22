from collections import Counter

def calcular(data):
    """
    El input es un dataframe con los recorridos de cada usuario y si terminan en conversion.
    El output es un diccionario con la cantidad de conversiones atribuidas a cada canal por cada modelo.
    """
    atribucion = {}

    # chequear que no haya conversiones
    data = data[data.iloc[:,1]==1]

    # calcular cada uno de los modelos
    atribucion['first'] = calcular_first_click(data)
    atribucion['last'] = calcular_last_click(data)
    atribucion['linear'] = calcular_linear(data)

    return atribucion

def calcular_first_click(data):
    """ Calcula el modelo first click, atribuyendo la conversion al primer canal del recorrido."""
    
    # tomar solo el primer canal de cada conversion
    first_channel = [canal[0] for canal in data.iloc[:,0]]

    # contar conversiones de cada canal
    results = dict(Counter(first_channel))
    
    return results

def calcular_last_click(data):
    """ Calcula el modelo last click, atribuyendo la conversion al ultimo canal del recorrido."""

    # tomar solo el ultimo canal de cada conversion
    last_channel = [canal[-1] for canal in data.iloc[:,0]]

    # contar conversiones de cada canal
    results = dict(Counter(last_channel))

    return results

def calcular_linear(data):
    """Calcula el modelo linear, atribuyendo la conversion proporcionalmente a todos los canales del recorrido."""
    results = {}

    # para cada camino
    for camino in data.iloc[:,0]:
        for canal in camino:
            # calcular el proporcional de cada canal
            results[canal] = results.get(canal, 0) + 1/len(camino)
    
    # redondear
    results = {k:round(v,2) for k,v in results.items()}

    return results
    