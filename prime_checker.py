def is_prime(n):
    """
    Checks to see if a number is prime
    """
    if n == 0 or n == 1:
        return False # Remember, a prime number cannot be 1 or 0.
        
    if n < 0:
        return False # A prime number must be a positive number.
        
    for i in range(2, n):
        if n % i == 0:
            return False # If the number is divisible by anything other than 1 or itself, it is NOT prime.
            
    return True # If your number passes the above condition test, it is prime.
    
