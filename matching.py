#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Imports

import numpy as np
import pandas as pd


from func_args import get_args
from func_aquisition import adquisition_survey
from func_normalize import *
from func_matching import calculate_match
from func_rondas import get_rondas, shuffle_rondas
from func_outputs import outputs, create_matrix_matching


# main
def main(): 
    # Captura de argumentos. 
    bootcamp, companies_filename, students_filename, n_rondas = get_args()
    
    # DFs limpios
    df_companies, df_students = adquisition_survey(bootcamp, companies_filename, students_filename)
    
    # Normalize
    students, companies = normalize_2dfs(df_students, df_companies)

    # TO DO: crear la tabla matching
    lista_matching = calculate_match(students, companies, bootcamp)
    
    # Función principal para generar la lista de rondas ordenadas
    lista_interviews = get_rondas(lista_matching, n_rondas, students.index, companies.index)
    
    # barajamos para que todos estén igualmente motivados en cada entrevista
    lista_interviews = shuffle_rondas(lista_interviews)
    
    # obtenemos el excel de output deseado
    outputs(lista_interviews, lista_matching)


if __name__== '__main__':
    main()

