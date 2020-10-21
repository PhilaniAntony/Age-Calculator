#Age claclculator in seconds

from datetime import datetime

def ageCalculator ():
    print('============= Welcome To Age Calculator ================')
    try:
        #create a current time varible
        current_date =datetime.now()
        
        #Capture user birth date in string format
        birthdate = input('Please provide your birthday in the following format 3/9/1990  \n ')
        
        #strip the datetime from birthdate
        edited_date = datetime.strptime(birthdate, "%d/%m/%Y")
        human_formated_date = edited_date.strftime("%d %B %Y ")
        
        #claculate age in days
        age_in_days = current_date - edited_date
        
        #conert the age from days to seconds
        age_in_seonds = age_in_days.total_seconds()
        print('**************************************************************************')
        print(f'Born {human_formated_date}, you are {age_in_seonds} seconds old')
        print('Thank you for using our app')
        print('**************************************************************************')
        
    except (TypeError , ValueError):
        print('Please follow the format given')
        raise SystemExit
        
        
ageCalculator()