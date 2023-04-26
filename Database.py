class Homework:
    def __init__(self, course:str, homework:str, time:int):
        self.course = course
        self.homework = homework
        self.time = time
        homework_list.append(self)

    def get_course(self)->str:
        return self.course
    
    def get_homework_name(self)->str:
        return self.homework
    
    def get_time(self)->int:
        return self.time

class User:
    def __init__(self, username:str, password:str, first_name:str, last_name:str):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        user_list.append(self)

    def get_username(self)->str:
        return self.username
    
    def check_password(self, password)->bool:
        if password == self.password:
            return True
        return False

    def get_first_name(self)->str:
        return self.first_name
    
    def get_last_name(self)->str:
        return self.last_name
    
course_list = []
homework_list = []
user_list = []

def initialize_data():
    PHYS3032_PS1 = Homework("PHYS3032", "PS1", 130)
    PHYS3032_PS2 = Homework("PHYS3032", "PS2", 170)
    PHYS3032_PS3 = Homework("PHYS3032", "PS3", 100)
    PHYS3032_PS4 = Homework("PHYS3032", "PS4", 90)
    PHYS3032_PS5 = Homework("PHYS3032", "PS5", 150)
    PHYS3032_PS6 = Homework("PHYS3032", "PS6", 210)
    PHYS3032_PS7 = Homework("PHYS3032", "PS7", 230)
    PHYS3032_PS8 = Homework("PHYS3032", "PS8", 140)
    course_list.append("PHYS3032")
    EMIA_HW1 = Homework("EMIA2020", "HW1", 120)
    EMIA_HW2 = Homework("EMIA2020", "HW2", 130)
    EMIA_HW3 = Homework("EMIA2020", "HW3", 90)
    course_list.append("EMIA2020")
    user0 = User("andrew", "123456", "Andrew", "Ho")
    user1 = User("mary3308", "qwer789", "Megumi", "Kato")

initialize_data()
