"""
For doctests run following command:
python -m doctest -v bubble_sort.py
or
python3 -m doctest -v bubble_sort.py

For manual testing run:
python bubble_sort.py
"""

from __future__ import print_function


def bubble_sort(collection):
    """
    Examples:
    >>> bubble_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> bubble_sort([])
    []

    >>> bubble_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    length = len(collection)
    for i in range(length-1, -1, -1):#range(length-1, -1, -1)
        for j in range(i):#range(1, i)
            if collection[j] > collection[j+1]:
                collection[j], collection[j+1] = collection[j+1], collection[j]

    return collection


if __name__ == '__main__':
    import sys
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    user_input = input_function('Enter numbers separated by a comma:\n')
    unsorted = [int(item) for item in user_input.split(',')]
    print(bubble_sort(unsorted))
