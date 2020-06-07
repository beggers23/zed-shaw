# Exercise 18

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_one(arg):
    print(f"arg: {arg}")


def print_none():
    print("nonthing")


print_two("Zed", "Shaw")
print_two_again("B", "Eggs")
print_one("First!")
print_none()
