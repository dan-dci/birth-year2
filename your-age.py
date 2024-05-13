# main.py

def calculate_birth_year(current_year, month_of_birth, day_of_birth, age):
    # Get today's date
    from datetime import date
    today = date.today()
    
    # Check if the user's birthday has already occurred this year
    birthday_this_year = date(today.year, month_of_birth, day_of_birth)
    
    if today < birthday_this_year:
        # If today's date is before the user's birthday this year, subtract an additional year
        return current_year - age - 1
    else:
        # If the user's birthday has passed, subtract the age normally
        return current_year - age

def main():
    import datetime
    current_year = datetime.datetime.now().year
    
    name = input("What is your name? ")
    
    try:
        age = int(input("How old are you? "))
    except ValueError:
        print("Please enter a valid age (it should be a number).")
        return

    try:
        month_of_birth = int(input("What is your birth month (1-12)? "))
        if month_of_birth < 1 or month_of_birth > 12:
            print("Please enter a valid month (1-12).")
            return
    except ValueError:
        print("Please enter a valid month (1-12).")
        return
    
    try:
        day_of_birth = int(input("What is your birth day (1-31)? "))
        if day_of_birth < 1 or day_of_birth > 31:
            print("Please enter a valid day (1-31).")
            return
    except ValueError:
        print("Please enter a valid day (1-31).")
        return

    # Calculate the year of birth using the adjusted method
    birth_year = calculate_birth_year(current_year, month_of_birth, day_of_birth, age)
    
    # Prepare the full date of birth string in the format YYYY-MM-DD
    date_of_birth = f"{birth_year}-{month_of_birth:02d}-{day_of_birth:02d}"
    
    print(f"Hello, {name}! You were probably born on {date_of_birth}.")

if __name__ == "__main__":
    main()
