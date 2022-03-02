def main():
    user_input = input('Enter a string: ').lower().strip()
    start = 0
    end = len(user_input) - 1

    while(start < end):
        if (user_input[start] != user_input[end]):
            print(user_input + ' is not a palindrome.')
            return
        start += 1

        while not(user_input[start].isalnum()):
            
            start += 1
        
        end -= 1

        while not(user_input[end].isalnum()):
            end -= 1

    print(user_input + ' is a palindrome.')

main()
