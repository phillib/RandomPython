def remove_duplicates(my_list):
    """
    Removes duplicate items in a list
    """
    new_list = list()
    
    for each in my_list:
        if each not in new_list:
            new_list.append(each)
            
    return new_list
