from flask import request


class AccountMgr:
    def __init__(self):
        pass

    def login(self):
        # account = request.form.get("account")
        # keyword = request.form.get("keyword")
        account = request.args.get("account")
        password = request.args.get("password")
        print(account, password)
        return "bbbb"

    def register(self):
        # account = request.form.get("account")
        # keyword = request.form.get("keyword")
        account = request.args.get("account")
        password = request.args.get("password")
        print(account, password)

        return "bbbb"

