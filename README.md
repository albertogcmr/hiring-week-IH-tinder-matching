# Tinder para empresas

Espero que guste

## UXUI Madrid
revisar el formulario para empresas, aparecen cosas como: 
- On a scale from 1 to 10, how much time will the employee be spending working on back end and front end?
- Además creo que es mejor hacer obligatorias TODAS las respuestas permitienedo en 'No es necesario' y el 'Nada'. 
- Mark the top 3 competencies you are looking for in an employee for this position -> esta pregunta está mal hecha. Debería ser como en web. Nada de respuesta múltiple


## Mejoras
Usar argparse. Mirar la doc
data.columns = data.columns.str.strip().str.lower() # strip nombre de columnas
data = data[["id", "year", "type", "country", "activity", "fatal"]] # quedarnos con las dimensiones que nos interesan, timespant fuera
