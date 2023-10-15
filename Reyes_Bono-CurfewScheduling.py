#oct/15/2023 04:59
#second commit lol

def get_age():
    while True:
        age_str = input("Enter age: ")
        if age_str.isdigit():
            age = int(age_str)
            if age > 0:
                return age
            else:
                print("Error: Your age can't be negative. Try again.")
        else:
            print("Error: Your age should be a whole number. Please try again.")

def get_district(age):
    blue = ["District 1", "District 3", "District 5"]
    red = ["District 2", "District 4", "District 6"]
    green = ["District 7" "District 8", "District 9"]
    
    blue_marketday = "MarketDay : Tue, Sat. 06:00 - 19:00"
    blue_curfew = "Curfew: Mon, Tue, Fri. 10:00 - 05:00"
    while True:
        district = input("Enter district: ")
        if district in blue:
            if age > 60 or age < 18:
                return blue_marketday, blue_curfew
            else:
                return blue_marketday
        else:
            print("Error: Invalid credentials. Please enter a registered district.")

def display_profile():
    age = get_age()
    district = get_district(age)

    print(f"==> I am {age} years old.")
    print(f"==> Schedules: {district}.")
display_profile()
