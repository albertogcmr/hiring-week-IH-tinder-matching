import pandas as pd
from random import shuffle


def least_common(queue):
    ''' Ordenar por menos número de entrevistas en diccionario input: queue '''
    return sorted(queue, key=queue.get, reverse=False)

def get_next_interview_eq_times(lista_matching_ordenada, used, students_dict_queue, pref_students=True): 
    # https://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html
    # Constrained minimization of multivariate scalar functions (minimize)
    
    # ordena los estudiantes por prioridad según el que tenga menos entrevistas concertadas 
    # # y soólo los que no estén en used
    elements_ordered = [elem for elem in least_common(students_dict_queue) if elem not in used]
    not_pref, pref = 'company', 'student'
    if not pref_students: 
        not_pref, pref = pref, not_pref

    for elem in elements_ordered: # según el orden de los menos entrevistados
        for match in lista_matching_ordenada:
            if match.get(pref) == elem and match.get(not_pref) not in used: # TO DO all() 
                return match # Devuelve el primer match válido, según el orden de least_common()
    return None # Ningún match válido

def get_rondas(lista_matching, n_rondas, students, companies, min_interviews_per_company): 

    lista_matching_ordenada = sorted(lista_matching, key = lambda x: x['weight'], reverse=True)
    students_dict_queue = {student: 0 for student in students}
    companies_dict_queue = {company: 0 for company in companies}
    res = []

    for ronda in range(n_rondas): # rondas

        # dentro de cada ronda
        used = []
        for _ in range(len(companies)): # num mesas = num companies

            if min(companies_dict_queue.values()) < min_interviews_per_company: 
                # interview = get_next_interview_eq_companies(lista_matching_ordenada, used, companies_dict_queue)
                interview = get_next_interview_eq_times(lista_matching_ordenada, used, companies_dict_queue, pref_students=False)
            
            else: 
                # interview = get_next_interview_eq_students(lista_matching_ordenada, used, students_dict_queue)
                interview = get_next_interview_eq_times(lista_matching_ordenada, used, students_dict_queue, pref_students=True)

            if interview == None: 
                break

            student, company, w = interview.get('student'), interview.get('company'), interview.get('weight')
            used.extend([student, company]) # añadimos empresa y compañia para que no vuelvan a aparecer en esta ronda
            lista_matching_ordenada.remove(interview) # eliminamos el matching para que no se repita

            res.append({'ronda': ronda, 'company': company, 'student': student, 'weight': w})
            students_dict_queue[student] += 1 

            # actualizamos el número de entrevistas que llevan student y company
            companies_dict_queue[company] += 1

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