
def main():
    s = "abc"
    hidden_name = iter(s)

    while True:
        try:
            c = next(hidden_name)
            print(c)
        except StopIteration:
            break


main()
