# 路由层，只做路由转发
from . import account


def init(app):
    account.init(app)