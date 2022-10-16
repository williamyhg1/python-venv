def days_to_units(days): 
    return int(days) * 24

def validate_and_execute():
    try:
        user_input_number = int(input("Please enter a number of days and I will convert it to hours!\n"))
        if (user_input_number) > 0:
            calculated_value = days_to_units(user_input_number)
            print(f"{user_input_number} days equal to {calculated_value} hours")
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number")
        else:
            print("You entered a negative number.")
    except:
        print("Your input is not a valid number.")
        


validate_and_execute()