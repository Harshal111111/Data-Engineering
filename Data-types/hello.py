
# Sets can be created in two ways:
# 1. using  { } braces
# 2. using build in set() constructor

unique_set = {1, 2, 3, 3, 4, 4, 5}
new_set = set([1,4,3.4,2,5]) # Output: {1,2,3,4,5}
print(unique_set)  # Output: {1, 2, 3, 4, 5}

set_a = {1,2,3}
set_b = {3,4,5}
print(set_a | set_b) #union
print(set_a & set_b) #intersection
print(set_a - set_b) #difference
print(set_a ^ set_b) #symmetric difference
