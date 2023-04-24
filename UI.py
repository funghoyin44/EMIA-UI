import tkinter
import Database
root = tkinter.Tk()

current_row = 0
heading = tkinter.Label(root, text = "Homework Time", padx = 100, pady = 20, font = ("Arial", 30), bg = "yellow", fg = "blue")
heading.grid(row = 0, column = 0)

def search():
    code = search_bar.get().upper()
    for i in Database.course_list:
        if code == i:
            row_number = int(3)
            colour = ["yellow", "green"]
            current_colour = colour[0]
            for j in Database.homework_list:
                if j.get_course() == code:
                    result = tkinter.Label(root, text = str(j.get_homework_name()+"\t\t\t\t\t\t\t\t\t"+str(j.get_time())), bg = current_colour, width = 100)
                    result.grid(row = row_number, column = 0)
                    if current_colour == colour[0]:
                        current_colour = colour[1]
                    else:
                        current_colour = colour[0]
                    row_number = row_number + 1
            return None
    result = tkinter.Label(root, text = "No result", bg = "pink", width = 100)
    result.grid(row = 3, column = 0)
    

search_bar = tkinter.Entry(root, width = 100, borderwidth = 3)
search_bar.grid(row = 1, column = 0)
search_bar.insert(0, "Search Course Code")

search_button = tkinter.Button(root, text = "Search", command = search)
search_button.grid(row = 1, column = 1)
result_heading = tkinter.Label(root, text = "Homework                               \
                                                                                            Estimated Time(minutes)")
result_heading.grid(row = 2, column = 0)


root.mainloop()
