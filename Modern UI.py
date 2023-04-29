from Database import *
import tkinter
import customtkinter
from PIL import Image
from hwtime import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os

#Option#
Developer_Mode = False
Bypass_Login = False




#There are no more option below this line#

#Initialization
root = customtkinter.CTk()
root.geometry("1280x720")
root.title("Homework Time Client (Beta)")
root.attributes("-alpha", 0.90)
customtkinter.set_appearance_mode("dark")
customIconFont = customtkinter.CTkFont(family= "Calibri", size = 40, weight = "bold")
customButtonFont = customtkinter.CTkFont(family= "Calibri", size = 30, weight = "bold")
customMenuButtonColour = "#8a8787"
customButtonColour = "#0d5ee0"
customTextFont = customtkinter.CTkFont(family= "Calibri", size = 30, weight = "bold")
customTextFontSmall = customtkinter.CTkFont(family= "Calibri", size = 20, weight = "bold")
result_list = []
homework_choice_list = []
login = User
success_login = False
performance_graph_generated = False

#Logic
def search(code = None):
    global course_list
    global homework_list
    current_y = 125
    if code == None:
        code = search_bar.get().upper()
    colour_list = ["#37ed61", "#e66581"]
    current_colour = colour_list[0]
    clear_result()
    for i in course_list:
        if i == code:
            for j in homework_list:
                if j.get_course() == code:
                    homework_name = str(j.get_homework_name())
                    label = customtkinter.CTkButton(result_frame, text = "{}\t\t{}\t\t{}\t\t{}".format(j.get_homework_name(), j.get_suggested_time(), j.get_min_time(), j.get_max_time()), font = customTextFont, fg_color = current_colour, width = 980, height = 50, command = lambda: display_homework_graph(j), corner_radius = 0)
                    result_list.append(label)
                    label.pack()
                    label.place(x = 0, y = current_y)
                    if(current_colour == colour_list[0]):
                        current_colour = colour_list[1]
                    else:
                        current_colour = colour_list[0]
                    current_y = current_y + 50
            return None
    label = customtkinter.CTkLabel(result_frame, text = "Not Found", fg_color = "#e80e3d", font = customTextFont, width = 980, height = 50)
    result_list.append(label)
    label.pack()
    label.place(x = 0, y = current_y)

def back_to_search(homework):
    homework_graph_frame.destroy()
    course = homework.get_course()
    buildSearchFrame(homework.get_course())
    search(course)
    

def display_homework_graph(homework):
    global homework_graph_frame
    serachcourse_withgraph(homework.get_course().lower(), homework.get_homework_name().lower(), login.get_cga())
    homework_graph_frame = customtkinter.CTkFrame(root, width = 980, height = 720)
    homework_graph_frame.pack()
    homework_graph_frame.place(x = 300, y = 0)
    title = customtkinter.CTkLabel(homework_graph_frame, text = "{} {}".format(homework.get_course(), homework.get_homework_name()), font = customTextFont, fg_color = "grey", width = 980, height = 60)
    title.pack()
    title.place(x = 0, y = 0)
    exit_button = customtkinter.CTkButton(homework_graph_frame, text = "< Back", fg_color = "grey", bg_color = "grey", font = customButtonFont, command = lambda : back_to_search(homework), width = 200, height  = 50)
    exit_button.pack()
    exit_button.place(x = 10, y = 7)
    homework_graph_source = customtkinter.CTkImage(Image.open("homework.png"), size = (800, 500))
    homework_graph = customtkinter.CTkLabel(homework_graph_frame, image = homework_graph_source)
    homework_graph.pack()
    homework_graph.place(x = 100, y = 150)
    detail = customtkinter.CTkLabel(homework_graph_frame, text = "Suggested Time: {}\tMin Time: {}\tMax Time: {}".format(homework.get_suggested_time(), homework.get_min_time(), homework.get_max_time()), font = customTextFont, width = 200, height = 40)
    detail.pack()
    detail.place(x = 100, y = 650)

def clear_result():
    global result_list
    if len(result_list) == 0:
        return None
    for i in range(len(result_list)):
        result_list[i].destroy()
    result_list = []        

   

def display_performace_graph():
    global performance_frame
    deadline_fighter = checkdeadlinefighter("a")
    graph_source = customtkinter.CTkImage(Image.open("temp.png"), size = (800, 500))
    label = customtkinter.CTkLabel(performance_frame, image = graph_source)
    label.pack()
    label.place(x = 100, y = 150)
    if deadline_fighter == True:
        fighter_notice = customtkinter.CTkLabel(performance_frame, text = "You are a deadline fighter!", font = customTextFont, text_color = "red", width = 150, height = 40)
    else:
        fighter_notice = customtkinter.CTkLabel(performance_frame, text = "You are not a deadline fighter!", font = customTextFont, text_color = "green", width = 150, height = 40)
    fighter_notice.pack()
    fighter_notice.place(x = 330, y = 650)

