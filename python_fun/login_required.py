def login_required(func):
    def wrapper_check():
        print("verifying the login")
        func()
        print("verification finishes")

    return wrapper_check
