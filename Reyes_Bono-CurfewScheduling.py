#oct/15/2023 05:18
#FOURTH COMMIT MOTHERFUCKER WAHAHAHAHAHAHHA HELL YEAH

districts = ["District 1", "District 2", "District 3", "District 4", "District 5", "District 6", "District 7", "District 8", "District 9"]

def get_age():
    while True:
        try:
            age = int(input("Enter age: "))
            return age
        except ValueError:
            print("Invalid input")
  
#curfew generator
def get_district(age):
    blue = [districts[0], districts[2], districts[4]]
    red = [districts[1], districts[3], districts[5]]
    green = [districts[6], districts[7], districts[8]]
    
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




