import pandas as pd
from random import shuffle


def least_common(queue):
    ''' Ordenar por menos número de entrevistas en diccionario input: queue '''
    res = sorted(queue, key=queue.get, reverse=False)
    return res

def get_next_interview(lista_matching_ordenada, used, students_dict_queue, companies_dict_queue, min_interviews_per_company): 
    # https://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html
    # Constrained minimization of multivariate scalar functions (minimize)
    
    print(len(used))
    # ordena los estudiantes por prioridad según el que tenga menos entrevistas concertadas
    students_ordered = least_common(students_dict_queue) 
    companies_ordered = least_common(companies_dict_queue) 
    '''
    if len(used) == 42: 
        pass
        # print(companies_ordered)
        # print(companies_dict_queue)
        # print(lista_matching_ordenada)

    if min(companies_dict_queue.values()) < min_interviews_per_company: 
        # todavía no hemos llegado al cupo mínimo de entrevistas para empresas
        # print('echo', max(companies_dict_queue.values()))
        for company in companies_ordered: 
            for match in lista_matching_ordenada: 
                if company not in used and match.get('student') not in used: 
                    print('entra')
                    return match
                    '''
    if False: 
        pass
    else: 
        for student in students_ordered: # según el orden de los menos entrevistados
            if student not in used: 
                for match in lista_matching_ordenada:
                    if match['company'] not in used and student == match['student']: # TO DO all() 
                        return match # Devuelve el primer match válido, según el orden de least_common()
    """
    for student in students_ordered: # según el orden de los menos entrevistados
        if student not in used: 
            for match in lista_matching_ordenada:
                if match['company'] not in used and student == match['student']: # TO DO all() 
                    return match # Devuelve el primer match válido, según el orden de least_common()
    """
    return None # Ningún match válido

    
def get_rondas(lista_matching, n_rondas, students, companies, min_interviews_per_company): 

    lista_matching_ordenada = sorted(lista_matching, key = lambda x: x['weight'], reverse=True)
    students_dict_queue = {student: 0 for student in students}
    companies_dict_queue = {company: 0 for company in companies}

    # print(students_dict_queue)
    # print(companies_dict_queue)
    res = []

    for ronda in range(n_rondas): # rondas
        used = []
        for _ in range(len(companies)): # num mesas = num companies
            
            interview = get_next_interview(lista_matching_ordenada, used, students_dict_queue, companies_dict_queue, min_interviews_per_company)
            if interview == None: 
                break
            student, company, w = interview.get('student'), interview.get('company'), interview.get('weight')
            used.extend([student, company]) # añadimos empresa y compañia para que no vuelvan a aparecer en esta ronda
            lista_matching_ordenada.remove(interview) # eliminamos el matching para que no se repita

            res.append({'ronda': ronda, 'company': company, 'student': student, 'weight': w})
            students_dict_queue[student] += 1
            companies_dict_queue[company] += 1

    # print(students_dict_queue)
    # print(companies_dict_queue)
    # print(lista_matching_ordenada)
    return res    


def shuffle_rondas(lista_interviews): 
    rondas = sorted(list({interview.get('ronda') for interview in lista_interviews}))
    nuevas_rondas = [r for r in rondas]
    shuffle(nuevas_rondas)
    
    modificacion_rondas = {antigua: nueva for antigua, nueva in zip(rondas, nuevas_rondas)}

    for interview in lista_interviews: 
        interview['ronda'] = modificacion_rondas.get(interview['ronda'])
        
    lista_interviews = sorted(lista_interviews, key=lambda x: x['ronda'])
    return lista_interviews