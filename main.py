

def days_to_units(days): 
    return int(days) * 24

def validate_and_execute():
    try:
        user_input_number = set(input("Please enter a number of days and I will convert it to hours!\n").split(","))
        print(user_input_number)
        if len(user_input_number) > 0:
            for unit in user_input_number:
                if int(unit) == 0:
                    print("You entered a 0, please enter a valid positive number")
                elif int(unit) < 0:
                    print("You entered a negative number.")    
                else: 
                    calculated_value = days_to_units(unit)
                    print(f"{unit} days equal to {calculated_value} hours")
                
    except:
        print("Your input is not a valid number.")
        
switch = True


while switch:
    validate_and_execute()
    exit=str.lower(input("Do you want to exit?"))
    if exit == "yes":
        switch = False
    elif exit == "no":
        switch =True
    else:
        switch = True
