import pandas as pd

WEB_SURVEY_DIC = {
    'companies_questions': {
        "What is the name of your company?": "name", 
    
        'Does your company have specific language requirements for this position? [English]': 'english', 
        'Does your company have specific language requirements for this position? [Spanish]': 'spanish', 
        'Does your company have specific language requirements for this position? [Portuguese]': 'portuguese', 
        'Does your company have specific language requirements for this position? [French]': 'french', 
        'Does your company have specific language requirements for this position? [Dutch]': 'dutch', 
        'Does your company have specific language requirements for this position? [Catalan]': 'catalan', 

        'Where will this position be located?': 'location', 
        'Regarding remote working, how many days a week could the employee work off site?': 'offsite', 
        'On a scale from 1 to 10, how much time will the employee be spending working on back end and front end?': 'position', 

        'Aside from the ones covered in our curriculum (MERN Stack), are there additional specific hard-skills you would value in an employee? [Java]': 'java', 
        'Aside from the ones covered in our curriculum (MERN Stack), are there additional specific hard-skills you would value in an employee? [C# / ASP.net]': 'caspnet',
        'Aside from the ones covered in our curriculum (MERN Stack), are there additional specific hard-skills you would value in an employee? [Python]': 'python',
        'Aside from the ones covered in our curriculum (MERN Stack), are there additional specific hard-skills you would value in an employee? [PHP]': 'php',
        'Aside from the ones covered in our curriculum (MERN Stack), are there additional specific hard-skills you would value in an employee? [SQL]': 'sql',
        'Aside from the ones covered in our curriculum (MERN Stack), are there additional specific hard-skills you would value in an employee? [Angular (Typescript generation)]': 'angular',
        'Aside from the ones covered in our curriculum (MERN Stack), are there additional specific hard-skills you would value in an employee? [Vue]': 'vue',
        'Aside from the ones covered in our curriculum (MERN Stack), are there additional specific hard-skills you would value in an employee? [Firebase]': 'firebase',
        'Aside from the ones covered in our curriculum (MERN Stack), are there additional specific hard-skills you would value in an employee? [AWS]': 'aws',
        'Aside from the ones covered in our curriculum (MERN Stack), are there additional specific hard-skills you would value in an employee? [Docker / Kubernetes]': 'dockerkubernetes',
        'Aside from the ones covered in our curriculum (MERN Stack), are there additional specific hard-skills you would value in an employee? [Design Tools (Photoshop, Illustrator...)]': 'design', 

        'From this list, please rank these 3 soft skills in order of importance for this position [Motivation and ability to overcome problems: employee has a passionate, can-do attitude and proactively looks for solutions to every problem they encounter]': 'motivation',
        'From this list, please rank these 3 soft skills in order of importance for this position [Coachability: Employee is receptive and actively listens and acts on feedback received]': 'coachability',
        'From this list, please rank these 3 soft skills in order of importance for this position [Teamwork: Employee is able to receive and provide value in a team environment]': 'teamwork', 
        }, 
    'students_questions': {
        "What is your full name?": "name", 
        
        'What is your level in the following languages? [English]': 'english', 
        'What is your level in the following languages? [Spanish]': 'spanish', 
        'What is your level in the following languages? [Portuguese]': 'portuguese', 
        'What is your level in the following languages? [French]': 'french', 
        'What is your level in the following languages? [Dutch]': 'dutch', 
        'What is your level in the following languages? [Catalan]': 'catalan', 
        
        'What are your preferences for job location?': 'location', 
        'What is your preference in terms of remote working?': 'offsite', 
        'In you role, how would you prefer to allocate your time between working on backend and working on frontend?': 'position', 
        
        'Aside from the ones covered in our curriculum (MERN Stack), do you have experience with additional specific hard-skills? [Java]': 'java', 
        'Aside from the ones covered in our curriculum (MERN Stack), do you have experience with additional specific hard-skills? [C# / ASP.net]': 'caspnet',
        'Aside from the ones covered in our curriculum (MERN Stack), do you have experience with additional specific hard-skills? [Python]': 'python',
        'Aside from the ones covered in our curriculum (MERN Stack), do you have experience with additional specific hard-skills? [PHP]': 'php',
        'Aside from the ones covered in our curriculum (MERN Stack), do you have experience with additional specific hard-skills? [SQL]': 'sql',
        'Aside from the ones covered in our curriculum (MERN Stack), do you have experience with additional specific hard-skills? [Angular (Typescript generation)]': 'angular',
        'Aside from the ones covered in our curriculum (MERN Stack), do you have experience with additional specific hard-skills? [VueJS]': 'vue',
        'Aside from the ones covered in our curriculum (MERN Stack), do you have experience with additional specific hard-skills? [Firebase]': 'firebase',
        'Aside from the ones covered in our curriculum (MERN Stack), do you have experience with additional specific hard-skills? [AWS]': 'aws',
        'Aside from the ones covered in our curriculum (MERN Stack), do you have experience with additional specific hard-skills? [Docker / Kubernetes]': 'dockerkubernetes',
        'Aside from the ones covered in our curriculum (MERN Stack), do you have experience with additional specific hard-skills? [Design Tools (Photoshop, Illustrator...)]': 'design', 
        
        "From this list of soft skills, please rank in order the ones you consider you're stronger at [Motivation and ability to overcome problems: I am passionate, have a can-do attitude and proactively look for solutions to every problem.]": 'motivation',
        "From this list of soft skills, please rank in order the ones you consider you're stronger at [Coachability: I am receptive and actively listen and act on the feedback I receive]": 'coachability',
        "From this list of soft skills, please rank in order the ones you consider you're stronger at [Teamwork: I'm able to receive and provide value in a team environment]": 'teamwork',  
    }, 
    'resp_language': {
        # Company
        "No need": 1, 
        "Must be able to read basic documentation": 2, 
        "Must be able to read documentation and have an informal conversation": 3, 
        "Must be able to read documentation and communicate in a meeting": 4, 
        "Can work in full capacity in this language": 5, 
        # Student same
        "No Experience": 1, 
        "I'm able to read basic documentation": 2, 
        "I'm able to read documentation and have an informal conversation": 3, 
        "Able to read documentation and communicate in a meeting": 4, 
        "Can work in full capacity in this language": 5
    }, 
    'resp_location': {
        # Company
        "In the city where the campus is located": 1, 
        "In the country where the campus is located": 2, 
        "In a city in another country": 3, 
        # Student
        "In the city where the campus is located": 1, 
        "Anywhere in the country where the campus is located": 2, 
        "Anywhere in the world": 3
    }, 
    'resp_offsite': {
        # Company
        "100% office-based job. We're not keen on remote working.": 1, 
        "1-2 Days a week": 2, 
        "3+ Days. It's up to the employee": 3, 
        "100% remote-based job. No physical office.": 4, 
        # Student
        "100% office-based job.": 1, 
        "1-2 Days a week": 2, 
        "3+ Days": 3, 
        "100% remote-based job. No physical office.": 4
    }, 
    'hard_skills': {
        # Company
        "No Need": 1, 
        "Nice to have: They should have a basic knowledge": 2, 
        "Must have: Must be able to work with the technology on a regular basis": 3,   
        # Student
        "No Experience": 1, 
        "Basic Knowledge: I've played around with it": 2, 
        "Advanced Knowledge: I'm comfortable working with it": 3
    }

}

