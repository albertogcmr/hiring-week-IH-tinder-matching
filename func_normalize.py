from sklearn.preprocessing import MinMaxScaler
import pandas as pd


def normalize_2dfs(dfstudents, dfcompanies): 
    ''' Escala ambos datasets para que el maximo y el mínimo se tengan de los dos '''

    df = pd.concat([dfstudents, dfcompanies])

    # DataConversionWarning: Data with input dtype int64 were all converted to float64 by MinMaxScaler
    df = df.astype(float)

    scaler = MinMaxScaler()
    print(df)
    df[df.columns] = scaler.fit_transform(df[df.columns]) # para no perder el tipo DataFrame
    print(df)

    #ahora separar df en students/companies y devolverlos
    studentsx = df.loc[dfstudents.index]
    companiesx = df.loc[dfcompanies.index]

    return studentsx, companiesx

def normalize_list_matches(list_matches): 
    ''' 
    Transforma una lista de diccionarios cuyos keys weight son las distancias entre student-company
    en la misma lista pero los pesos normalizados de [0-N] -> [0-1] y luego invierte para
    obtener [0-1] -> [1-0]
    '''
    df = pd.DataFrame(list_matches)
    '''
    HINT: documentation
    Reshape your data either using array.reshape(-1, 1) if your data has a single feature or 
    array.reshape(1, -1) if it contains a single sample.
    '''
    x = df.weight.values.reshape(-1, 1) #returns a numpy array
    min_max_scaler = MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    df.weight = x_scaled
    
    df.weight = 1 - df.weight # ahora cambiamos [1, 0] -> [0, 1]

    df = round_column(df, column='weight', decimals=2) # redondeamos a 2 decimales
    res = df.to_dict(orient='records')
    return res

def round_column(df, column='weight', decimals=2): 
    """ Redondea a 2 decimales la columna column """
    df[column] = df[column].round(decimals)
    return df