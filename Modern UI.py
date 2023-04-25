from Database import *
import tkinter
import customtkinter
from PIL import Image

#Initialization
root = customtkinter.CTk()
root.geometry("1280x720")
root.title("Homework Time Client (Beta)")
root.attributes("-alpha", 0.95)
customtkinter.set_appearance_mode("dark")
customIconFont = customtkinter.CTkFont(family= "Calibri", size = 40, weight = "bold")
customButtonFont = customtkinter.CTkFont(family= "Calibri", size = 30, weight = "bold")
customMenuButtonColour = "#8a8787"
customButtonColour = "#0d5ee0"
customTextFont = customtkinter.CTkFont(family= "Calibri", size = 30, weight = "bold")
customTextFontSmall = customtkinter.CTkFont(family= "Calibri", size = 20, weight = "bold")
result_list = []


#Logic
def search():
    global course_list
    global homework_list
    current_y = 125
    code = search_bar.get().upper()
    colour_list = ["#37ed61", "#e66581"]
    current_colour = colour_list[0]
    clear_result()
    for i in course_list:
        if i == code:
            for j in homework_list:
                if j.get_course() == code:
                    label = customtkinter.CTkLabel(result_frame, text = "{}\t\t\t\t\t\t{}".format(j.get_homework_name(), j.get_time()), font = customTextFont, fg_color = current_colour, width = 980, height = 50)
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

def clear_result():
    global result_list
    if len(result_list) == 0:
        return None
    for i in range(len(result_list)):
        result_list[i].destroy()
    result_list = []        

def buildSearchFrame():
    global result_frame
    global search_bar
    result_frame = customtkinter.CTkFrame(root, width = 980, height = 720, corner_radius = 0)
    result_frame.pack()
    result_frame.place(x = 300, y = 0)
    #icon_source = customtkinter.CTkImage(Image.open("Dummy Image.jpg"), size = (980, 720))
    #label = customtkinter.CTkLabel(result_frame, image = icon_source)
    #label.pack()
    search_bar = customtkinter.CTkEntry(result_frame, width = 700, height = 50, corner_radius = 10, font= customTextFont)
    search_bar.insert(0, "Search Course Code")
    search_bar.pack()
    search_bar.place(x = 40, y = 20)
    search_button = customtkinter.CTkButton(result_frame, width = 200, height = 50, fg_color= customButtonColour, text = "Search", font= customButtonFont, command = search)
    search_button.pack()
    search_button.place(x = 750, y = 20)
    notice_bar = customtkinter.CTkLabel(result_frame, text = "Homework\t\t\t\tEstimated Time(Minutes)", font = customTextFont, width = 980, height = 20, fg_color = "grey")
    notice_bar.pack()
    notice_bar.place(x = 0, y = 90)

def buildUploadFrame():
    global result_list
    global course_chosen
    clear_result()
    result_frame.destroy()
    upload_frame = customtkinter.CTkFrame(root, width = 980, height = 720, corner_radius = 0)
    upload_frame.pack()
    upload_frame.place(x = 300, y = 0)
    top_bar = customtkinter.CTkLabel(upload_frame, text = "Result Upload\t\t\t\t\t Welcome User", font = customTextFont, fg_color = "grey", width = 980, height = 60)
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
    course_choice = customtkinter.StringVar(upload_frame)
    course_choice = customtkinter.CTkOptionMenu(upload_frame, width = 200, height = 40, variable = course_chosen, values = course_list, command = update_homework_choice_list())
    course_choice.pack()
    course_choice.place(x = 250, y = 200)

    homework_tag = customtkinter.CTkLabel(upload_frame, text = "Homework:", font=customTextFontSmall, width = 100, height = 40)
    homework_tag.pack()
    homework_tag.place(x = 550, y = 200)
    homework_chosen = customtkinter.StringVar(upload_frame)
    homework_chosen.set(homework_choice_list[0])
    homework_choice = customtkinter.StringVar(upload_frame)
    homework_choice = customtkinter.CTkOptionMenu(upload_frame, width = 200, height = 40, variable = homework_chosen, values = homework_choice_list)
    homework_choice.pack()
    homework_choice.place(x = 660, y = 200)

    time_tag = customtkinter.CTkLabel(upload_frame, text = "Time(Minutes):", font=customTextFontSmall, width = 100, height = 40)
    time_tag.pack()
    time_tag.place(x = 160, y = 300)
    time_entry = customtkinter.CTkEntry(upload_frame, width = 200, height = 40)
    time_entry.pack()
    time_entry.place(x = 295, y = 300)


def update_homework_choice_list():
    global homework_choice_list
    course = course_chosen.get()
    homework_choice_list = []
    for i in homework_list:
        if(course == i.get_course()):
            homework_choice_list.append(i.get_homework_name())


#Left Menu
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

buildSearchFrame()



root.mainloop()