UXUI_SURVEY_DIC = {
    'companies_questions': {
        "What is the name of your company?": "name", 
    
        'Does your company have specific language requirements for this position? [English]': 'english', 
        'Does your company have specific language requirements for this position? [Spanish]': 'spanish', 
        'Does your company have specific language requirements for this position? [Portuguese]': 'portuguese', 
        'Does your company have specific language requirements for this position? [French]': 'french', 
        'Does your company have specific language requirements for this position? [Dutch]': 'dutch', 
        'Does your company have specific language requirements for this position? [Catalan]': 'catalan', 

        'Where will this position be located?': 'location', 
        'Regarding remote working, how many days a week could the employee work off site?': 'offsite', 
        'On a scale from 1 to 10, how much time will the employee be spending working on back end and front end?': 'position', 

        "Mark the top 3 competencies you are looking for in an employee for this position": "competencies", 
        # este cluster ahora no se usa
        'Aside from the ones covered in our curriculum (MERN Stack), are there additional specific hard-skills you would value in an employee? [Java]': 'java', 
        'Aside from the ones covered in our curriculum (MERN Stack), are there additional specific hard-skills you would value in an employee? [C# / ASP.net]': 'caspnet',
        'Aside from the ones covered in our curriculum (MERN Stack), are there additional specific hard-skills you would value in an employee? [Python]': 'python',
        'Aside from the ones covered in our curriculum (MERN Stack), are there additional specific hard-skills you would value in an employee? [PHP]': 'php',
        'Aside from the ones covered in our curriculum (MERN Stack), are there additional specific hard-skills you would value in an employee? [SQL]': 'sql',
        'Aside from the ones covered in our curriculum (MERN Stack), are there additional specific hard-skills you would value in an employee? [Angular (Typescript generation)]': 'angular',
        'Aside from the ones covered in our curriculum (MERN Stack), are there additional specific hard-skills you would value in an employee? [Vue]': 'vue',
        'Aside from the ones covered in our curriculum (MERN Stack), are there additional specific hard-skills you would value in an employee? [Firebase]': 'firebase',
        'Aside from the ones covered in our curriculum (MERN Stack), are there additional specific hard-skills you would value in an employee? [AWS]': 'aws',
        'Aside from the ones covered in our curriculum (MERN Stack), are there additional specific hard-skills you would value in an employee? [Docker / Kubernetes]': 'dockerkubernetes',
        'Aside from the ones covered in our curriculum (MERN Stack), are there additional specific hard-skills you would value in an employee? [Design Tools (Photoshop, Illustrator...)]': 'design', 

        'From this list, please rank these 3 soft skills in order of importance for this position [Motivation and ability to overcome problems: employee has a passionate, can-do attitude and proactively looks for solutions to every problem they encounter]': 'motivation',
        'From this list, please rank these 3 soft skills in order of importance for this position [Coachability: Employee is receptive and actively listens and acts on feedback received]': 'coachability',
        'From this list, please rank these 3 soft skills in order of importance for this position [Teamwork: Employee is able to receive and provide value in a team environment]': 'teamwork', 
        }, 

    'students_questions': {
        "NOMBRE Y APELLIDOS": "name", 
        
        'What is your level in the following languages? [English]': 'english', 
        'What is your level in the following languages? [Spanish]': 'spanish', 
        'What is your level in the following languages? [Portuguese]': 'portuguese', 
        'What is your level in the following languages? [French]': 'french', 
        'What is your level in the following languages? [Dutch]': 'dutch', 
        'What is your level in the following languages? [Catalan]': 'catalan', 
        
        'What are your preferences for job location?': 'location', 
        'What kind of roles are you open to in terms of remote working?': 'offsite', 
        'In you role, how would you prefer to allocate your time between working on UX and working on UI?': 'position', 
        
        'Mark the top 3 competencies you think you have': 'competencies', 
        # esto cambia, habrá que borrarlo
        'Aside from the ones covered in our curriculum (MERN Stack), do you have experience with additional specific hard-skills? [Java]': 'java', 
        'Aside from the ones covered in our curriculum (MERN Stack), do you have experience with additional specific hard-skills? [C# / ASP.net]': 'caspnet',
        'Aside from the ones covered in our curriculum (MERN Stack), do you have experience with additional specific hard-skills? [Python]': 'python',
        'Aside from the ones covered in our curriculum (MERN Stack), do you have experience with additional specific hard-skills? [PHP]': 'php',
        'Aside from the ones covered in our curriculum (MERN Stack), do you have experience with additional specific hard-skills? [SQL]': 'sql',
        'Aside from the ones covered in our curriculum (MERN Stack), do you have experience with additional specific hard-skills? [Angular (Typescript generation)]': 'angular',
        'Aside from the ones covered in our curriculum (MERN Stack), do you have experience with additional specific hard-skills? [VueJS]': 'vue',
        'Aside from the ones covered in our curriculum (MERN Stack), do you have experience with additional specific hard-skills? [Firebase]': 'firebase',
        'Aside from the ones covered in our curriculum (MERN Stack), do you have experience with additional specific hard-skills? [AWS]': 'aws',
        'Aside from the ones covered in our curriculum (MERN Stack), do you have experience with additional specific hard-skills? [Docker / Kubernetes]': 'dockerkubernetes',
        'Aside from the ones covered in our curriculum (MERN Stack), do you have experience with additional specific hard-skills? [Design Tools (Photoshop, Illustrator...)]': 'design', 
        
        "From this list of soft skills, please rank in order the ones you consider you're stronger at [Motivation and ability to overcome problems: I am passionate, have a can-do attitude and proactively look for solutions to every problem.]": 'motivation',
        "From this list of soft skills, please rank in order the ones you consider you're stronger at [Coachability: I am receptive and actively listen and act on the feedback I receive]": 'coachability',
        "From this list of soft skills, please rank in order the ones you consider you're stronger at [Teamwork: I'm able to receive and provide value in a team environment]": 'teamwork',  
    }, 
    'resp_language': {
        # Company
        "No need it": 1, 
        "Must be able to read documentation and have an informal conversation": 3, 
        "Must be able to read documentation and communicate in a meeting": 4, 
        "Can work in full capacity in this language": 5, 
        # Student same
        "I don't speak it": 1, 
        "I'm able to read basic documentation": 2, 
        "I'm able to read documentation and have an informal conversation": 3, 
        "Able to read documentation and communicate in a meeting": 4, 
        "Can work in full capacity in this language": 5
    }, 
    'resp_location': {
        # Company
        "In the city where the campus is located": 1, 
        "In the country where the campus is located": 2, 
        "Anywhere in the world": 3, 
        # Student
        "In the city where the campus is located": 1, 
        "In the country where the campus is located": 2, 
        "Anywhere in the world": 3
    }, 
    'resp_offsite': {
        # Company
        "100% office-based job. We're not keen on remote working.": 1, 
        "1-2 Days a week": 2, 
        "2+ Days. It's up to the employee": 3,      ################ 2+ debería se 3+
        "100% remote-based job. No physical office.": 4, 
        # Student
        "100% office-based job.": 1, 
        "1-2 Days a week": 2, 
        "3+ Days": 3, 
        "100% remote-based job. No physical office.": 4
    }, 
    'hard_skills': {    ###########3 esto ha cambiado ya, no hacen falta
        # Company
        "No Need": 1, 
        "Nice to have: They should have a basic knowledge": 2, 
        "Must have: Must be able to work with the technology on a regular basis": 3,   
        # Student
        "No Experience": 1, 
        "Basic Knowledge: I've played around with it": 2, 
        "Advanced Knowledge: I'm comfortable working with it": 3
    }

}

