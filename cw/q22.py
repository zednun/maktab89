import re


class User:
    def __init__(self, fname, lname, user_name, password, phone, email):
        self.fname = fname
        self.lname = lname
        self.user_name = user_name
        self.__password = password
        self.phone = phone
        self.email = email
        self.user_dict = {}

    def register(self):
        self.validate()
        if self.user_name in self.user_dict:
            raise Exception("Account already exist!!")
        else:
            self.user_dict.update({self.user_name: [self.__password, self.fname, self.lname, self.phone, self.email]})

    def validate(self):
        assert re.findall("^(\+98)?9\d{9}$", self.phone), "invalid phone number!"
        assert re.findall("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", self.email), "invalid email!"
        assert re.findall("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$", self.__password), "invalid password!"

        return True

    def login(self, username, password):
        if username in self.user_dict:
            if self.__password == password:
                return "Successfully"
            else:
                return "Wrong password!"
        else:
            return "This user has not registered!"


class Main:
    try:
        obj = User("mahsa", "admin", "zednun", "Aassass12", "+989387218176", "mahsa.example@gmail.com")
        obj.register()
        print(obj.login("zednun", "Aassass12"))
        print(obj.login("zednun", "12345"))
        print(obj.login("zahra", "12345"))
    except AssertionError as msg:
        print(msg)

