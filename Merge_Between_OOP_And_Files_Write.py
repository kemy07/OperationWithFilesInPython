class Student:
    def enter (self , name , id):
        self.name = name
        self.id = id
    def get_info(self):
        return "Name: " + self.name + " Id:" + str (self.id)

