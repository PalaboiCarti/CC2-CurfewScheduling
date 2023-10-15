#oct/15/2023 05:11
#third commit lmfaooo

def get_age():
    while True:
        try:
            age = int(input("Enter age: "))
            return age
        except ValueError:
            print("Invalid input")

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


