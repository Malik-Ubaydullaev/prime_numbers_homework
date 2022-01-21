from is_prime import is_prime

#Define function,Find list of prime numbers in a given range.
def prime_range(start:int, end:int)->list:
    """
    Find list of prime numbers in range.
    Parameters:
        start (int): start of range
        end (int): end of range
    Returns:
        list: list of prime numbers in range
    """
    lst = []
    k = 0
    for i in range (start, end+1):
        for j in range (start, i):
            if i % j == 0:
                k += 1
        if k == 0:
            lst.append(i)
        else:
            k = 0
    return lst
 

#Test function.