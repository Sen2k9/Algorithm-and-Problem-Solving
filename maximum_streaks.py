def getMaxStreaks(toss):
    maxH = 0
    maxT = 0
    tempH = 0
    tempT = 0
    for i in range(len(toss)):

        if toss[i] == "Heads":
            tempH += 1
            if tempH > maxH:
                maxH = tempH
            tempT = 0
        else:
            tempT += 1
            if tempT > maxT:
                maxT = tempT
            tempH = 0
    return maxH, maxT


toss = ["Heads", "Heads", "Heads", "Heads"]
print(getMaxStreaks(toss))
