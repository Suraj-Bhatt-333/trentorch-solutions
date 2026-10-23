def count_comparisons_linear_search(arr, target):
    """
    arr:    a list of numbers
    target: the value being searched for

    Returns:
        (found, comparisons): found is True if target is in arr, False
        otherwise. comparisons is the number of element-to-target
        comparisons actually performed (stop as soon as a match is
        found -- don't keep scanning).
    """
    # TODO: Implement a left-to-right linear scan, counting comparisons.
    comparisions = 0
    is_found = False
    for i in arr:
        if i==target:
            is_found = True
            comparisions += 1
            break
        comparisions +=1
    return (is_found, comparisions)


def count_comparisons_binary_search(sorted_arr, target):
    """
    sorted_arr: a list of numbers, already sorted ascending
    target:     the value being searched for

    Returns:
        (found, comparisons): same shape as count_comparisons_linear_search,
        but using binary search -- each comparison must actually halve
        the remaining search space.
    """
    # TODO: Implement binary search from Theory, counting one
    # comparison per midpoint check.
    left = 0
    right = len(sorted_arr)-1
    comparisions = 0
    is_found = False
    while(left<=right):
        mid = left + (right-left)//2
        if sorted_arr[mid]==target:
            is_found=True
            comparisions +=1
            break 
        elif sorted_arr[mid]<target:
            comparisions +=1
            left = mid+1
        else:
            comparisions +=1
            right = mid -1
    return (is_found, comparisions)
