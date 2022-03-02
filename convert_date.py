def main():
    user_input = input('Enter a date in the form of mm/dd/yyyy: ')

    ls = user_input.split('/')

    month = eval(ls[0])
    day = ls[1]
    year = ls[2]

    if month == 1:
        month = 'January'

    elif month == 2:
        month = 'Feburary'
        
    elif month == 3:
        month = 'March'
        
    elif month == 4:
        month = 'April'
        
    elif month == 5:
        month = 'May'
        
    elif month == 6:
        month = 'June'
        
    elif month == 7:
        month = 'July'
        
    elif month == 8:
        month = 'August'
        
    elif month == 9:
        month = 'September'
        
    elif month == 10:
        month = 'October'
        
    elif month == 11:
        month = 'November'
        
    elif month == 12:
        month = 'December'

    else:
        month = 'Invalid Month'

main()
