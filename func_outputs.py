import pandas as pd

def create_matrix_ronda_empresa(rondas): 
    '''
    matriz cruzada rondas vs company mostrando el alumno en la celda
    '''
    df = pd.DataFrame()
    for x in rondas: 
        ronda = x['ronda']
        company = x['company']
        student = x['student']
        df.loc[ronda, company] = student
    df.fillna('', inplace=True)
    return df

def create_matrix_ronda_estudiante(rondas): 
    '''
    matriz cruzada rondas vs student mostrando la company en la celda
    '''
    df = pd.DataFrame()
    for x in rondas: 
        ronda = x['ronda']
        company = x['company']
        student = x['student']
        df.loc[ronda, student] = company
    df.fillna('', inplace=True)
    return df