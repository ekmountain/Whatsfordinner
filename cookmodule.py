import random


def cook():
    print("Cooking your own food is the healthier option. Good for you.")
    recipes = ["chili", "salmon", "chicken fried rice", "chicken noodle soup", "tacos", "southwest stew",
               "grilled chicken", "roast chicken", "hamburgers", "steak", "homemade pizza", "orange glaze pork loin",
               "crispy pork medallions", "chicken alfredo", "chicken parmesan", "beef pot pie", "chicken pot pie",
               "rigatoni casserole", "spaghetti"]
    # make random selection
    random_option = random.choice(recipes)
    print(f"Your random selection is: {random_option}")
    # ask up to two more times for another option
    askagain = input("Are you happy with your selection? y/n ")
    if askagain == "y" or askagain == "Y":
        print("I'm glad I could help!")
    elif askagain == "n" or askagain == "N":
        random_option = random.choice(recipes)
        print(f"Your second random selection is: {random_option}")
        askagain = input("Are you happy with your selection? y/n ")
        if askagain == "n" or askagain == "N":
            random_option = random.choice(recipes)
            print(f"Your third, and final, random selection is: {random_option}")
        elif askagain == "y" or askagain == "Y":
            print("That wasn't too bad, I guess.")
        else:
            print("Am I a joke to you?")
