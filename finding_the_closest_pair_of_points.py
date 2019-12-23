import random


def closest_pair(ax, ay):
    if len(ax) <= 3:
        return brute_force(ax)
    mid = len(ax) // 2
    Qx = ax[:mid]
    Rx = ax[mid:]
    #midpoint = ax[mid][0]

    Qy = []
    Ry = []
    for each in ay:
        if each in Qx:
            Qy.append(each)
        else:
            Ry.append(each)
    p1, p2, min1 = closest_pair(Qx, Qy)
    p3, p4, min2 = closest_pair(Rx, Ry)

    if min1 <= min2:
        return p1, p2, min1
    else:
        return p3, p4, min2


def brute_force(ax):
    l = len(ax)
    p1 = ax[0]
    p2 = ax[1]
    dis = dest(p1, p2)
    if l == 2:
        return p1, p2, dis
    else:
        for i in range(l):
            for j in range(i + 1, l):
                temp = dest(ax[i], ax[j])
                if temp < dis:
                    dis = temp
                    p1, p2 = ax[i], ax[j]
    return p1, p2, dis


def dest(p1, p2):
    import math
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


def closest_split_pair(ax, ay, dis, best_pair):
    midpoint = ax[len(ax) // 2][0]
    y_prime = [each for each in ay if each[0]
               <= (midpoint - dis) or each[0] >= (midpoint + dis)]

    l = len(y_prime)
    for i in range(l-1):
        for j in range(i+1, min(i + 7, l)):
            temp = dest(y_prime[i], y_prime[j])
            if temp < dis:
                dis = temp
                best_pair = (y_prime[i], y_prime[j])
    return best_pair[0], best_pair[1], dis


def test_case(length: int = 1000):
    # random.seed(10)
    lst1 = [random.randint(-10**9, 10**9) for i in range(length)]
    lst2 = [random.randint(-10**9, 10**9) for i in range(length)]
    return lst1, lst2


def main():
    x, y = test_case()
    #a = list(zip(x, y))
    a = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    ax = sorted(a, key=lambda x: x[0])
    ay = sorted(a, key=lambda x: x[1])
    p1, p2, dis = closest_pair(ax, ay)
    # presorting takes O(n), recursion takes O(nlogn), total = O(nlogn)
    best_pair = (p1, p2)

    p3, p4, dis2 = closest_split_pair(ax, ay, dis, best_pair)
    # this function takes O(n)

    print("Closest Pair of Points {}, {} and distance {}".format(p3, p4, dis2))

    """
    So, total complexity = sorting + closest_pair + closest_split_pair
                         = O(n) + O(nlogn) + O(n)
                         = O(nlogn)
    """


main()

"""
reference: https://medium.com/@andriylazorenko/closest-pair-of-points-in-python-79e2409fc0b2
"""
