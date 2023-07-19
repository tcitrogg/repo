# variables && naming conventions
name = ""
# - pascal case
# - camel case
averageAge = 10
AverageAge = 10
# - snake case
average_age = 10

name1 = "asd"

# control flow I :[conditional stmt]
# if expression:
#     run this block of code
# age = 18

# if age >= 13:
#     print("You're good!")

# age 13 - 18
# if 13 <= age <= 18:
#     print("Yeah! can sign up")
# else:
#     print("Nah! cannot say sign up")

# choice = input("Enter the masterpiece: ")

# if choice == "one_piece":
#     print("onigiri")
# elif choice == "naruto":
#     print("rasengan")
# elif choice == "bleach":
#     print("bankai")
# else:
#     print("kon ni chi wa")


# if choice != "black":
#     print("You white??")


# answer = input("Do you want to continue installation? [Y/n]: ").upper()

# if answer == "Y":
#     print("(+) Downloading...")
# else:
#     print("(x) Exiting...")

answer = int(input("Your age: "))

if 13 <= answer <= 18:
    print("Yeah! can sign up")
else:
    print("Nah! cannot say sign up")

# types II :[list, tuple, dict, set]

# control flow II :[loop stmt]

# range

# break