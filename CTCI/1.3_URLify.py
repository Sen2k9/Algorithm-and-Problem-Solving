def urflify(string, truelength):
    if len(string) == truelength:
        return string

    char = list(string)
    print(char)

    space = 0

    for i in range(truelength):
        if char[i] == " ":
            space += 1

    index = truelength + space * 2

    for i in range(truelength - 1, -1, -1):
        if char[i] == " ":
            char[index - 1] = "0"
            char[index - 2] = "2"
            char[index - 3] = "%"

            index = index - 3

        else:

            char[index - 1] = char[i]
            index -= 1

    return "".join(char)


print(urflify("Mr John Smith    ", 13))
