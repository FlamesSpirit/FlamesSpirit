def even(num):
    reamainder = num % 2
    if reamainder == 0:
        even = True
    elif reamainder == 1:
        even = False
    return even


# 3 * x + 1
y = int(input("num: "))
x = y
print(even(x))
while x > 2:
    if x < 2:
        break
    while even(x) == True:
        if x < 2:
            break
        x = x // 2
        print(x)
    while even(x) == False:
        if x < 2:
            break
        x = 3 * x + 1
        print(x)
print(x)
