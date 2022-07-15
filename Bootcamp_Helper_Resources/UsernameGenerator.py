#Noluvuyo Ngogodo < 7113358510@bootcamp.wethinkcode.co.za>
from ast import Break
from xml.dom import UserDataHandler


def user_details():
    """
    Prompt user input
    """
#First name Validation
while True:
        fname = str(input("Enter First Name:\n")).lower()

        is_num = 0

        for letter in fname:
            if letter.isnumeric() == True:
                is_num += 1

                if is_num == 0:
                    break
                else:
                    print("Enter a valid First Name with no digits")
#Last Name validation
while True:
        lname = str(input("Enter Last Name:")).lower()

        is_num = 0

        for letter in lname:
            if letter.isnumeric() == True:
                is_num += 1
                if is_num == 0:
                    break
                else:
                    print("Enter a valid Last Name with no digits")

        while True:
            campus_name = str(input("Enter your campus:\n"))
            city = ""
            if campus_name == "Johannesburg" or campus_name == "Cape Town" or campus_name == "Durban" or campus_name == "Phokeng":
                city = user_campus(campus_name)
                print(city)
                break
            else:
                print("Enter campus")

while True:
current_year = int(input("Enter year\n"))
if current year






def create_user_name(first_name, last_name, cohort, final_campus):
        """
    Create and return a valid username
    """   

def user_campus(campus):
    """
    Return valid campus abbreviations
    """
if campus == "Johannesburg":
    return 'JHB'
    elif campus_name == "Cape Town":
        return 'CPT'
    elif campus_name == "Durban":
        return 'DBN'

    elif campus_name == "Phokeng":
        return 'PHO'    

if __name__ == '__main__':
    user_details()   