# WEB COLUMNS
NAME =       ['name']
LANGUAGES =  ['english', 'spanish', 'portuguese', 'french', 'dutch', 'catalan']
BACKGROUND = ['location', 'offsite', 'position']
WEB_HARDSKILLS = ['java', 'caspnet', 'python', 'php', 'sql', 'angular', 
              'vue', 'firebase', 'aws', 'dockerkubernetes', 'design']
SOFTSKILLS = ['motivation', 'coachability', 'teamwork']
COLUMNS_WEB = NAME + LANGUAGES + BACKGROUND + WEB_HARDSKILLS + SOFTSKILLS

# UXUI COLUMNS

NAME =       ['name']
LANGUAGES =  ['english', 'spanish', 'portuguese', 'french', 'dutch', 'catalan']
BACKGROUND = ['location', 'offsite', 'position']
COMPETENCIES = ['competencies']
UXUI_HARDSKILLS = ['user', 'methodologies', 'usability', 'information', 'interaction', 
              'visual', 'html', 'motion']
# COLUMNS_UXUI = NAME + LANGUAGES + BACKGROUND + UXUI_HARDSKILLS + SOFTSKILLS
COLUMNS_UXUI = NAME + LANGUAGES + BACKGROUND + COMPETENCIES + SOFTSKILLS
COLUMNS_UXUI_2 = NAME + LANGUAGES + BACKGROUND + UXUI_HARDSKILLS + SOFTSKILLS

