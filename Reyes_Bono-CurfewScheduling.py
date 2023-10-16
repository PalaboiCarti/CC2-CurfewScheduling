#oct/16/2023 11:14
#12th commit XD
#v1.1

districts = [1, 2, 3, 4, 5, 6, 7, 8, 9]

blue = [districts[0], districts[2], districts[4]]
red = [districts[1], districts[3], districts[5]]
green = [districts[6], districts[7], districts[8]]

red_marketday = "MarketDays : Mon, Wed. 06:00 - 21:00"
red_curfew = "Curfew: Mon, Wed, Sat. 20:00 - 05:00"

blue_marketday = "MarketDays : Tue, Sat. 06:00 - 19:00"
blue_curfew = "Curfew: Mon, Tue, Fri. 20:00 - 05:00"

green_marketday = "Thur, Fri. 06:00 - 19:00"
green_curfew = "Tue, Fri, Sat. 20:00 - 06:00"

print(f""" 
15-10-2023
Version 1.0

 ██████╗███████╗███████╗███████╗
██╔════╝╚══███╔╝██╔════╝██╔════╝
██║       ███╔╝ ███████╗███████╗
██║      ███╔╝  ╚════██║╚════██║
╚██████╗███████╗███████║███████║
 ╚═════╝╚══════╝╚══════╝╚══════╝

                City Z Schedule System™
                                """)


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


def get_district():
    while True:
        print("Please enter your district number as an integer")
        try:
            district = int(input("District "))
            if district in districts:
                while True:
                    print("---------------------")
                    print(f"Entered District: District {district}")
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
        except ValueError:
            print("Error: Input is not an integer. Please try again.")
            print("---------------------")


# curfew generator
def get_schedule(age, district):
    while True:
        if district in red:
            if age > 60 or age < 18:
                print(f"    -{red_marketday}")
                print(f"    -{red_curfew}")
                return
            else:
                print(f"    -{red_marketday}")
                return

        elif district in blue:
            if age > 60 or age < 18:
                print(f"    -{blue_marketday}")
                print(f"    -{blue_curfew}")
                return
            else:
                print(f"    -{blue_marketday}")
                return

        elif district in green:
            if age > 60 or age < 18:
                print(f"    -{green_marketday}")
                print(f"    -{green_curfew}")
                return
            else:
                print(f"    -{green_marketday}")
                return

        else:
            print("Error: Invalid credentials. Please enter a registered district.")


def display_profile():
    name = get_name()
    age = get_age()
    district = get_district()
    print(f"NAME : {name}")
    print(f"AGE : {age}")
    if district in red:
        print(f"DISTRICT : RED")
    elif district in blue:
        print(f"DISTRICT : BLUE")
    elif district in green:
        print(f"DISTRICT : GREEN")
    else:
        print(f"DISTRICT : UNIDENTIFIED")
    print(f"ALLOTED SCHEDULES:")
    schedule = get_schedule(age, district)
    print(f"    -Sunday Curfew: 21:00 - 06:00")

    def retry():
        while True:
            print("---------------------")
            response = input("Do you want to run the profile setup again? (y/n): ")
            if response == "y":
                print("---------------------")
                display_profile()
            elif response == "n":
                print("---------------------")
                print("Thank you for using CZSS.")
                print("Exiting program..")
                break
            else:
                print("Invalid response. Please enter 'y' or 'n'.")

    retry()


display_profile()
