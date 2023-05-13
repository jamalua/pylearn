
nums = [1,2,3,4,5,6,7,8,9,10]
'''
# my_list = [n*n for n in nums]
myList = [n for n in nums if n%2 == 0]
print(myList)

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
hereos = ['Batman', 'Superman', 'Spiderman', 'Wolverine' 'Deadpool']

# my_dict = {}
# for name, hero in zip(names, hereos):
#     my_dict[name] = hero

# print(my_dict)

my_dict = {name : hero for name,hero in zip(names,hereos)}

print(my_dict)

    
'''
lst = ['EVEN' if n%2==0 else 'ODD' for n in nums]

print(lst)
