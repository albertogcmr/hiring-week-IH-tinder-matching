# Tinder para empresas

Script para el area de Outcomes de Ironhack. Permite crear rondas de emparejamiento entre empresas y estudiantes dando prioridad a las de mayor afinididad (matching) entre alumno y empresa y procurando que todos los alumnos tengan un número similar de entrevistas. 
Este script utiliza python 3 y varias librerías. 

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

screenshots
3 views: desde companies, desde students, matriz cruzada con rondas: 
```
https://docs.google.com/spreadsheets/d/18SUFPnRMS3qnD5hDGcIpd3CeYnTf9sK8_Jb6mMj939g/edit#gid=1412799612
```




## Encuestas Web

```
Forms Students: 
https://docs.google.com/spreadsheets/d/1tESGSKhoOWekvYnvMypd6t1eFXN_av8F60wyxPkbUb8/edit#gid=1960323408

Forms Company: 
https://docs.google.com/spreadsheets/d/1AHnY6-E9w__BNcWqiS2rkqYbNlmqaU6nPFiPHDDKRfI/edit#gid=730113545

Encuestas Students: 
https://docs.google.com/forms/d/1w85z6lqZdQfByTMiefqUcth16-F9NnLHuZuh9CVHxyU/edit#responses

Encuestas Company: 
https://docs.google.com/forms/d/1JOjjmV1W-ay7h00wVtpcQzD6FHNJU8Qg6RRz1ptDN4Q/edit
```
### Actual BNC web
```
Students (tab 11APR): https://docs.google.com/spreadsheets/d/128bKUO5In9JPMMs9JTLAhL-KxnmhiB3L2qSdyGKdxnY/edit#gid=1970037490

Companies (tab 11APR): https://docs.google.com/spreadsheets/d/1r6zryUQRl3X_4sbcfzpUrNIuT8lBAxVC7Ov7tItmfhc/edit#gid=1943728679
```
### Madrid web
```
https://docs.google.com/spreadsheets/d/1bk_R2l83sWOd8VQyQV3R_n2Ikzx69QrMpfyvg6PpYms/edit?ts=5cb6d4ad#gid=177161654
```
