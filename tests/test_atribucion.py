import atribucion

def main():
    modelo = atribucion.Modelo("Test", False)
    resultado_markov = modelo.markov()
    return resultado_markov

if __name__ == "__main__":
    main()