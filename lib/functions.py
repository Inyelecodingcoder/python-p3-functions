#!/usr/bin/env python3

def greet_programmer():
    pass
    print("Hello, programmer!")
    return greet_programmer
greet_programmer()

def greet(name):
    pass
    print(f"Hello, {name}!")
    return greet
greet("Naureen")

def greet_with_default(name="programmer"):
    pass
    print(f"Hello, {name}!")
    return greet_with_default
greet_with_default()

def greet_with_default(name="programmer"):
    pass
    print(f"Hello, {name}!")
    return greet_with_default
greet_with_default("Sunny")

def add(num1, num2):
    pass
    result = num1 + num2
    print(result)
    return (result)

sum = add(45,55)
print(sum)


def halve(number):
    pass
    if type(number) not in (int, float):
        return None

    return number / 2
halve(100)    