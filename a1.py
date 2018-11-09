def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    """

    if n % 50 != 0:
        return int((n / 50) + 1)
    else:
        return int(n / 50) 


def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """

    price_gain = 0
    price_loss = 0

    for price_change in price_changes:
        if price_change > 0:
            price_gain = price_gain + price_change
        if price_change < 0:    
            price_loss = price_loss + price_change             
    return (price_gain, price_loss)

def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """

    for i in range(k):
        temp = L[i]
        L[i] = L[len(L) - i - 1]
        L[len(L) - i - 1] = temp

if __name__ == '__main__':
    import doctest
    doctest.testmod()