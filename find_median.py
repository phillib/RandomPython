def median(my_list):
    """
    Finds the median of a list of numbers
    """
    
    my_list = sorted(my_list) # First, sort the list
    
    list_length = len(my_list) # Find the length of the list
    
    if list_length == 1: # If the list only has one element, the median is the one element
        return my_list[0]
    
    if list_length % 2 == 0: # If list has an even number of items, take the average of the 2 middle items as median
        high_mid = list_length // 2
        low_mid = high_mid - 1
        average = (my_list[high_mid] + my_list[low_mid]) / 2.0
        return average
        
        
    else: # If the number of items in the list is odd, the middle number is the median
        mid_ref = list_length // 2
        return my_list[mid_ref]
    
#print median([1, 7, 9, 14, 32, 2, 3])
#median output in this case equals 7
