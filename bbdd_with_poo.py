import pymysql


class Person:

    def __init__(self, username, mail, password=None):
        self.username = username
        self.mail = mail
        self.password = password
        self.exist = False
        self.connection = pymysql.connect(host='localhost',
                                          user='',  # User en phpmyadmin
                                          password='',  # Password en phpmyadmin
                                          database='dbpython',
                                          port=3306)

    def check(self):
        with self.connection.cursor() as cursor:
            sql = f'SELECT name, mail FROM users WHERE name="{self.username}" and mail="{self.mail}"'
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                self.exist = True
                return self.exist
            else:
                if self.password is not None:
                    return self.create_superuser()
                else:
                    return self.create_user()

    def create_user(self):
        with self.connection.cursor() as cursor:
            sql = f'INSERT INTO users (name, password, mail, rol) VALUES ("{self.username}", "", "{self.mail}", {False})'
            cursor.execute(sql)
            self.connection.commit()
            self.exist = True
            return "Se ha insertado el usuario con éxito."

    def create_superuser(self):
        with self.connection.cursor() as cursor:
            sql = f'INSERT INTO users (name, password, mail, rol) VALUES ("{self.username}", "{self.password}", ' \
                  f'"{self.mail}", {False})'
            cursor.execute(sql)
            self.connection.commit()
            self.exist = True
            return "Se ha insertado el super usuario con éxito."


def main():
    user1 = Person("user1", "user_1@gmail.com")
    print(user1.check())

    user2 = Person("Usuario2", "user_2@gmail.com", "123456")
    print(user2.check())

    user3 = Person("Usuario3", "user_3@gmail.com", "123456")
    print(user3.check())


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Something was wrong")
