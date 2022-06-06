from string import digits
class User:
    def __init__(self,login,password):
        self.login=login
        self.password=password
        self.__secret='Нята'

    @property
    def secret(self):
        s=input('Введите пароль для доступа к секрету:')
        if s ==self.password:
            return self.__secret
        else:
            raise ValueError('Не верный пароль')
    @property
    def password(self):
        return self.password

    @staticmethod
    def number(password):
        for digit in digits:
            if digit in password:
                return True
            return False
    @password.setter
    def password(self,value):
        if not isinstance(value,str):
            raise TypeError ('Пароль должен быть строкой')
        if len(value)<4:
            raise ValueError ('Короткий пароль')
        if len(value)>12:
            raise ValueError ('слишком большой пароль')
        if not User.number(value):
            raise ValueError('Пароль должен содержать как минимум одну цифру')
        self.password=value

