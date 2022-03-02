def main():
    user_input = input('Enter a date in the form of mm/dd/yyyy: ')

    ls = user_input.split('/')

    month = eval(ls[0].lstrip('0'))
    day = eval(ls[1].lstrip('0'))
    year = ls[2]

    month_names = ['January' , 'Feburary' , 'March' , 'April' , 'May' , 'June' , 'July' , 'August' , 'September' , 'October' , 'November' , 'December']
    max_day = [31,28,31,30,31,30,31,31,30,31,30,31]
    if (month < 1) or (month > 12):
        print ('Invalid Month.')
        return

    if day > max_day[month - 1]:
        print('Invalid Day.')
        return

    print(month_names[month - 1] , day , ',' , year)

main()
