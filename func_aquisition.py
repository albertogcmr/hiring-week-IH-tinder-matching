from func_encuestas import web_translate_csv# , DIC_COMPANIES, DIC_STUDENTS

def adquisition_survey(bootcamp, companies_filename, students_filename):
    if bootcamp == 'web': 
        companies_enc = web_translate_csv(bootcamp, 'companies', companies_filename)
        students_enc = web_translate_csv(bootcamp, 'students', students_filename)
    elif bootcamp == 'uxui': 
        # TO DO
        raise ValueError('uxui bootcamp no implementado')
    elif bootcamp == 'data': 
        # TO DO
        raise ValueError('data bootcamp no implementado')
    else: 
        raise ValueError('bootcamp no implementado')

    return companies_enc, students_enc

def save_clean_dfs(): 
    pass