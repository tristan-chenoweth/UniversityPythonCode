user_input = eval(input('Enter a positive integer: '))

if user_input % 5 == 0:
    if user_input % 2 == 0:
        print('HiFive')
        print('HiEven')
    else:        
        if user_input % 2 == 0:
            if user_input % 5 == 0:
                print('HiFive')
                print('HiEven')
            else:
                if  user_input % 5 == 0:
                    print('HiFive')
        
                if user_input % 2 == 0:
                    print('HiEven')
