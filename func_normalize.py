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