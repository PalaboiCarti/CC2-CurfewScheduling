#oct/15/2023 07:42
#Eigth Commit hooooh

districts = ["District 1", "District 2", "District 3", "District 4", "District 5", "District 6", "District 7", "District 8", "District 9"]

blue_marketday = "MarketDays : Tue, Sat. 06:00 - 19:00"
blue_curfew = "Curfew: Mon, Tue, Fri. 10:00 - 05:00"
red_marketday = "MarketDays : Mon, Wed. 06:00 - 21:00"

def get_name():
    while True:
        print("Please follow this format: ")
        print("<LastName>, <FirstName(s)> <MiddleInitial>.")
        name = input("Enter your name: ")
        if all(char.isalpha() or char.isspace() or char in "., " for char in name):
            while True:
                print("---------------------")
                print(f"Entered name: {name}")
                confirmation = input("Please confirm if the credentials are correct (y/n): ")
                if confirmation == "y":
                    print("---------------------")
                    return name
                elif confirmation == "n":
                    print("Resubmit credentials.")
                    print("---------------------")
                    break  
                else:
                    print("Invalid response. Please enter 'y' or 'n'.")
        else:
            print("Error: Invalid credentials. Please try again.")
            print("---------------------")


def get_age():
    while True:
        try:
            age = int(input("Enter age: "))
            while True:
                print("---------------------")
                print(f"Entered age: {age}")
                confirmation = input("Please confirm if the credentials are correct (y/n): ")
                if confirmation == "y":
                    print("---------------------")
                    return age
                elif confirmation == "n":
                    print("Resubmit credentials.")
                    print("---------------------")
                    break  
                else:
                    print("Invalid response. Please enter 'y' or 'n'.")
        except ValueError:
            print("Invalid input")
            print("---------------------")
            
#get district 
def get_district():
    while True:
        district = input("Enter District: ")
        if district in districts:
            while True:
                print("---------------------")
                print(f"Entered District: {district}")
                confirmation = input("Please confirm if the credentials are correct (y/n): ")
                if confirmation == "y":
                    print("---------------------")
                    return district
                elif confirmation == "n":
                    print("Resubmit credentials.")
                    print("---------------------")
                    break  
                else:
                    print("Invalid response. Please enter 'y' or 'n'.")
        else:
            print("Error : Unidentified district.")
            print("Please select one of the following districts:")
            for district in districts:
                print(f"    -{district}")
  
#curfew generator
def get_schedule(age, district):
    blue = [districts[0], districts[2], districts[4]]
    red = [districts[1], districts[3], districts[5]]
    green = [districts[6], districts[7], districts[8]]
    
    while True:
        if district in blue:
            if age > 60 or age < 18:
                return blue_marketday, blue_curfew
            else:
                return blue_marketday
        else:
            print("Error: Invalid credentials. Please enter a registered district.")

def display_profile():
    name = get_name()
    age = get_age()
    district = get_district()
    schedule = get_schedule(age, district)
    
    print(f"NAME : {name}")
    print(f"AGE : {age}")
    print(f"ALLOTED SCHEDULES:")
    if isinstance(schedule, tuple) and blue_marketday in schedule and blue_curfew in schedule:
        print(f"    -{blue_marketday}")
        print(f"    -{blue_curfew}")
    else:
        print(f"    -{blue_marketday}")
    print(f"    -Sunday Curfew: 21:00 - 06:00")
    def retry():
        while True:
            response = input("Do you want to run the profile setup again? (y/n): ")
            if response == "y":
                display_profile()
            elif response == "n":
                print("Thank you for using CZSS.")
                print("Exiting program..")
                break
            else:
                print("Invalid response. Please enter 'y' or 'n'.")
    retry()


display_profile()
