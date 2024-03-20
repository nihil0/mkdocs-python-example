"""
This is an example module for which we generate documentation with mkdocs
"""


def my_function(a: int, b: int) -> int:
    """
    Returns the sum of a and b

    Args:
        a: first number
        b: second number

    Returns:
        sum of both numbers
    """
    return a + b


def my_other_function(name: str) -> None:
    """
    Greets the person whose name is passed as an argument

    Args:
        name: name of the person to be greeted
    """
    print(f"Hello {name}")


class Car:
    """
    The car class represent a car with a make and a model
    """
    def __init__(self, make: str, model: str):
        """
        Initialize the attributes to describe a car.

        Args:
            make: make of the car, e.g., BMW
            model: model of the car, e.g., 3-series
        """
        self.make = make
        self.model = model

    def display_car(self):
        """
        Prints information about the car.
        """
        print(f"This car is a {self.make} {self.model}.")
