def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if (number <= 0):
        raise ValueError ("Classification is only possible for positive integers.")
    sum = 0
    for x in range(1, int(number / 2)+1):
        if (number % x == 0):
            sum = sum + x
    if (sum == number):
        return "perfect"
    elif (sum > number):
        return " abundant"
    else:
        return "deficient"
