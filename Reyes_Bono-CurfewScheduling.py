#oct/15/2023 05:44
#Fifth commit mahnegggga

districts = ["District 1", "District 2", "District 3", "District 4", "District 5", "District 6", "District 7", "District 8", "District 9"]

def get_age():
    while True:
        try:
            age = int(input("Enter age: "))
            return age
        except ValueError:
            print("Invalid input")
            
#get district 
def get_district():
    while True:
        district = input("Enter District: ")
        if district in districts:
            print("Registered district")
        else:
            print("Unregistered district")
        return district
  
#curfew generator
def get_schedule(age, district):
    blue = [districts[0], districts[2], districts[4]]
    red = [districts[1], districts[3], districts[5]]
    green = [districts[6], districts[7], districts[8]]
    
    blue_marketday = "MarketDays : Tue, Sat. 06:00 - 19:00"
    blue_curfew = "Curfew: Mon, Tue, Fri. 10:00 - 05:00"
    red_marketday = "MarketDays : Mon, Wed. 06:00 - 21:00"
    while True:
        if district in blue:
            if age > 60 or age < 18:
                return blue_marketday, blue_curfew
            else:
                return blue_marketday
        else:
            print("Error: Invalid credentials. Please enter a registered district.")

def display_profile():
    age = get_age()
    district = get_district()
    schedule = get_schedule(age, district)

    print(f"==> I am {age} years old.")
    print(f"==> Schedules: {schedule}.")

display_profile()





