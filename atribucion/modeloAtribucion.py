from . import markov, shapley, heuristicos

class Modelo():
    def __init__(self, data, formateada=False):
        self.data = data
        self.formateada = formateada

        return None

    def markov(self, orden=1, ventana=30, touchpoints=8, conversion=True):

        if self.formateada == False:
            parametros = {
                'orden' : orden,
                'ventana' : ventana,
                'touchpoints' : touchpoints,
                'conversion' : conversion
            }
            data = markov.formatear(self.data, parametros)
        else:
            data = self.data

        resultado = markov.calcular(data)

        return resultado

    def shapley(self, ventana=30, touchpoints=8):

        if self.formateada == False:
            parametros = {
                'ventana' : ventana,
                'touchpoints' : touchpoints,
            }
            data = shapley.formatear(self.data, parametros)        
        else:
            data = self.data

        resultado = shapley.calcular(data)

        return resultado

    def heuristicos(self, ventana=30, touchpoints=8):

        if self.formateada == False:
            parametros = {
                'ventana' : ventana,
                'touchpoints' : touchpoints,
            }
            data = shapley.formatear(self.data, parametros)        
        else:
            data = self.data

        resultado = heuristicos.calcular(data)

        return resultado

    def comparacion(self):
        pass


