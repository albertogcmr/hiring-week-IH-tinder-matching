import pandas as pd
from random import shuffle


def least_common(queue):
    ''' Ordenar por menos número de entrevistas en la cola '''
    res = sorted(queue, key=queue.get, reverse=False)
    return res

def get_next_interview(lista_matching_ordenada, used, students_dict_queue): 
    
    # ordena los estudiantes por prioridad según el que tenga menos entrevistas concertadas
    students_ordered = least_common(students_dict_queue) 

    for student in students_ordered: # según el orden de los menos entrevistados
        if student not in used: 
            for match in lista_matching_ordenada:
                if match['company'] not in used and student == match['student']: # TO DO all() 
                    return match # Devuelve el primer match válido, según el orden de least_common()
    return None # Ningún matcha válido
    
def get_rondas(lista_matching, n_rondas, students, companies, min_interviews_for_company): 
    print(min_interviews_for_company)

    lista_matching_ordenada = sorted(lista_matching, key = lambda x: x['weight'], reverse=True)
    print(lista_matching_ordenada)
    students_dict_queue = generate_student_interviews(students)
    
    res = []
    for ronda in range(n_rondas): # rondas
        used = []
        for _ in range(len(companies)): # num mesas = num companies
            
            m = get_next_interview(lista_matching_ordenada, used, students_dict_queue)
            if m == None: 
                break
            student, company, w = m['student'], m['company'], m['weight']
            used.extend([student, company]) # añadimos empresa y compañia para que no vuelvan a aparecer en esta ronda
            lista_matching_ordenada.remove(m) # eliminamos el matching para que no se repita

            res.append({'ronda': ronda, 'company': company, 'student': student, 'weight': w})
            students_dict_queue[student] += 1
    return res    

def generate_student_interviews(students_list): 
    '''
    input: list of students
    output: dictionary key (student), value (0)
    '''
    return {student: 0 for student in students_list}

def shuffle_rondas(lista_interviews): 
    rondas = sorted(list({interview.get('ronda') for interview in lista_interviews}))
    nuevas_rondas = [r for r in rondas]
    shuffle(nuevas_rondas)
    
    modificacion_rondas = {antigua: nueva for antigua, nueva in zip(rondas, nuevas_rondas)}

    for interview in lista_interviews: 
        interview['ronda'] = modificacion_rondas.get(interview['ronda'])
        
    lista_interviews = sorted(lista_interviews, key=lambda x: x['ronda'])
    return lista_interviews