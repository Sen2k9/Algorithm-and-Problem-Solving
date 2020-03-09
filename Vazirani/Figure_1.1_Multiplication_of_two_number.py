
def multiply(x, y):
    if y == 0:
        return 0

    z = multiply(x, y // 2)
    if y % 2 == 0:
        print(2*z)
        return 2*z
    else:
        print(x+(2*z))
        return x+(2*z)


print(multiply(13, 11))
