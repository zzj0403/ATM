from core import src


def login_auth(func):
    def warapper(*args, **kwargs):
        if not src.user_data['name']:
            src.login()
        else:
            return func(*args, **kwargs)
    return warapper
