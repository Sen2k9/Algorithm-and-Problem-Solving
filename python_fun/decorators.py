from login_required import login_required


@login_required
def verify_login():
    print("login has successfully verified")


verify_login()
