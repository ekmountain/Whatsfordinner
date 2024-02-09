import fastfoodrandomizermodule
import sitdownrestaurantrandomizer


def eatOut():
    answer1 = input("Do you want to eat at a) a fastfood restaurant or b) a sit down restaurant? ")
    if answer1 == "a" or answer1 == "A":
        fastfoodrandomizermodule.fastfoodrandomizer()
    elif answer1 == "b" or answer1 == "B":
        sitdownrestaurantrandomizer.sitdownrestaurant()
    else:
        print("Am I a joke to you?")
