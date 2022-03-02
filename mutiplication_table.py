for i in range(1,10):
    print(format(i, '4d'), end='')
    
print()

print('-'*4*9)

for i in range(1,10):
    for j in range(1,10):
        print(format(i*j, '4d'), end='')
    print()
