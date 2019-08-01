from db import db_handler


def check_balance_interface(name):
    user_dic = db_handler.select(name)
    return user_dic['balance']


def transfer_interface(from_name, to_name, balance):
    if from_name == to_name:
        return False, '不能给自己转钱'
    to_dic = db_handler.select(to_name)
    if to_dic:
        from_dic = db_handler.select(from_name)
        if from_dic['balance'] >= balance:
            to_dic['balance'] += balance
            from_dic['balance'] -= balance
            db_handler.save(from_dic)
            db_handler.save(to_dic)
            return True, '转账成功'
        else:
            return False, '您的余额不够'
    else:
        return False, '您要转账人用户不存在'


def repay_interface(name, money):
    user_dic = db_handler.select(name)
    user_dic['balance'] += money
    db_handler.save(user_dic)
    return True, '转账成功'
