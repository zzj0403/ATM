from db import db_handler
import os, json
from conf import settings


def loggin_interface(name, passwrod):
    user_dic = db_handler.select(name)
    if user_dic:
        if passwrod == user_dic['passwrod'] and not user_dic['locked']:
            return True, '登入成功'
        else:
            return False, '密码错误'
    else:
        return False, '用户不存在'


def register_interface(name, passwrod, balance=15000):
    user_dic = db_handler.select(name)
    if user_dic:
        return False, '用户已存在'
    user_dic = {'name': name, 'passwrod': passwrod, 'balance': balance, 'credit': balance, 'locked': False,
                'banflow': [], 'shoppingcart': {}}
    db_handler.save(user_dic)
    return True, '注册成功'
