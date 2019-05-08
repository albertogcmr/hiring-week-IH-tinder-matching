

# normalizacion. Por columnas en alumnos o empresas hay un 0.0 y un 1.0
def normalize_2dfs_xx(students, companies): 
    # print(students.min(), companies.max())
    
    mins = [min(s, c) for s, c in zip(students.min(), companies.min())]    
    maxs = [max(s, c) for s, c in zip(students.max(), companies.max())]
    if any(m==0 for m in maxs): 
        raise ValueError('Imposible normalizar: Va a dividir por Zero')
    students = (students-mins)/(maxs-mins) # checkear indeterminación
    companies = (companies-mins)/(maxs-mins)
    
    return students, companies

# FUNCIONA
# normalizacion. Por columnas en alumnos o empresas hay un 0.0 y un 1.0
def normalize_2dfs(students, companies): 
    # print(students.min(), companies.max())
    
    mins = [min(s, c) for s, c in zip(students.min(), companies.min())]
    students = students-mins
    companies = companies-mins
    
    # maxs = [max(s, c, 1) for s, c in zip(students.max(), companies.max())]
    maxs = [max(s, c) for s, c in zip(students.max(), companies.max())]
    if any(m==0 for m in maxs): 
        raise ValueError('Imposible normalizar: Va a dividir por Zero')
    students = students/maxs
    companies = companies/maxs
    
    return students, companies