# проверка prob2
previous = 1
next = 2
sum = 2

while next <= 4000000:
    if (previous + next) % 2 == 0:
        sum += (previous + next)
    tmp = previous
    previous = next
    next += tmp

print(sum)
