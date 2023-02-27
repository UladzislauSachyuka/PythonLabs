import random


def list_of_even_numbers():
    return [element for element in random.sample(range(0, 100), 10) if element % 2 == 0]
