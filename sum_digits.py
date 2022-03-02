def sum_digits(n):
    sum_d = 0
    while (n >= 10):
        remainder = n % 10
        n = n // 10
        sum_d += remainder
    sum_d += n
    return sum_d

print(sum_digits(235))
print(sum_digits(247))
print(sum_digits(59700897488445215199821598033953566993213144269487738431470012805))
