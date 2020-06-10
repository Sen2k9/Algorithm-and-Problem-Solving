
def minimum(*args):

    ans = args[0]

    for each in args[1:]:
        if each < ans:
            ans = each

    return ans


def maximum(*args):
    ans = args[0]

    for each in args[1:]:
        if each > ans:
            ans = each

    return ans


print(minimum(10, 2, 5, 6))

print(maximum(10, 2, 6, 78))


print("typing {foo}".format(foo=2, more=3))
