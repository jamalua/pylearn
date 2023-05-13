my_list = [1, 2, 3]

# print statement will print the complete list
print(my_list)
# With using * the list will be unpacked
print(*my_list)


# If we want to have teh first value, last value and all hte values in between then we can have soemthign like that

my_list = [1, 2, 3, 4, 5, 6, 7]

a, *b, c = my_list
print(a)
print(b)
print(c)

# We can even merge items in two lists using this

my_fist_list = [1, 2, 3]
my_second_list = [4, 5, 6]

list_without_asterics = [my_fist_list, my_second_list]
print(list_without_asterics)

list_with_asterics = [*my_fist_list, *my_second_list]
print(list_with_asterics)
