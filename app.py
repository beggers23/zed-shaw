def counter():
    print("Input a number")
    num = int(input("> "))
    i = 0
    arr = []

    while (i < num):
        arr.append(i)
        i += 1
    return arr


counted = counter()
for num in counted:
    print(num)
