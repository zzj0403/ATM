from interface import user, bank
from lib import common


def register():
    while True:
        if user_data['name']:
            print('您已经登入了')
            return
        name = input("请输入名字:>>").strip()
        passwrod = input('请输入密码:>>').strip()
        repeat_passwrod = input('重复输入密码:>>').strip()
        if passwrod == repeat_passwrod:
            flag, msg = user.register_interface(name, passwrod)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致')


user_data = {
    'name': None
}


def login():
    print('登入')
    if user_data['name']:
        print('您已经登入了')
        return
    while True:
        name = input("请输入名字:>>").strip()
        passwrod = input('请输入密码:>>').strip()
        flag, msg = user.loggin_interface(name, passwrod)
        if flag:
            user_data['name'] = name
            print(msg)
            break
        else:
            print(msg)
            break


@common.login_auth
def transfer():
    print('转账')
    while True:
        to_name = input('请输入你需要转的账号：>>').strip()
        money = input('请输入你转账的金额：>>').strip()
        if money.isdigit():
            money = int(money)
            flag, msg = bank.transfer_interface(user_data['name'], to_name, money)
            if flag:
                print(msg)
                break
            else:
                print(msg)


@common.login_auth
def check_balance():
    print('查询')
    balance = bank.check_balance_interface(user_data['name'])
    print(balance)


def shopping():
    print('购物')


def logout():
    user_data['name'] = None


func_dic = {
    '1': register,
    '2': login,
    '3': transfer,
    '4': check_balance,
    '5': shopping,
    '6': logout
}


def run():
    while True:
        msg = """
    1: 注册
    2: 登入
    3：转账
    4：查询余额
    5：购物
    6: 登出
    7：退出
    """
        print(msg)
        choice = input(">>").strip()
        if choice == '7':
            break
        if choice not in func_dic:
            print("输入的指令不存在")
            continue
        func_dic[choice]()