def try_login(bypass_user = None):
    global login
    global success_login
    global login_frame
    if bypass_user != None:
        initialize_data(bypass_user)
        login = bypass_user
        success_login = True
        buildSearchFrame()
        build_left_menu_frame()
        return None
    username = username_entry.get()
    password = password_entry.get()
    for i in user_list:
        if i.get_username() == username:
            if i.check_password(password):
                login = i
                success_login = True
                initialize_data(login)
                buildSearchFrame()
                build_left_menu_frame()
                login_frame.destroy()
                return None
    invalid_login_tag = customtkinter.CTkLabel(login_frame, text = "Invalid Username or Password!", font = customTextFontSmall, text_color = "red", width = 100, height = 30)
    invalid_login_tag.pack()
    invalid_login_tag.place(x = 530, y = 550)

def buildSearchFrame(input = None):
    global result_frame
    global search_bar
    result_frame = customtkinter.CTkFrame(root, width = 980, height = 720, corner_radius = 0)
    result_frame.pack()
    result_frame.place(x = 300, y = 0)
    #icon_source = customtkinter.CTkImage(Image.open("Dummy Image.jpg"), size = (980, 720))
    #label = customtkinter.CTkLabel(result_frame, image = icon_source)
    #label.pack()
    search_bar = customtkinter.CTkEntry(result_frame, width = 700, height = 50, corner_radius = 10, font= customTextFont)
    if input != None:
        search_bar.insert(0, str(input))
    else:
        search_bar.insert(0, "Search Course Code")
    search_bar.pack()
    search_bar.place(x = 40, y = 20)
    search_button = customtkinter.CTkButton(result_frame, width = 200, height = 50, fg_color= customButtonColour, text = "Search", font= customButtonFont, command = search)
    search_button.pack()
    search_button.place(x = 750, y = 20)
    notice_bar = customtkinter.CTkLabel(result_frame, text = "Homework\tSuggested\tMin\t\tMax", font = customTextFont, width = 980, height = 20, fg_color = "grey")
    notice_bar.pack()
    notice_bar.place(x = 0, y = 90)

def buildLoginFrame():
    if Bypass_Login:
        try_login(user_list[0])
        return None
    global username_entry
    global password_entry
    global login_frame
    login_frame = customtkinter.CTkFrame(root, width = 1280, height = 720)
    login_frame.pack()
    login_frame.place(x = 0, y = 0)
    login_tag = customtkinter.CTkLabel(login_frame, text = "Login", font = customTextFont, width = 200, height = 80)
    login_tag.pack()
    login_tag.place(x = 570, y = 150)
    username_tag = customtkinter.CTkLabel(login_frame, text = "Username:", font = customTextFontSmall, width = 150, height = 60)
    username_tag.pack()
    username_tag.place(x = 450, y = 250)
    username_entry = customtkinter.CTkEntry(login_frame, width = 200, height = 40)
    username_entry.pack()
    username_entry.place(x = 580, y = 260)
    password_tag = customtkinter.CTkLabel(login_frame, text = "Password:", font = customTextFontSmall, width = 150, height = 60)
    password_tag.pack()
    password_tag.place(x = 450, y = 350)
    password_entry = customtkinter.CTkEntry(login_frame, width = 200, height = 40)
    password_entry.pack()
    password_entry.place(x = 580, y = 360)
    login_button = customtkinter.CTkButton(login_frame, text = "Login", width = 200, height = 50, fg_color = customButtonColour, font = customButtonFont, command = try_login)
    login_button.pack()
    login_button.place(x = 580, y = 450)

def buildUploadFrame():
    global course_chosen
    global upload_frame
    global course_choice
    global time_entry
    global date_entry
    upload_frame = customtkinter.CTkFrame(root, width = 980, height = 720, corner_radius = 0)
    upload_frame.pack()
    upload_frame.place(x = 300, y = 0)

    top_bar = customtkinter.CTkLabel(upload_frame, text = "Result Upload\t\t\t\t Welcome {} {}".format(login.get_first_name(), login.get_last_name()), font = customTextFont, fg_color = "grey", width = 980, height = 60)
    top_bar.pack()
    top_bar.place(x = 0, y = 0)
    title = customtkinter.CTkLabel(upload_frame, text = "Homework Detail", font = customTextFont, width = 980, height = 60)
    title.pack()
    title.place(x = 0, y = 60)
    course_tag = customtkinter.CTkLabel(upload_frame, text = "Course:", font=customTextFontSmall, width = 100, height = 40)
    course_tag.pack()
    course_tag.place(x = 160, y = 200)
    course_chosen = customtkinter.StringVar(upload_frame)
    course_chosen.set(course_list[0])
    update_homework_choice_list(course_list[0])
    course_choice = customtkinter.CTkOptionMenu(upload_frame, width = 200, height = 40, variable = course_chosen, values = course_list, command = update_homework_choice_list)
    course_choice.pack()
    course_choice.place(x = 250, y = 200)

    homework_tag = customtkinter.CTkLabel(upload_frame, text = "Homework:", font=customTextFontSmall, width = 100, height = 40)
    homework_tag.pack()
    homework_tag.place(x = 550, y = 200)

    time_tag = customtkinter.CTkLabel(upload_frame, text = "Time(Minutes):", font=customTextFontSmall, width = 100, height = 40)
    time_tag.pack()
    time_tag.place(x = 160, y = 300)
    time_entry = customtkinter.CTkEntry(upload_frame, width = 200, height = 40)
    time_entry.pack()
    time_entry.place(x = 295, y = 300)

    date_tag = customtkinter.CTkLabel(upload_frame, text = "Date(YYYY-MM-DD):", font=customTextFontSmall, width = 100, height = 40)
    date_tag.pack()
    date_tag.place(x = 550, y = 300)
    date_entry = customtkinter.CTkEntry(upload_frame, width = 200, height = 40)
    date_entry.pack()
    date_entry.place(x = 730, y = 300)
    
    submit_button = customtkinter.CTkButton(upload_frame, text = "Submit", fg_color = customButtonColour, font = customButtonFont, width = 200, height = 50, corner_radius = 10, command = submit)
    submit_button.pack()
    submit_button.place(x = 390, y = 400)

