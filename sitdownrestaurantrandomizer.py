import random


def sitdownrestaurant():
    restaurants = ["Texas Roadhouse", "Culver's", "Shake Shack", "Mi Cancun", "Goji Bistro", "Chili's", ]
    displaylist = input("Do you want to see a list of the available options? y/n ")
    if displaylist == "Y" or displaylist == "y":
        print("Here is a list of the available options: ")
        for location in restaurants:
            print(location)
    random_option = random.choice(restaurants)
    print(f"Your random selection is: {random_option}")
    # ask if user wants another option
    askagain = input("Are you happy with your selection? y/n ")
    if askagain == "y" or askagain == "Y":
        print("I'm glad I could help!")
    elif askagain == "n" or askagain == "N":
        random_option = random.choice(restaurants)
        print(f"Your second random selection is: {random_option}")
        askagain = input("Are you happy with your selection? y/n ")
        if askagain == "n" or askagain == "N":
            random_option = random.choice(restaurants)
            print(f"Your third, and final, random selection is: {random_option}")
        elif askagain == "y" or askagain == "Y":
            print("That wasn't too bad, I guess.")
        else:
            print("Am I a joke to you?")
    else:
        print("Am I a joke to you?")
