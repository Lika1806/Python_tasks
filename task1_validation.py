import re
import functools

def get_arg(name,index, args, kwargs):
    if name in kwargs:
        return kwargs[name]
    return args[index]


def valid_username(foo):
    reserved = ['admin', 'root']
    @functools.wraps(foo)
    def test(*args, **kwargs):
        name = get_arg('username',0, args, kwargs)
        if 5<=len(name)<=20 and name.isalnum() and name.lower not in reserved:
            return foo(*args, **kwargs)
        raise ValueError("Username is not valid")
    return test

def valid_email(foo):
    pattern = '^[\w\.-]+@[\w\.-]+\.+[\w]{2,4}$'
    @functools.wraps(foo)
    def test(*args, **kwargs):
        email = get_arg('email',1, args, kwargs)
        if bool(re.match(pattern,email)):
            return foo(*args, **kwargs)
        raise ValueError("Email in not valid")
    return test

def valid_phone(foo):
    pattern1 = '^\\+374[0-9]{8}$'
    pattern2 = '^0[0-9]{8}$'
    @functools.wraps(foo)
    def test(*args, **kwargs):
        phone = get_arg('phone',2, args, kwargs)
        if re.match(pattern1, phone) or re.match(pattern2,phone):
            return foo(*args, **kwargs)
        raise ValueError("Phone number is not valid")
    return test

def valid_password(foo):
    @functools.wraps(foo)
    def test(*args, **kwargs):
        password = get_arg('password', 3, args, kwargs)
        if len(password)>=8:
            flags = [str.islower, str.isupper, str.isdigit, lambda x: True if x in '&*^%$#!@' else False]
            for s in password:
                if not flags: break
                for i in range(len(flags)):
                    if flags[i](s):
                        flags.pop(i)
                        break
            if not flags:
                return foo(*args, **kwargs)
        raise ValueError("Password is not valid")
    return test

def valid_re_pass(foo):
    @functools.wraps(foo)
    def test(*args, **kwargs):
        if get_arg('password', 3, args, kwargs) == get_arg('re_pass', 4, args, kwargs):
            return foo(*args, **kwargs)
        raise ValueError ("Wrong repetition")
    return test

@valid_re_pass
@valid_password
@valid_phone
@valid_email
@valid_username
def info(username, email, phone, password, re_pass):
    print ('Information is valid')


try:
    info('Antony', 'name.lastname.123@gmail.com', password='AAaa**11', re_pass = 'AAaa**11', phone = '012345678')
except ValueError as e:
    print(e)

try:
    info('Aony', 'name.lastname.123@gmail.com', password='AAaa**11', re_pass = 'AAaa**11', phone = '012345678')
except ValueError as e:
    print(e)

try:
    info('Antony', 'name.la()stname.123@gmail.com', password='AAaa**11', re_pass = 'AAaa**11', phone = '012345678')
except ValueError as e:
    print(e)


try:
    info('Antony', 'name.lastname.123@gmail.com', password='AAaa11', re_pass = 'AAaa11', phone = '012345678')
except ValueError as e:
    print(e)

try:
    info('Antony', 'name.lastname.123@gmail.com', password='AAaa**11', re_pass = 'AAaa**11', phone = '12345678')
except ValueError as e:
    print(e)

try:
    info('Antony', 'name.lastname.123@gmail.com', password='AAaa**11', re_pass = 'AAaa***11', phone = '012345678')
except ValueError as e:
    print(e)


