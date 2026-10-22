def countdown_with_skip(start: int) -> list:
    """
    Using a while loop, count down from `start` to 1 (inclusive),
    appending each number to a list, but skip appending any
    number that is exactly 3 (use continue for this).
    Do not use break here.
    Return the resulting list.
    """
    res =[]
    count = start
    while(count!=0):
        if count==3:
            count -= 1
            continue
        else:
            res.append(count)
            count -=1
    return res
        
        


def find_first_negative(numbers: list) -> int | None:
    """
    Using a while loop with an index variable, find and return
    the first negative number in `numbers`. Use break once found.
    If no negative number exists, use the loop's else clause to
    return None after the loop completes normally.
    """
    n = len(numbers)
    if n!=0:
        index =0
        found = 0
        while index<len(numbers):
            if numbers[index]<0:
                found =numbers[index]
                break
            index +=1
        if found==0:
            return None
        else:
            return found
    else: 
        return None


def sum_with_index(numbers: list) -> dict:
    """
    Using a for loop with enumerate(), build and return a
    dictionary mapping each index to the running sum of all
    numbers up to and including that index.

    Example: sum_with_index([10, 20, 30])
    -> {0: 10, 1: 30, 2: 60}
    """
    res = {}
    sum =0
    for idx,val in enumerate(numbers):
        sum += val
        res[idx] = sum 
    return res


def manual_iteration_trace(items: list) -> list:
    """
    Without using a for loop, replicate what a for loop does
    internally: use iter() to get an iterator from `items`, then
    repeatedly call next() on it inside a while loop, catching
    StopIteration to know when to stop.

    Return a list of all elements retrieved this way, in order
    (it should exactly match the original `items` list).
    """
    res = []
    iterator = iter(items)
    while True:
        try:
            res.append(next(iterator))
        except StopIteration:
            break
    return res
