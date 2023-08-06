from service.account import AccountMgr


def init(app):

    account = AccountMgr()

    @app.route("/login", methods=["GET", "POST", "PUT"])
    def login():
        return account.login()

    @app.route("/register", methods=["GET", "POST", "PUT"])
    def register():
        return account.register()