# DATA COLUMNS


# ################################################################

# Funciones translate CSV

def translate_language(x, dic_resp_language): 
    return dic_resp_language.get(x, 0) # 0 default

def translate_location(x, dic_resp_location): 
    return dic_resp_location.get(x, 0) # 0 default

def translate_offsite(x, dict_resp_offsite): 
    return dict_resp_offsite.get(x, 0) # 0 default

def translate_position(x): 
    try: 
        return int(x)
    except: 
        return 5 # si no sabe que poner se pondrá un valor intermedio. 

def translate_hardskills(x, dict_hard_skills): 
    # print(dict_hard_skills)
    return dict_hard_skills.get(x, 0) # 0 default
    
# companies_enc = web_translate_csv(bootcamp, element = 'companies', path=companies_filename, dic=DIC_COMPANIES)

# def web_translate_csv(path, dic): 
def web_translate_csv(bootcamp, element, path): 
    '''
    esta funcion sirve para limpiar...
    '''
    if bootcamp == 'web': 
        if element == 'companies': 
            dic = WEB_SURVEY_DIC.get('companies_questions')
        elif element == 'students': 
            dic = WEB_SURVEY_DIC.get('students_questions')
        else: 
            raise ValueError('web_translate_csv: element invalido. No se ha introducido ni companies ni students')
    
    elif  bootcamp == 'uxui': 
        raise ValueError('No implementado todavía')
    
    elif  bootcamp == 'data': 
        raise ValueError('No implementado todavía')
    else: 
        raise ValueError('Bootcamp no implementado')
    
    # dic = WEB_SURVEY_DIC # probando
    df = pd.read_csv(path, sep=',') # abrimos el csv
    df.columns = df.columns.str.strip() # limpiamos las columnas de posibles terminadores \r\n
    
    df.rename(index=str, columns=dic, inplace=True) # renombramos las columnas según el diccionario pasado por parámetro
    
    # Mirar el orden, que ha cambiado
    # df = df[list(set(dic.values()))] # nos quedamos únicamente con las columnas que son value en el diccionario
    
    # TO DO
    df = df[COLUMNS_WEB] # nos quedamos únicamente con las columnas que son value en el diccionario
    # print(df.columns)
    df.set_index('name', inplace=True)
    
    # eliminamos duplicados
    df = df[~df.index.duplicated(keep='first')]
        
    # languages
    for language in LANGUAGES: 
        df[language] = df[language].apply(lambda x: translate_language(x, WEB_SURVEY_DIC.get('resp_language') ))
    
    # location
    df['location'] = df['location'].apply(lambda x: translate_location(x, WEB_SURVEY_DIC.get('resp_location')))
    
    # offsite 
    df['offsite'] = df['offsite'].apply(lambda x: translate_offsite(x, WEB_SURVEY_DIC.get('resp_offsite')))
    
    # position
    df['position'] = df['position'].apply(translate_position)
    
    # hardskills 
    for hardskill in WEB_HARDSKILLS: 
        df[hardskill] = df[hardskill].apply(lambda x: translate_hardskills(x, WEB_SURVEY_DIC.get('hard_skills')))
    
    return df


