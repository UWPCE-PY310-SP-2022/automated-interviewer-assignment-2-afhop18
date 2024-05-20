#-----------------------------------------------------------------------------#
# Title: Assignment02 - simple method of assignment (no tuples / lists)
# Desc: This script is an automated interviewer using asking question
# of the user and providing feedback based on that answer using only input
# and strings
# Change Log:
#   Andrew Hopkins, 5/13/2024, created script
#-----------------------------------------------------------------------------#

Q1: str = input("What is your name? ")
print(f"You have entered {Q1} as your name\n")

Q2: str = input("What is your conference ID? ")
print(f"You have entered {Q2} as your conference ID\n")

Q3: str = input("Which organization do you represent? ")
print(f"You have entered {Q3} as the organization you represent\n")

Q4: str = input("What is your email address? ")
print(f"You have entered {Q4} as your email address\n")

Q5: str = input("Please state any food preferences you have? ")
print(f"You have given {Q5} as your food preferences\n")

ses1: str = "Python for Beginners"
attend: str = input(f"Do you wish to attend {ses1}? (Y/N):")
if attend in {"Y","y"}:
    print(f"You have elected to attend {ses1}\n")
else:
    print(f"You have elected not to attend {ses1}\n") #anything other than Y submits non-attendence

ses2: str = "Database Development with Python"
attend = input(f"Do you wish to attend {ses2}? (Y/N):")
if attend in {"Y","y"}:
    print(f"You have elected to attend {ses2}\n")
else:
    print(f"You have elected not to attend {ses2}\n") #anything other than Y submits non-attendence

ses3: str = "Python for Data Science"
attend = input(f"Do you wish to attend {ses3}? (Y/N):")
if attend in {"Y","y"}:
    print(f"You have elected to attend {ses3}\n")
else:
    print(f"You have elected not to attend {ses3}\n") #anything other than Y submits non-attendence

ses4: str = "Advanced Python for Application Developers"
attend = input(f"Do you wish to attend {ses4}? (Y/N):")
if attend in {"Y","y"}:
    print(f"You have elected to attend {ses4}\n")
else:
    print(f"You have elected not to attend {ses4}\n") #anything other than Y submits non-attendence





