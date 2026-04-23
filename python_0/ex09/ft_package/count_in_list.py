def count_in_list(lst, item):
    """Count the number of occurrences of item in lst."""
    count = 0
    for elem in lst:
        if elem == item:
            count += 1
    return count