#########################################################################3
#############   UXUI    ###################################################

'''
# https://datascience.stackexchange.com/questions/11797/split-a-list-of-values-into-columns-of-a-dataframe


import pandas

df = pandas.Series([('Adventure', 'Drama', 'Fantasy'), ('Comedy', 'Family'), ('Drama', 'Comedy', 'Romance'), (['Drama']), 
                    (['Documentary']), ('Adventure', 'Biography', 'Drama', 'Thriller')]).apply(frozenset).to_frame(name='genre')
for genre in frozenset.union(*df.genre):
    df[genre] = df.apply(lambda _: int(genre in _.genre), axis=1)
    
df.head()
'''
def uxui_translate_csv(bootcamp, element, path): 
    if bootcamp == 'uxui': 
        if element == 'companies': 
            dic = UXUI_SURVEY_DIC.get('companies_questions')
        elif element == 'students': 
            dic = UXUI_SURVEY_DIC.get('students_questions')
        else: 
            raise ValueError('web_translate_csv: element invalido. No se ha introducido ni companies ni students')
    
    elif  bootcamp == 'web': 
        raise ValueError('No implementado todavía')
    
    elif  bootcamp == 'data': 
        raise ValueError('No implementado todavía')
    else: 
        raise ValueError('Bootcamp no implementado')

    # dic = WEB_SURVEY_DIC # probando
    df = pd.read_csv(path, sep=',') # abrimos el csv

    df.columns = df.columns.str.strip() # limpiamos las columnas de posibles terminadores \r\n
    
    df.rename(index=str, columns=dic, inplace=True) # renombramos las columnas según el diccionario pasado por parámetro
    # Mirar el orden, que ha cambiado
    # df = df[list(set(dic.values()))] # nos quedamos únicamente con las columnas que son value en el diccionario
    
    # TO DO
    # df = df[COLUMNS_UXUI] # nos quedamos únicamente con las columnas que son value en el diccionario

    # df.set_index('name', inplace=True)
        
    # languages
    for language in LANGUAGES: 
        df[language] = df[language].apply(lambda x: translate_language(x, UXUI_SURVEY_DIC.get('resp_language') ))
    
    # location
    df['location'] = df['location'].apply(lambda x: translate_location(x, UXUI_SURVEY_DIC.get('resp_location')))
    
    # offsite 
    df['offsite'] = df['offsite'].apply(lambda x: translate_offsite(x, UXUI_SURVEY_DIC.get('resp_offsite')))
    
    # position
    df['position'] = df['position'].apply(translate_position)
        
    def uxui_translate_hardskills(x, hardskill): 
        return 1 if hardskill.lower() in x.lower() else 0
    
    # hardskills 
    for hardskill in UXUI_HARDSKILLS: 
        df[hardskill] = df['competencies'].apply(lambda x: uxui_translate_hardskills(x, hardskill))

    df = df[COLUMNS_UXUI_2] # nos quedamos únicamente con las columnas necesarias
    df.set_index('name', inplace=True)  # name será el índice
    
    # eliminamos duplicados
    df = df[~df.index.duplicated(keep='first')]
    # print(df.iloc[0, :]) # test de position a nulo
    return df