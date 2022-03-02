numbers = []

for i in range(5):
    user_input = eval(input('Enter a number: '))
    numbers.append(user_input)


print(numbers)


avg = sum(numbers)/len(numbers)
print('The average is: ', avg)

count = 0

for n in numbers:
    if n > avg:
        count += 1

print('The number above average is: ', count)
