def arithmaticShift(x, count):

    for i in range(count):
        x = x >> i

    return x


def logicalShift(x, count):

    for i in range(count):
        x = x >> 1
