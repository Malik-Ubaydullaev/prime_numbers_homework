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
    for i in range (start, end):
        if is_prime(i):
            lst.append(i)
    return lst
 

#Test function.