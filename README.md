# Tinder para empresas

Script para el area de Outcomes de Ironhack. Permite crear rondas de emparejamiento entre empresas y estudiantes dando prioridad a las de mayor afinididad (matching) entre alumno y empresa y procurando que todos los alumnos tengan un número similar de entrevistas. 
Este script utiliza python 3 y varias librerías. 


## Fuentes 

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

revisar el formulario para empresas, aparecen cosas como: 
- On a scale from 1 to 10, how much time will the employee be spending working on back end and front end?
- Además creo que es mejor hacer obligatorias TODAS las respuestas permitienedo en 'No es necesario' y el 'Nada'. 
- Mark the top 3 competencies you are looking for in an employee for this position -> esta pregunta está mal hecha. Debería ser como en web. Nada de respuesta múltiple


## Instrucciones
1. Copiar ambos formularios desde la fuente original: 
	1. students form (URL_1)
	2. companies form (URL_2)
2. Enviar a los estudiantes y a las empresas que participan en la hiring fair su encuesta correspondiente. Mas detallado
3. Una vez que los formularios estén terminados generar la hoja de cálculo que proporciona google. 
4. descargar ambos excel en formato CSV 
5. copiar ambos csv en la carpeta input del proyecto
6. Ejecutar la siguiente instrucción en la línea de comandos (abrir terminal): 
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
3 views: desde companies, desde students, matriz cruzada con rondas: 
```
https://docs.google.com/spreadsheets/d/18SUFPnRMS3qnD5hDGcIpd3CeYnTf9sK8_Jb6mMj939g/edit#gid=1412799612
```



