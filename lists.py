# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    list_to_remove_elements = list_to_remove_elements.copy()
    if len(list_to_remove_elements) > 5:  
        list_to_remove_elements.pop(5)
    if len(list_to_remove_elements) > 4:  
        list_to_remove_elements.pop(4)
    if len(list_to_remove_elements) > 0:  
        list_to_remove_elements.pop(0)
    return list_to_remove_elements



def add_elements(list_to_add_elements):
    return ['Pink'] + list_to_add_elements + ['Yellow']


def is_empty(list_to_check):
    return len(list_to_check) == 0


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        return list_to_compare1[2] == list_to_compare2[2]
    return False


def list_of_lists(list_of_lists_to_modify):
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
       return list_to_compare1[2] == list_to_compare2[2]
    return False
    
    return [
        list_of_lists_to_modify[0][:2],  # Primera lista: primeros 2 elementos
        list_of_lists_to_modify[1][1:4] 
        if len(list_of_lists_to_modify[1]) >= 4 
        else list_of_lists_to_modify[1][1:],  # Segunda: elementos 1-3
        list_of_lists_to_modify[2][-2:]
    ]
