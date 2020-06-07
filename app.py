# Guesses in comments
print("1", True and True)  # True
print("2", False and True)  # False
print("3", 1 == 1 and 2 == 1)  # False
print("4", "test" == "test")  # True
print("5", 1 == 1 or 2 != 1)  # True
print("6", True and 1 == 1)  # True
print("7", False and 0 != 0)  # False
print(True or 1 == 1)  # True
print("test" == "testing")  # False
print(1 != 0 and 2 == 1)  # False
print("test" != "testing")  # True
print("12", "test" == 1)  # False
print(not (True and False))  # True
print("curious now")
print(not (1 == 1 and 0 != 1))  # False
print(not (10 == 1 or 1000 == 1000))  # False
print(not (1 != 10 or 3 == 4))  # False
print(not ("testing" == "testing" and "Zed" == "Cool Guy"))  # True
print("harder still")
print(1 == 1 and (not("testing" == 1 or 1 == 0)))  # True
print("chunky" == "bacon" and (not (3 == 4 or 3 == 3)))  # False
print(3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")))  # False
