# 3.Write a function that takes a list of integers and returns the sum of the elements.
# If any element in the list is not an integer, the function should raise a ValueError.


def sum_of_integers(lst):
    # Check if all elements in the list are integers
    for element in lst:
        if not isinstance(element, int):
            raise ValueError(f"All elements must be integers. Found {type(element)} instead.")

    # Calculate the sum of the elements
    total_sum = sum(lst)
    return total_sum


# Example usage:
try:
    result = sum_of_integers([1, 2, 3, 4, 5])
    print(f"The sum of the elements is: {result}")

    # This will raise a ValueError
    result = sum_of_integers([1, 2, 'three', 4, 5])
    print(f"The sum of the elements is: {result}")
except ValueError as e:
    print(e)
