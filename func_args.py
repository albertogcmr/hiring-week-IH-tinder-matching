import argparse

def get_args2(): 
    # TO DO con argparse
    bootcamp = 'web'
    companies_filename = './input/Web Company Form (Responses) .csv'
    students_filename = './input/Web Student Form (Responses) .csv'
    rondas = '11'
    
    return (bootcamp, companies_filename, students_filename, int(rondas))
    
def get_args(argv=None): 
    '''
    Funciona correctamente siendo llamado desde main
    '''
    valid_bootcamps = ['web', 'uxui', 'data']

    parser = argparse.ArgumentParser(description="Arguments for Hiring Fair")
    parser.add_argument("bootcamp", type=str, choices=valid_bootcamps, help="[web, uxui or data]")
    parser.add_argument("companiesCSV", type=str, help="Relative path to companies survey CSV")
    parser.add_argument("studentsCSV", type=str, help="Relative path to students survey CSV")
    parser.add_argument("rounds", type=int, help="Max rounds per hiring fair")

    args = parser.parse_args()
    return (args.bootcamp, args.companiesCSV, args.studentsCSV, args.rounds)
