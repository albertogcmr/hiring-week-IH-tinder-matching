# Tinder para empresas

Script para el area de Outcomes de Ironhack. Permite crear rondas de emparejamiento entre empresas y estudiantes dando prioridad a las de mayor afinididad (matching) entre alumno y empresa. 
Este script utiliza python 3 y varias librerías. 

## UXUI Madrid
revisar el formulario para empresas, aparecen cosas como: 
- On a scale from 1 to 10, how much time will the employee be spending working on back end and front end?
- Además creo que es mejor hacer obligatorias TODAS las respuestas permitienedo en 'No es necesario' y el 'Nada'. 
- Mark the top 3 competencies you are looking for in an employee for this position -> esta pregunta está mal hecha. Debería ser como en web. Nada de respuesta múltiple


## Mejoras
### TO DO
Usar argparse. Mirar la doc
```
######## jluna: https://github.com/JavierLuna/jluna-commands/blob/master/github
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="Command to execute", choices=['create', 'list', 'clone'], type=str)
    parser.add_argument("-n", "--projectname", help="Project name", type=str, required=False, default="Default")
    parser.add_argument("-p", "--public", help="Public repo", action="store_true")
    parser.add_argument("-u", "--upload", help="Detects local git repo and commits it to github repo",
                        action="store_true")
    parser.add_argument("--ssh", help="Forces ssh use to push to repo", action="store_true")

    args = parser.parse_args()

    if args.command == 'create':
        clone_url = create_github_repo(args)
        if clone_url is None:
            return
        if args.upload:
            upload_local_to_github(clone_url)
    elif args.command == 'list':
        list_all_repos(args)

    elif args.command == 'clone':
        clone_repo(args)


if __name__ == '__main__':
main()
```
### DONE
data.columns = data.columns.str.strip().str.lower() # strip nombre de columnas
data = data[["id", "year", "type", "country", "activity", "fatal"]] # quedarnos con las dimensiones que nos interesan, timespant fuera


## Instrucciones
1. Descargar como CSV el excel correspondiente a las repuestas de la encuesta de las **compañías**. La carpeta destino será ```./encuestas``` y el nombre destino 
2. Descargar como CSV el excel correspondiente a las repuestas de la encuesta de los **estudiantes**. La carpeta destino será ```./encuestas```. 
3. Ejecutar la siguiente instrucción en la línea de comandos: 
```
$> python3 matching.py CSV_COMP CSV_EST N
```
Siendo: 
```
matching.py = nombre del script
CSV_COMP = ./encuestas/<fichero_compañias.csv>
CSV_EST = ./encuestas/<fichero_estudiantes.csv>
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
