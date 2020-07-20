def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []

    # get() returns the value of the item with the specified key.
    # abs() returns the absolute value of the specified number.

    for num in a:
        if cache.get(abs(num)):
            result.append(abs(num))

        else:
            cache[abs(num)] = num

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
