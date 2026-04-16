def ft_filter(function, iterable):
    """Construct an iterator from those elements of iterable for which function returns true."""
    if function is None:
        return iterable

    result = []
    for element in iterable:
        if function(element):
            result.append(element)
    return result


# def is_even(n):
#     return n % 2 == 0

# print(ft_filter(is_even, [1, 2, 3, 4, 5,6, 7, 8, 10]))