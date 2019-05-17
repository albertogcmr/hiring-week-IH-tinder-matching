from scipy.spatial import distance
import pandas as pd
import numpy as np

from func_normalize import normalize_list_matches

PESOS = {
    'web': {
        'english': 1,
        'spanish': 1,
        'portuguese': 1,
        'french': 1,
        'dutch': 1,
        'catalan': 1,
        'location': 1, 
        'offsite': 1,
        'position': 5, # importante
        'java': 5,     # importante las técnicas
        'caspnet': 5,
        'python': 5,
        'php': 5,
        'sql': 5,
        'angular': 5,
        'vue': 5,
        'firebase': 5,
        'aws': 5,
        'dockerkubernetes': 5,
        'design': 5,
        'motivation': 1,
        'coachability': 1,
        'teamwork': 1
    }, 
    'uxui': {}, 
    'data': {}
}


def calc_dist(s_array, c_array, weights_val): 
    ''' 
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.euclidean.html
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cosine.html
    scipy.spatial.distance.cosine

    input: 
        s_array: float array from one student dimension, 
        c_array: float array from one company dimension, 
        weights_val: weights for the euclidean distance
    output: 
        res: weighted euclidean distance
    '''
    # quito esto para no hacer la invertida
    # res = invert_match(distance.euclidean(s_array, c_array, weights_val))
    return distance.euclidean(s_array, c_array, weights_val)

# deprecated
def invert_match(distance): 
    ''' 
    [0, N] -> [1, 1/(1+N)]
    input: euclidean distance
    output: affinity
    commentary: 
        1: Best Match
        0.x: Worst Match
    '''
    res =  1/(1+distance)
    return res

def match(student, company, weights): 
    '''
    input: 
        student: float array from one student dimension, 
        company: float array from one company dimension, 
        weights: dictionary of weights for the euclidean distance 
    output: 
        res:  weighted euclidean distance rounded to 2-digits
    important: 
        student is modified in order not to penalize overcualification
    '''
    student = [min(s, c) for s, c in zip(student, company)] 
    return calc_dist(student, company, list(weights.values()))


def calculate_match(df1, df2, bootcamp): 
    '''
    input: 
        df1: students_DataFrame, 
        df2: companies_DataFrame,
        bootcamp: type-bootcamp
    output: 
        res: list of dictionaries: [{'student': 'Alex', 'company': 'BBVA', 'weight': 0.34}, {}, ...]
    '''
    res = []
    pesos = PESOS.get(bootcamp, 'Error') # bootcamp 'web'??

    for s in df1.index: 
        for c in df2.index:
            try: 
                weight = match(df1.loc[s], df2.loc[c], pesos)
                res.append({'student': s, 'company': c, 'weight': weight})
            except: 
                res.append({'student': s, 'company': c, 'weight': 0})
    
    # ahora normalizamos los pesos y [0,1] -> [1, 0]
    list_matches_normalized = normalize_list_matches(res)
    return list_matches_normalized 




