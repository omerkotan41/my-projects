print("Welcome to Band Name Generator!")

length = int(input("How many words do you want your Band Name to consist of? \n"))

if length == 2:
    city = input("Please enter a name of city you want: \n")
    animal = input("Please enter a name of animal you want: \n")
    name = input("Please enter a name that you want it to be: \n")    

    from itertools import permutations
    names = [city , animal, name]
    for p in permutations(names, 2):
        band_name = " ".join(p)
        print("Your band name could be: " + band_name)

else:
    city = input("Please enter a name of city you want: \n")
    animal = input("Please enter a name of animal you want: \n")
    name = input("Please enter a name that you want it to be: \n")

    from itertools import permutations
    names = {city , animal, name}
    for p in permutations(names):
        band_name = " ".join(p)
        print("Your band name could be: " + band_name)

