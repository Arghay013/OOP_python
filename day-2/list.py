# list, array, collection is name( simple terms)

""" numbers = [17, 18, 26, 28, 387, 29, 6, 57, 28]
# index =  -9  -8  -7  -6  -5   -4  -3  -2  -1
print(numbers[3],numbers[-3]) """

# list(start : end) stert from forst index and end in before last index

""" print(numbers[2:6])
print(numbers[2:])
print(numbers[:7])
print(numbers[:]) # sortcut to coppy a list
print(numbers[::-1]) # sortcut to reverse a list
print(numbers[2:6:1])
print(numbers[2:6:2])
print(numbers[2:6:-1])
print(numbers[6:2:-1]) """
numbers = [12,25,34,55,78,90]
odd_nums = [num for num in numbers if num%2 == 0 if num%5 ==0]
print(odd_nums)
