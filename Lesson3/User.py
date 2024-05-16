class User:
    def __init__(self, first_name, last_name):
        self.name = first_name
        self.surname = last_name

    def firstName(self):
        print(self.name)

    def lastName(self):
        print(self.surname)

    def fullName(self):
        print(self.name, self.surname)
