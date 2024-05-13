# main.py

def calculate_birth_year(current_year, age):
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

    birth_year = calculate_birth_year(current_year, age)
    
    print(f"Hello, {name}! You were probably born in {birth_year}.")

if __name__ == "__main__":
    main()
