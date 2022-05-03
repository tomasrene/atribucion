# MODELOS DE ATRIBUCION
Esta es una librería creada para el trabajo con modelos de atribución sobre datos de marketing digital.
Con esta librería se podrán crear modelos heurísticos (First click, Last click, Linear) o modelos data-driven (Markov, Shapley).
Funciona tanto con datos previamente formateados como con datos sin formatear.

## INSTALACIÓN
```
pip install atribucion
```
## CÓMO SE USA
Primero, es necesario crear un modelo pasando la data a utilizar. Se deberá indicar si la información fue previamente formateada o no.

La data formateada debe ser un dataframe con 2 columnas:
1. lista o array de recorridos (string)
2. conversión (boolean o int)

La data sin formatear debe ser un dataframe con 4 columnas:
1. tiempo (date o timestamp)
2. usuario (string)
3. canal (string)
4. conversion (boolean o int)

```
modelo = atribucion.Modelo(data, formateada=True)
```
Si la data no está formateada, se puede formatear para Markov o para Shapley. Los modelos heurísticos usan indistintamente cualquiera de las dos.
Para formatear la data, hay que indicar 3 parámetros:
1. ventana (int): cuántos días para atrás de la conversión se van a tener en cuenta para armar los recorridos.
2. touchpoints (int): la mayor cantidad de touchpoints que se admiten en cada recorrido.
3. conversión (bool): si se corta cada recorrido al encontrar una conversión o no.

```
modelo.formatear_markov(ventana=30, touchpoints=8, conversion=True)
modelo.formatear_shapley(ventana=30, touchpoints=8, conversion=True)
```
Luego, se piden los modelos deseados llamando a la función correspondiente.
La única que admite un parámetro es markov (el orden).

````
resultado_markov = modelo.markov(orden=1)
resultado_shapley = modelo.shapley()
resultado_first = modelo.first()
resultado_last = modelo.last()
resultado_linear = modelo.linear()
````
