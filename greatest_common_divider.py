n1 = eval(input('Enter the first number: '))
n2 = eval(input('Enter the second number: '))

if n1 > n2:
    min_num = n1
else:
    min_num = n2

divider = 0

for i in range(2, min_num + 1):
    if(n1%i == 0 and n2%i == 0):
        divider =i

if (divider == 0):
    print()
    print('No common divider')
else:
    print()
    print('Greastest common divider: ', divider)
