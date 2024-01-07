########################### List and dict ############################
test_list = []
my_dict = {} 
print(type(test_list))  # <class 'list'>
print(type(my_dict))  # <class 'dict'>

#____________ Adding __________________#
test_list.append([1, 2, 3])  # add a single item (a list)
test_list.extend([3, 1, 2])  # add multiple items one by one

#______________ Insert _______________#
test_list.insert(2, "Fk")  # insert "Fk" at index 2

#______________ Finding _______________#
index_of_3 = test_list.index(3)  # return the index of the first occurrence of 3
is_12_in_list = 12 in test_list  # check if 12 is in the list

#______________ Remove _______________#
removed_first_item = test_list.pop(0)  # remove the item at index 0 and return it
removed_last_item = test_list.pop()  # remove the last item and return it
test_list.remove("Fk")  # remove the first occurrence of "Fk" in the list

#____________ Sorting _________________#
test_list.sort()  # sort the list in-place
sorted_list = sorted(test_list)  # return a new sorted list without modifying the original

# Copying
new_list = list(test_list)  # create a new list with the same elements as test_list

# Slice
sliced_list = test_list[1:4]  # return values from index 1 to 3 (not including 4)

print(test_list)

############################## Tuple ###############################
#Immutable : cant modife 

test_tuple = (1, 2, 3, 'apple', 'banana', True)

print(type(test_tuple))  # <class 'tuple'>

#______________ Finding _______________#
index_of_3_in_tuple = test_tuple.index(3)  # return the index of the first occurrence of 3
is_12_in_tuple = 12 in test_tuple  # check if 12 is in the tuple

#____________ Sorting _________________#
sorted_tuple = sorted(test_tuple)  # return a new sorted tuple without modifying the original

# Copying
new_tuple = tuple(test_tuple)  # create a new tuple with the same elements as test_tuple

# Slice
sliced_tuple = test_tuple[1:4]  # return values from index 1 to 3 (not including 4)

print(test_tuple)
