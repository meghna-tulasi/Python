"""
For doctests run following command:
python -m doctest -v binary_search.py
or
python3 -m doctest -v binary_search.py

For manual testing run:
python binary_search.py
"""
from __future__ import print_function
import bisect


def binary_search(sorted_collection, item):
    """
    Examples:
    >>> binary_search([0, 5, 7, 10, 15], 0)
    0

    >>> binary_search([0, 5, 7, 10, 15], 15)
    4

    >>> binary_search([0, 5, 7, 10, 15], 5)
    1

    >>> binary_search([0, 5, 7, 10, 15], 6)

    """
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        midpoint = (left + right) // 2
        current_item = sorted_collection[midpoint]
        if current_item == item:
            return midpoint
        else:
            if item < current_item:
                right = midpoint - 1
            else:
                left = midpoint + 1
    return None


def binary_search_std_lib(sorted_collection, item):
    """

    Examples:
    >>> binary_search_std_lib([0, 5, 7, 10, 15], 0)
    0

    >>> binary_search_std_lib([0, 5, 7, 10, 15], 15)
    4

    >>> binary_search_std_lib([0, 5, 7, 10, 15], 5)
    1

    >>> binary_search_std_lib([0, 5, 7, 10, 15], 6)

    """
    index = bisect.bisect_left(sorted_collection, item)
    if index != len(sorted_collection) and sorted_collection[index] == item:
        return index
    return None

def binary_search_by_recursion(sorted_collection, item, left, right):
    midpoint = left + (right - left) // 2

    if sorted_collection[midpoint] == item:
        return midpoint
    elif sorted_collection[midpoint] > item:
        return binary_search_by_recursion(sorted_collection, item, left, right-1)
    else:
        return binary_search_by_recursion(sorted_collection, item, left+1, right)

def __assert_sorted(collection):
    """

    Examples:
    >>> __assert_sorted([0, 1, 2, 4])
    True

    >>> __assert_sorted([10, -1, 5])
    Traceback (most recent call last):
    ...
    ValueError: Collection must be sorted
    """
    if collection != sorted(collection):
        raise ValueError('Collection must be sorted')
    return True


if __name__ == '__main__':
    import sys
 
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    user_input = input_function('Enter numbers separated by coma:\n')
    collection = [int(item) for item in user_input.split(',')]
    try:
        __assert_sorted(collection)
    except ValueError:
        sys.exit('Sequence must be sorted to apply binary search')

    target_input = input_function(
        'Enter a single number to be found in the list:\n'
    )
    target = int(target_input)
    result = binary_search(collection, target)
    if result is not None:
        print('{} found at positions: {}'.format(target, result))
    else:
        print('Not found')
