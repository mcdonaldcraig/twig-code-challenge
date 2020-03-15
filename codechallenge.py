"""From rhe passing in of and array and a positive integer return an array built from he array split by the integer

Usage:

    python 3 codechallenge <array> <integer>
 """

import sys


def create_split_array(arr, size):
    """Take the values of arr and size and split arr into lists of determined length

        Args:
            arr: The initial array
            size: the number of sub-arrays to be created in the list

        Returns:
            The desired list utilizing a list generator to produce
    """
    length = len(arr)
    # Check that the size value is not larger than the list length
    if size > length:
        print(f"the split size cannot be larger than: " + str(length))
        exit()
    else:
        check_array(arr)
        check_number(size)
        q, r = divmod(length, size)
        return (arr[i * q + min(i, r):(i + 1) * q + min(i + 1, r)] for i in range(size))


def check_array(arr):
    """Check the array is not empty

        Args:
            arr: The array that is to be split

        Returns:
            the array if not empty
    """
    if len(arr) == 0:
        raise ValueError(f"The array input cannot be empty")

    return arr


def check_number(size):
    """Checks the size value is not 0 or a negative number

        Args:
            size: the amount of sub-arrays that the array is to be split into

        Returns:
              The size value if not 0 or a negative number
    """
    if size <= 0:
        raise ValueError(f"the number must be greater than 0")

    return size


def print_output(output):
    """Will output out the array in a nice format

        Args:
            output: The list output from create_split_array()

        Returns:
              a readable version of the output i.e. [[1], [2], [3], [4]]
    """
    print(list(output))


def main(arr, size):
    """Call the create_split_array function and pass output to print_output()

        Args:
            arr: the array that is to be split
            size: The number of arrays to split arr into

    """
    output = create_split_array(arr, size)
    print_output(output)


if __name__ == '__main__':
    # ensure that the first sys value is turned into a list, and the second is being passed as an integer
    main(sys.argv[1].split(','), int(sys.argv[2]))