def buildPerformanceFrame():
    global performance_frame
    performance_frame = customtkinter.CTkFrame(root, width = 980, height = 720)
    performance_frame.pack()
    performance_frame.place(x = 300, y = 0)
    title = customtkinter.CTkLabel(performance_frame, width = 980, height = 60, text = "Performance\t\t\t\t\t\t      ", font = customTextFont, fg_color = "grey")
    title.pack()
    title.place(x = 0, y = 0)
    display_performace_graph()

def update_homework_choice_list(course_chosen):
    global homework_choice_list
    global homework_chosen
    course = course_chosen
    for i in range(len(homework_choice_list)):
        homework_choice_list.remove(homework_choice_list[0])
    for i in homework_list:
        if(course == i.get_course()):
            homework_choice_list.append(i.get_homework_name())
    homework_chosen = customtkinter.StringVar(upload_frame)
    homework_chosen.set(homework_choice_list[0])
    homework_choice = customtkinter.StringVar(upload_frame)
    homework_choice = customtkinter.CTkOptionMenu(upload_frame, width = 200, height = 40, variable = homework_chosen, values = homework_choice_list)
    homework_choice.pack()
    homework_choice.place(x = 660, y = 200)
    

def submit():
        if(uploaddata(course_choice.get(), homework_chosen.get(), time_entry.get(), "a", login.get_cga(), date_entry.get()) == True):
            submitted = customtkinter.CTkLabel(upload_frame, text = "Submitted! Thank You!", font = customTextFontSmall, text_color = "green", width = 100, height = 30)
            submitted.pack()
            submitted.place(x = 390, y = 500)
        else:
            submitted = customtkinter.CTkLabel(upload_frame, text = "Submission Fail!", font = customTextFontSmall, text_color = "red", width = 100, height = 30)
            submitted.pack()
            submitted.place(x = 390, y = 500)

def reset_database():
    os.system("xcopy .\Bin\hwtime.csv hwtime.csv /Y")

#Left Menu
def build_left_menu_frame():
    left_menu_frame = customtkinter.CTkFrame(root, width = 300, height = 720, corner_radius = 0, fg_color= "grey2")
    left_menu_frame.pack()
    left_menu_frame.place(x = 0, y = 0)
    icon = customtkinter.CTkLabel(left_menu_frame, text = "Homework Time", font = customIconFont)
    icon.pack()
    icon.place(x = 13, y = 30)

    search_option = customtkinter.CTkButton(left_menu_frame, text = "Search", \
                                            font = customButtonFont, fg_color = customButtonColour, corner_radius = 0, width = 300, height = 70, command = buildSearchFrame)
    search_option.pack()
    search_option.place(x = 0, y = 90)
    report_option = customtkinter.CTkButton(left_menu_frame, text = "Upload", \
                                            font = customButtonFont, fg_color = customButtonColour, corner_radius = 0, width = 300, height = 70, command = buildUploadFrame)
    report_option.pack()
    report_option.place(x = 0, y = 160)
    performance_option = customtkinter.CTkButton(left_menu_frame, text = "Performance", \
                                            font = customButtonFont, fg_color = customButtonColour, corner_radius = 0, width = 300, height = 70, command = buildPerformanceFrame)
    performance_option.pack()
    performance_option.place(x = 0, y = 230)

    if Developer_Mode == True:
        reset_database_button = customtkinter.CTkButton(left_menu_frame, text = "Reset Database", width = 300, height = 30, fg_color = "red", font = customButtonFont, corner_radius = 0, command = reset_database)
        reset_database_button.pack()
        reset_database_button.place(x = 0, y = 640)
        developer_mode_label = customtkinter.CTkLabel(left_menu_frame, text = "Developer Mode", width = 300, height = 20, font = customTextFont)
        developer_mode_label.pack()
        developer_mode_label.place(x = 0, y = 680)

buildLoginFrame()



root.mainloop()
