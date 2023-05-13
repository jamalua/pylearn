#without warlus

nums = []
num = input('Typa a number: ')
while num.isdigit():
    nums.append(int(num))
    num = input("Type a number: ")

print(nums)


#With Walrus
nums = []
while (num := input('Type a number: ')).isdigit():
    nums.append(num)

print(nums)