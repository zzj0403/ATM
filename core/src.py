from interface import user
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

@common.login_auth
def check_balance():
    print('查询')



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
