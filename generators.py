def square_numbers(nums):
    for i in nums:
        yield i*i

l = [1,2,3,4,5,6,7]
x = square_numbers(l)


#print(x.__next__())
#print(x.__next__())

for n in x:
    print(n)

#using generators with list comprehension. The differnce is tht we have () rather than [].
lisComp = (p for p in range(10))

print(lisComp)
for a in lisComp:
    print(a)
