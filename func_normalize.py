from sklearn.preprocessing import MinMaxScaler
import pandas as pd


def normalize_2dfs(students, companies): 

    # display(students)
    # display(companies)

    # print('concat')
    df = pd.concat([students, companies])
    # display(df)

    scaler = MinMaxScaler()
    df[df.columns] = scaler.fit_transform(df[df.columns]) # para no perder el tipo DataFrame
    # print('normalizado')
    # display(df)

    #ahora separar df en students/companies y devolverlos
    studentsx = df.head(len(students))
    # display(studentsx)
    companiesx = df.tail(len(companies))
    # display(studentsx)
    # print(students.index == studentsx.index)
    # print(companies.index == companiesx.index)

    return studentsx, companiesx

def normalize_list_matches(list_matches): 
    df = pd.DataFrame(list_matches)
    print('df')
    display(df)

    '''
    Reshape your data either using array.reshape(-1, 1) if your data has a single feature or 
    array.reshape(1, -1) if it contains a single sample.
    '''
    x = df.weight.values.reshape(-1, 1) #returns a numpy array
    min_max_scaler = MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    df.weight = x_scaled
    print('df normalizada')

    display(df)

    # ahora cambiamos [1, 0] -> [0, 1]
    df.weight = 1 - df.weight
    print('df ahora cambiamos [1, 0] -> [0, 1]')

    display(df)
    df = round_column(df, column='weight', decimals=2) # rdondeamos a 2 decimales
    res = df.to_dict(orient='records')
    print('lista de diccionarios', res)
    return res

def round_column(df, column='weight', decimals=2): 
    df[column] = df[column].round(decimals)
    return df