class Homework:
    def __init__(self, course:str, homework:str, time:int):
        self.course = course
        self.homework = homework
        self.time = time


    def get_course(self)->str:
        return self.course
    
    def get_homework_name(self)->str:
        return self.homework
    
    def get_time(self)->int:
        return self.time
    
course_list = []
homework_list = []

def initialize_data():
    PHYS3032_PS1 = Homework("PHYS3032", "PS1", 130)
    PHYS3032_PS2 = Homework("PHYS3032", "PS2", 170)
    PHYS3032_PS3 = Homework("PHYS3032", "PS3", 100)
    PHYS3032_PS4 = Homework("PHYS3032", "PS4", 90)
    PHYS3032_PS5 = Homework("PHYS3032", "PS5", 150)
    PHYS3032_PS6 = Homework("PHYS3032", "PS6", 210)
    PHYS3032_PS7 = Homework("PHYS3032", "PS7", 230)
    PHYS3032_PS8 = Homework("PHYS3032", "PS8", 140)
    homework_list.append(PHYS3032_PS1)
    homework_list.append(PHYS3032_PS2)
    homework_list.append(PHYS3032_PS3)
    homework_list.append(PHYS3032_PS4)
    homework_list.append(PHYS3032_PS5)
    homework_list.append(PHYS3032_PS6)
    homework_list.append(PHYS3032_PS7)
    homework_list.append(PHYS3032_PS8)
    course_list.append("PHYS3032")

initialize_data()