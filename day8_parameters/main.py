def greet_with(name,loc):
    print(f"Hello, {name},")
    print(f"What is it like in {loc}?")
name = input("What is your name?: ")
location = input("What is your location?: ")
greet_with(name, location)