#Define function, Check if number is prime.
def is_prime(n:int)->bool:
    """
    Check if number is prime.
    Parameters:
        n (int): number to check
    Returns:
        bool: True if prime, False if not.
    """
    for  i in range(2, n):
        if n % i == 0:
            return False
    return True