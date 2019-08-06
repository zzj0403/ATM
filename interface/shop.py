from db import db_handler


def sheck_shop_interface(name):
    user_dic = db_handler.select(name)
    return user_dic['shoppingcart']