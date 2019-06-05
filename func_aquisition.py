from func_encuestas import web_translate_csv, uxui_translate_csv

def adquisition_survey(bootcamp, companies_filename, students_filename):
    '''
    input: 
        bootcamp-type ['web', 'uxui', 'data], 
        companies_filename: path, 
        students_filename: path
    output: 
        companies_enc: pandas.DataFrame, 
        students_enc: pandas.DataFrame
    '''
    if bootcamp == 'web': 
        companies_enc = web_translate_csv(bootcamp, 'companies', companies_filename)
        students_enc = web_translate_csv(bootcamp, 'students', students_filename)
    elif bootcamp == 'uxui': 
        companies_enc = uxui_translate_csv(bootcamp, 'companies', companies_filename)
        students_enc = uxui_translate_csv(bootcamp, 'students', students_filename)
    elif bootcamp == 'data': 
        # TO DO
        raise ValueError('data bootcamp no implementado')
    else: 
        raise ValueError('bootcamp no implementado')

    return companies_enc, students_enc

def save_clean_dfs(): 
    ''' Obsotele '''
    pass