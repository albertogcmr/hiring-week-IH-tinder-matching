
# #################################################### #

def check_rondas(rondas): 
    res = []
    for ronda in rondas: 
        companies = [company for company, student, w in ronda]
        students = [student for company, student, w in ronda]
        res.append(len(set(companies)) == len(set(students)) )
    return all(e for e in res)

'''
check_rondas(rondas)    
'''

# #################################################### #

def rondas2string(rondas):
    res = ''
    for i, ronda in enumerate(rondas): 
        res += '\n\nRonda {}'.format(i)
        for c, s, w in ronda: 
            res += '\nCompany: {} -> Student: {} -> Matching: {}'.format(c, s, w)
        
    return res
        
'''        
text = rondas2string(rondas)
with open("Rondas.txt", "w") as f:
    f.write(text)
'''

# #################################################### #
# beautifultable
'''
table = BeautifulTable()
table.column_headers = ["ronda", "company", "student", "match"]
for i, ronda in enumerate(rondas): 
    for row in ronda: 
        table.append_row([i, row[0], row[1], row[2]])
with open("Rondas_table.txt", "w") as f:
    f.write(str(table))
'''

# #################################################### #
# agrupadas por compañía: 

'''
table = BeautifulTable()
table.column_headers = ["company", "ronda", "student", "match"]

for company in companies_list: 
    for i, ronda in enumerate(rondas): 
        for row in ronda: 
            if row[0] == company: 
                table.append_row([row[0], i, row[1], row[2]])

print(table)

with open("Rondas_table_by_company.txt", "w") as f:
    f.write(str(table))
'''
                
# #################################################### #
# Rondas_table_by_student  

'''
table = BeautifulTable()
table.column_headers = ["student", "company", "ronda", "match"]

for student in students_list: 
    for i, ronda in enumerate(rondas): 
        for row in ronda: 
            if row[1] == student: 
                table.append_row([row[1], row[0], i, row[2]])

with open("Rondas_table_by_student.txt", "w") as f:
    f.write(str(table))
    '''
# #################################################### #
 
'''    
student_rounds = {}

for student in students_list: 
    total = 0
    for ronda in rondas: 
        for row in ronda: 
            if row[1] == student: 
                total += 1
    student_rounds[student] = total

student_rounds
'''