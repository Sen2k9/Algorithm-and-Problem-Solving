
def main():
    try:
        print('block-try start')
        print(hello)
        print('block-try end')
    except:
        print('block-except')

    else:
        print('block-else')

    finally:
        print('block-finally')


main()
