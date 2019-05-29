# Tinder para empresas

Script para el area de Outcomes de Ironhack. Permite crear rondas de emparejamiento entre empresas y estudiantes dando prioridad a las de mayor afinididad (matching) entre alumno y empresa y procurando que todos los alumnos tengan un número similar de entrevistas. 
Este script utiliza python 3 y varias librerías. 


## Encuestas Fuente

### WEB
Encuestas Students: 
https://docs.google.com/forms/d/1w85z6lqZdQfByTMiefqUcth16-F9NnLHuZuh9CVHxyU/edit#responses
Encuestas Company: 
https://docs.google.com/forms/d/1JOjjmV1W-ay7h00wVtpcQzD6FHNJU8Qg6RRz1ptDN4Q/edit

### UXUI
Encuestas Students: 
https://docs.google.com/forms/d/1N1BbrRrs_qN-qrHhfhtbvj3eh8JupsxxCD97GZHNoBc/edit
Encuestas Company: 
https://docs.google.com/forms/d/1JpKsGgOfVaLiKg0uXTLb-Xp8TjG6k4KRz07pFd_GHuE/edit

### Data 
Encuestas Students: 

Encuestas Company: 



## TO DO
Si no saben front vs back o ux vs ui, poner un 5, y no hacer overcualificated
el uxui se elegen 3 competencias y no te calificas en cada una. 

revisar el formulario para empresas, aparecen cosas como: 
- On a scale from 1 to 10, how much time will the employee be spending working on back end and front end?
- Además creo que es mejor hacer obligatorias TODAS las respuestas permitienedo en 'No es necesario' y el 'Nada'. 
- Mark the top 3 competencies you are looking for in an employee for this position -> El código a usar será 
```## test 
import pandas

df = pandas.Series([('Adventure', 'Drama', 'Fantasy'), ('Comedy', 'Family'), ('Drama', 'Comedy', 'Romance'), (['Drama']), 
                    (['Documentary']), ('Adventure', 'Biography', 'Drama', 'Thriller')]).apply(frozenset).to_frame(name='genre')
for genre in frozenset.union(*df.genre):
    df[genre] = df.apply(lambda _: int(genre in _.genre), axis=1)
    
df.head()
```

## Instrucciones
1. Copiar ambos formularios desde la fuente original: 
< Insertar foto >
	1. students form (URL_1)
	2. companies form (URL_2)
2. Enviar a los estudiantes y a las empresas que participan en la hiring fair su encuesta correspondiente. Mas detallado
3. Una vez que los formularios estén terminados generar la hoja de cálculo que proporciona google. 
< Insertar foto >
4. descargar ambos excel en formato CSV 
5. copiar ambos csv en la carpeta input del proyecto
< Insertar foto >

6. Instalar dependencias: 
``` 
$ virtualenv venv 
$ . venv/bin/activate
$ pip install -r requirements.txt
$ make
$ python app.py
```
7. Ejecutar la siguiente instrucción en la línea de comandos (abrir terminal): 
< Insertar foto >
```
promt> python3 matching.py CSV_COMP CSV_STU N
```
Siendo: 
```
matching.py = nombre del script
CSV_COMP = ./encuestas/<fichero_compañias.csv>
CSV_STU = ./encuestas/<fichero_estudiantes.csv>
N = Número de rondas deseadas
```

## Mejoras. Reunión outcomes

squereformr(pdist(ratings.T, 'euclidean') # https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html
dm = pdist(X, lambda u, v: np.sqrt(((u-v)**2).sum()))

screenshots



