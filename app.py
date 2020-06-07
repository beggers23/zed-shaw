print("Let's practice everything")
print('You\'d need to know \'bout escapes with \\ that do: ')
print('\n new lines and \t tabs')

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explaination
\n\t\twhere there is none.
"""

print("-------------")
print(poem)
print("-------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 1000
formula = secret_formula(start_point)
# beans, jars, crates = secret_formula(start_point)
# print(f"We'd have {beans} beans, {jars} jars, and {crates} crates")

# Additional way to format a string
print("With a starting point of: {}".format(start_point))
print("We'd have {} beans, {} jars, and {} crates".format(*formula))
