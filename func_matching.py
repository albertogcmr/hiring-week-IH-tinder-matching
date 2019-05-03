from scipy.spatial import distance
import pandas as pd
import numpy as np

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
    '''
    return calc_match(distance.euclidean(s_array, c_array, weights_val))

def calc_match(distance): 
    ''' [0, 1] -> [1, 0]'''
    return 1/(1+distance)

def match(student, company, weights): 
    student = [min(s, c) for s, c in zip(student, company)] # añadimos para que la sobrecualificación de un estudiante no penalice
    return calc_dist(student, company, list(weights.values()))

# create dataframe de tamañ0 SxC



def calculate_match(df1, df2, bootcamp): 
    
    matching = pd.DataFrame(np.zeros((len(df1), len(df2))) , columns=df2.index, index=df1.index)

    pesos = PESOS.get(bootcamp, 'Error')
    print(pesos)
    for s in matching.index: 
        for c in matching.columns:
            try: 
                matching.loc[s, c] = match(df1.loc[s], df2.loc[c], pesos)
            except: 
                matching.loc[s, c] = 0
    return matching