# Program to help us figure out what to eat for dinner
import eatoutmodule
import cookmodule


def main():
    # call welcome function with opening questions
    Welcome()
    # beginning narrowing down the options
    question1 = eatOutorCook()
    # sends them to modules that will give them their selections
    if question1 == "Eat out":
        eatoutmodule.eatOut()
    else:
        cookmodule.cook()
    # ends program
    goodbye()


# Welcome function
def Welcome():
    print("What's for dinner? Worst question ever!")
    print("Well here's hoping I can help you with that.")


# Asks the question if they want to eat out or cook
def eatOutorCook():
    answer1 = input("Do you want to a) eat out or b) cook? ")
    if answer1 == "a" or answer1 == "A":
        Q1 = "Eat out"
        return Q1
    elif answer1 == "b" or answer1 == "B":
        Q1 = "Cook"
        return Q1
    else:
        print("Listen, I'm just trying to help, if you don't want it that's fine with me.")


# asks if they want to repeat the process or end the program
def askquestionagain():
    askagain = input("Are you happy with your selections? y/n ")
    if askagain == "y" or askagain == "Y":
        print("I'm glad I could help!")
        goodbye()
    elif askagain == "n" or askagain == "N":
        eatOutorCook()
    else:
        print("Oh well.")
        goodbye()


# goodbye function
def goodbye():
    print("Until next time. Goodbye")


main()
