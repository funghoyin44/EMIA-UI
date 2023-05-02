from hwtime import *

class Homework:
    def __init__(self, course:str, homework:str, min_time:int, max_time:int, suggested_time:int, useless:bool, mean:int):
        self.course = course
        self.homework = homework
        self.suggested_time = int(suggested_time)
        self.min_time = min_time
        self.max_time = max_time
        homework_list.append(self)

    def get_course(self)->str:
        return self.course
    
    def get_homework_name(self)->str:
        return self.homework
    
    def get_suggested_time(self)->int:
        return self.suggested_time
    
    def get_min_time(self)->int:
        return self.min_time
    
    def get_max_time(self)->int:
        return self.max_time

class User:
    def __init__(self, username:str, password:str, first_name:str, last_name:str, cga:int):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.cga = cga
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
    
    def get_cga(self)->int:
        return self.cga
    
course_list = ["EMIA2020", "COMP1021", "PHYS3032"]
homework_list = []
user_list = []
skin_option_list = ["Teddy Bear"]

def initialize_data(user):
    
    PHYS3032_PS1 = Homework("PHYS3032", "PS1", 30, 301, 130, True, 100)
    PHYS3032_PS2 = Homework("PHYS3032", "PS2", 40, 461, 170, True, 300)
    PHYS3032_PS3 = Homework("PHYS3032", "PS3", 50, 270, 100, True, 400)
    PHYS3032_PS4 = Homework("PHYS3032", "PS4", 30, 230, 90, True, 131)
    PHYS3032_PS5 = Homework("PHYS3032", "PS5", 90, 500, 150, True, 214)
    PHYS3032_PS6 = Homework("PHYS3032", "PS6", 30, 510, 210, True, 147)
    PHYS3032_PS7 = Homework("PHYS3032", "PS7", 90, 350, 230, True, 234)
    PHYS3032_PS8 = Homework("PHYS3032", "PS8", 60, 210, 140, True, 217)
    
    EMIA2020_HW1 = Homework("EMIA2020", "HW1", *serachcourse_withoutgraph("emia2020", "hw1", user.get_cga()))
    EMIA2020_HW2 = Homework("EMIA2020", "HW2", *serachcourse_withoutgraph("emia2020", "hw2", user.get_cga()))
    COMP1021_PA1 = Homework("COMP1021", "PA1", *serachcourse_withoutgraph("comp1021", "pa1", user.get_cga()))
user0 = User("andrew", "123456", "Andrew", "Ho", 3.7)
user1 = User("mary3308", "qwer789", "Megumi", "Kato", 4.0)