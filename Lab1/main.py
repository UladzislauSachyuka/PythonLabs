from helloworld import hello_world
from operation import calculation
from even_numbers import list_of_even_numbers


def main():
    hello_world()
    print(calculation(5, 3, "sum"))
    print(list_of_even_numbers())


if __name__ == "__main__":
    main()
