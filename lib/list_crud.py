def create_an_empty_list():
    return []
def create_a_list():
    # Using the literal constructor to create a list with four elements
    return [1, 'apple', True, 3.14]

def add_element_to_end_of_list(my_list, element):
    # Using the append() method to add an element to the end of the list
    my_list.append(element)
    return my_list

def add_element_to_start_of_list(my_list, element):
    # Using the insert() method to add an element to the start of the list
    my_list.insert(0, element)
    return my_list

def remove_element_from_end_of_list(my_list):
    # Using the pop() method to remove the last item from the list
    my_list.pop()
    return my_list

def remove_element_from_start_of_list(my_list):
    # Using the del keyword to remove the first item from the list
    del my_list[0]
    return my_list

def retrieve_first_element_from_list(my_list):
    # Using [] notation to return the value stored at the first index (index 0) of the list
    return my_list[0]

def retrieve_element_from_index(my_list, index):
    
    return my_list[index]

def retrieve_last_element_from_list(my_list):
    
    return my_list[-1]

my_list = create_a_list()
print("Initial List:", my_list)

my_list = add_element_to_end_of_list(my_list, 'banana')
print("List after adding element to the end:", my_list)

my_list = add_element_to_start_of_list(my_list, 'orange')
print("List after adding element to the start:", my_list)

my_list = remove_element_from_end_of_list(my_list)
print("List after removing element from the end:", my_list)

my_list = remove_element_from_start_of_list(my_list)
print("List after removing element from the start:", my_list)

first_element = retrieve_first_element_from_list(my_list)
print("First element of the list:", first_element)

element_at_index = retrieve_element_from_index(my_list, 1)
print("Element at index 1:", element_at_index)

last_element = retrieve_last_element_from_list(my_list)
print("Last element of the list:", last_element)
