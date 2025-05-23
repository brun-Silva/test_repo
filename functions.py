# Assuming the 'functions.py' contains a basic summation function
def sum_numbers(numbers):
    """
    Sums a list of numbers.

    :param numbers: list of numbers to sum.
    :return: sum of the numbers.
    """
    # Check if the input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers")

    total = 0
    for number in numbers:
        # Ensure each element is a number
        if not isinstance(number, (int, float)):
            raise ValueError("All elements must be numbers")
        total += number
    
    return total