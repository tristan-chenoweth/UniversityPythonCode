num = 1
sum_num = 0
while num < 10:
    sum_num = sum_num + num
    if sum_num > 20:
        break
    num = num + 2

print(sum_num, num)
