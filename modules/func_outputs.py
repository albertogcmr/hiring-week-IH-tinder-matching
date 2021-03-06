import pandas as pd


def create_matrix_matching(matching): 
    df = pd.DataFrame()
    for x in matching: 
        company = x['company']
        student = x['student']
        match = x['weight']
        df.loc[student, company] = match
    return df

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

def create_excel_output(dfs, path='output/output.xlsx'):
    writer = pd.ExcelWriter(path)
    for i, df in enumerate(dfs, 1): 
        df.to_excel(writer,'Sheet{}'.format(i))
    writer.save()

def report_matching(df): 
    students = df.student.value_counts()
    companies = df.company.value_counts()
    num_rondas = df.ronda.nunique()
    
    print('entrevistas alumnos (max, min): ({}, {})'.format(students.max(), students.min()))
    print('entrevistas empresas (max, min): ({}, {})'.format(companies.max(), companies.min()))
    print('Num. Rondas: {}'.format(num_rondas))

def outputs(rondas, lista_matching): 
    df = pd.DataFrame.from_dict(rondas, orient='columns')
    df_matrix = create_matrix_ronda_empresa(rondas)
    df_matrix2 = create_matrix_ronda_estudiante(rondas)
    df_matrix3 = create_matrix_matching(lista_matching)
    
    dfs = [df, df_matrix, df_matrix2, df_matrix3]
    create_excel_output(dfs)
    report_matching(df)

    