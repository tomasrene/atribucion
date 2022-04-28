import atribucion

def main():
    data = [
        [['C1','C2','C3'],1],
        [['C1','C3'],1],
        [['C2','C3'],0]
    ]
    modelo = atribucion.Modelo(data, True)
    resultado_markov = modelo.markov()
    resultado_shapley = modelo.shapley()
    return resultado_markov, resultado_shapley

if __name__ == "__main__":
    main()