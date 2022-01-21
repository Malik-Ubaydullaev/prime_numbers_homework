from is_prime import is_prime
#Define function, Find the number of prime numbers which are less than n.

def prime_number(n:int)->int:
    """
    Find the number of prime numbers which are less than n.
    Parameters:
        n (int): Given number
    Returns:
        int: Number of prime numbers
    """
    lst = []
    k = 0
    for i in range (2, n):
        for j in range (2, i):
            if i % j == 0:
                k += 1
        if k == 0:
            lst.append(i)
        else:
            k = 0
    return len(lst)
