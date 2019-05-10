# Imports

import numpy as np
import pandas as pd

from random import shuffle

from func_matching import calculate_match
from func_args import get_args
from func_grafos import create_graph, get_best_match
from func_aquisition import adquisition_survey
from func_outputs import outputs
from func_normalize import *


def most_common(lst):
    return max(set(lst), key=lst.count)

def get_rondas(G, n_rondas, student_queue, companies): 
    res = []
    mesas = len(companies)
    for r in range(n_rondas): 
        used = []
        
        for interview in range(mesas): 
            # debería ser el studiante que más sale en student_queue
            student = most_common(student_queue) 
            
            m = get_best_match(G, student, used)
            if m == None: 
                break
            node1, node2, w = m
            G.remove_edge(node1, node2)
            used.extend([node1, node2]) # añadimos empresa y compañia para que no vuelvan a aparecer en esta ronda
            
            if node1 not in companies: # si el nodo1 no es nombre de compañía, debemos intercambiar
                node2, node1 = node1, node2
            res.append({'ronda': r, 'company': node1, 'student': node2, 'weight': w})
            student_queue.remove(node2)
    return res    

def generate_student_queue(students_list, n_rondas): 
    shuffle(students_list)
    return students_list * n_rondas


def main(): 
    # Captura de argumentos. 
    bootcamp, companies_filename, students_filename, n_rondas = get_args()
    
    # DFs limpios
    companies, students = adquisition_survey(bootcamp, companies_filename, students_filename)
    
    # Normalize
    students, companies = normalize_2dfs(students, companies)
    
    # TO DO: crear la tabla matching
    matching = calculate_match(students, companies, bootcamp)

    G = create_graph(matching)
    
    students_list_queue = generate_student_queue(list(matching.index), n_rondas)
    # display(students_list_queue)
        
    # vamos a recorrer la lista para ir emparejando
    rondas = get_rondas(G, n_rondas, students_list_queue, list(matching.columns))
    
    outputs(rondas)


if __name__== '__main__':
    main()

