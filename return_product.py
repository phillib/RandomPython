def product(my_list):
    """
    Returns the product of a list of numbers
    """
    total = 1
    
    for each in my_list:
        total = total * each
        
    return total
