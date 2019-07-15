import argparse
   
   
def get_args(argv=None): 
    '''
    input: main args
    output: 
        args.bootcamp: ['web', 'uxui', 'data], 
        args.companiesCSV: path, 
        args.studentsCSV: path, 
        args.rounds: number of rounds for the hiring
    '''
    # $ python3 matching.py web ./input/company-web-mad.csv ./input/student-web-mad.csv 14
    valid_bootcamps = ['web', 'uxui', 'data']

    # --nombre_arg lo hace opcional
    parser = argparse.ArgumentParser(description="Arguments for Hiring Fair")
    parser.add_argument("bootcamp", type=str, choices=valid_bootcamps, help="[web, uxui or data]")
    parser.add_argument("companiesCSV", type=str, help="Relative path to companies survey CSV")
    parser.add_argument("studentsCSV", type=str, help="Relative path to students survey CSV")
    parser.add_argument("rounds", type=int, help="Max rounds per hiring fair")
    parser.add_argument("-mi", "--min_interviews_for_company", type=int, default=0, help="Min interviews per company")

    args = parser.parse_args()
    return (args.bootcamp, args.companiesCSV, args.studentsCSV, args.rounds, args.min_interviews_for_company)


def get_args2(): 
    ''' 
    Only for Test 
    '''      
    
    bootcamp = 'uxui'
    companies_filename = './input/uxui company matchmaking form template (Responses) - Form Responses 1.csv'
    students_filename = './input/uxui student matchmaking form template (Responses) - Form Responses 1.csv'
    rondas = '17'
    min_interviews_for_company = '5'
    
    '''
    bootcamp = 'web'
    companies_filename = './input/web company matchmaking form template (Responses) - Form Responses 1.csv'
    students_filename = './input/web student matchmaking form template (Responses) - Form Responses 1.csv'
    rondas = '17'
    '''
    
    return (bootcamp, companies_filename, students_filename, int(rondas), int(min_interviews_for_company))
