from is_prime import is_prime
#Define function, Find the all prime numbers which are less than n.
def prime_list(n:int)->list:
    """
    Find the all prime numbers which are less than n.
    Parameters:
        n (int): Given number
    Returns:
        list: List of prime numbers
    """
    lst = []
    k = 0
    for i in range (2, n+1):
        for j in range (2, i):
            if i % j == 0:
                k += 1
        if k == 0:
            lst.append(i)
        else:
            k = 0
    return lst

