# Finde the minimum number in an iterable object
def minimum(iterable):
    if len(iterable) == 0:
        return None

    if len(iterable) == 1:
        return iterable[0]

    # First number to compare
    MIN = iterable[0]

    # Keep updating the MIN variable with each number lower than MIN
    for value in iterable:
        if value < MIN:
            MIN = value

    return MIN


# Finde the maximum number in an iterable object
def maximum(iterable):
    if len(iterable) == 0:
        return None

    if len(iterable) == 1:
        return iterable[0]

    # First number to compare
    MAX = iterable[0]

    # Keep updating the MAX variable with each number greater than MAX
    for value in iterable:
        if value > MAX:
            MAX = value

    return MAX
