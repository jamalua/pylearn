nums = [1, 2, 3]

i_nums = iter(nums)

print(i_nums)

# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))

while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration as SI:
        print(SI)
        break


"""

class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

nums = MyRange(1, 10)

for n in nums:
    print(n)

"""
