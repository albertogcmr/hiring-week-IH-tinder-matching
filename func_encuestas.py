import pandas as pd


DIC_COMPANIES = {
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
    'From this list, please rank these 3 soft skills in order of importance for this position [Teamwork: Employee is able to receive and provide value in a team environment]': 'teamwork' # El \r del final es para que sirva de terminador
    }

DIC_STUDENTS = {
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
    'Aside from the ones covered in our curriculum (MERN Stack), do you have experience with additional specific hard-skills? [Design Tools (Photoshop, Illustrator...)]': 'design', # esta es nueva
    
    "From this list of soft skills, please rank in order the ones you consider you're stronger at [Motivation and ability to overcome problems: I am passionate, have a can-do attitude and proactively look for solutions to every problem.]": 'motivation',
    "From this list of soft skills, please rank in order the ones you consider you're stronger at [Coachability: I am receptive and actively listen and act on the feedback I receive]": 'coachability',
    "From this list of soft skills, please rank in order the ones you consider you're stronger at [Teamwork: I'm able to receive and provide value in a team environment]": 'teamwork' # El \r del final es para que sirva de terminador
    }

LANGUAGES = ['english', 'spanish', 'portuguese', 'french', 'dutch', 'catalan']

HARDSKILLS = ['java', 'caspnet', 'python', 'php', 'sql', 'angular', 
              'vue', 'firebase', 'aws', 'dockerkubernetes', 'design']

# ################################################################

# Funciones translate CSV

def translate_language(x): 
    DIC_RESP_LANGUAGE = {
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
    }
    return DIC_RESP_LANGUAGE.get(x, 0) # 0 default

def translate_location(x): 
    DIC_RESP_LOCATION = {
        # Company
        "In the city where the campus is located": 1, 
        "In the country where the campus is located": 2, 
        "In a city in another country": 3, 
        # Student
        "In the city where the campus is located": 1, 
        "Anywhere in the country where the campus is located": 2, 
        "Anywhere in the world": 3
    }
    return DIC_RESP_LOCATION.get(x, 0) # 0 default


def translate_offsite(x): 
    DIC_RESP_OFFSITE = {
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
    }
    return DIC_RESP_OFFSITE.get(x, 0) # 0 default

def translate_position(x): 
    try: 
        return int(x)
    except: 
        return 0

def translate_hardskills(x): 
    DIC_RESP_HARDSKILLS = {
        # Company
        "No Need": 1, 
        "Nice to have: They should have a basic knowledge": 2, 
        "Must have: Must be able to work with the technology on a regular basis": 3,   
        # Student
        "No Experience": 1, 
        "Basic Knowledge: I've played around with it": 2, 
        "Advanced Knowledge: I'm comfortable working with it": 3
    }
    return DIC_RESP_HARDSKILLS.get(x, 0) # 0 default
    
def translate_csv(path, dic): 
    df = pd.read_csv(path, sep=',') # abrimos el csv
    df.columns = df.columns.str.strip() # limpiamos las columnas de posibles terminadores \r\n
    
    df.rename(index=str, columns=dic, inplace=True) # renombramos las columnas según el diccionario pasado por parámetro
    
    df = df[list(dic.values())] # nos quedamos únicamente con las columnas que son value en el diccionario
    df.set_index('name', inplace=True)
    
    # eliminamos duplicados
    df = df[~df.index.duplicated(keep='first')]
        
    # languages
    for language in LANGUAGES: 
        df[language] = df[language].apply(translate_language)
    
    # location
    df['location'] = df['location'].apply(translate_location)    
    
    # offsite
    df['offsite'] = df['offsite'].apply(translate_offsite)
    
    # position
    df['position'] = df['position'].apply(translate_position)
    
    # hardskills
    for hardskill in HARDSKILLS: 
        df[hardskill] = df[hardskill].apply(translate_hardskills)
    
    return df