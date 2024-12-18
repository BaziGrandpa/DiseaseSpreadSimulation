import tkinter as tk
import Students
import math
from tkinter import messagebox
import Settings
builindgs_positions_range = {}
oval_objects_pool = []
oval_size = 4
hint_show = False

def visualize_agent(canvas,buildings):
    global hint_show
    if len(oval_objects_pool) <=0:
        for i in range(Students.total_students):
            oval_objects_pool.append(canvas.create_oval(0, 0, oval_size, oval_size, fill="green",state = "hidden"))

    #hide all the students
    # for oval in oval_objects_pool:
    #     canvas.itemconfig(oval,state = "hidden")
    total_alive_students = 0
    for building in buildings.values():
        total_alive_students += len(building.students)
    if total_alive_students >Students.total_students and not hint_show:
        messagebox.showinfo("Hint", f"Current students number:{total_alive_students} \n in all buildings is more than total students. ")
        hint_show = True

    adjust_agent_size(total_alive_students)

    oval_id = 0

    for building in buildings.values():
        #building_position_range = get_buildings_position_range(building)
        #start_position = [building_position_range[0]+oval_size,building_position_range[1]+oval_size]
        building_position_range = get_building_position_dynamically(building)
        start_position = building_position_range
        column_number =int( math.sqrt(building.maximum_number))
        id_in_list = 0
        for student_id in building.students:

            row = id_in_list // column_number
            column = id_in_list % column_number

            state = Students.get_student_infectiou_state(student_id)

            try:
                oval = oval_objects_pool[oval_id]
            except:
                print("Error: oval_id:",oval_id)

            # canvas = tk.Canvas(root, width=1200, height=900)
            # canvas.pack()
            start_position_x = start_position[0] + column*oval_size
            start_position_y = start_position[1] + row*oval_size
            canvas.coords(oval,start_position_x, start_position_y,start_position_x+ oval_size,start_position_y+ oval_size)
            if state ==2:
                canvas.itemconfig(oval, state="normal", fill="blue")

            elif state >Settings.stay_at_home_threshold and state < 2:
                canvas.itemconfig(oval, state="normal", fill="red" if (state > Settings.stay_at_home_threshold and state < 2) else "green")
            else:
                canvas.itemconfig(oval, state="normal", fill="yellow" if (state > 0 and state <=Settings.stay_at_home_threshold) else "green")
            id_in_list += 1
            oval_id += 1


    return

#get the top left and bottom right position of the building
def get_buildings_position_range(building):
    if building.name in builindgs_positions_range:
        return builindgs_positions_range[building.name]

    points = building.position        
    x = [point[0] for point in points]
    y = [point[1] for point in points]

    center_x = sum(x) / len(x)
    center_y = sum(y) / len(y)
    width = max(x) - min(x)
    height = max(y) - min(y)
    startx = center_x - width/4
    starty = center_y - height/4

    builindgs_positions_range[building.name] = [startx,starty,width,height]
    return builindgs_positions_range[building.name]

def get_building_position_dynamically(building):
    points = building.position        
    x = [point[0] for point in points]
    y = [point[1] for point in points]

    center_x = sum(x) / len(x)
    center_y = sum(y) / len(y)

    student_number = len(building.students)

    column_number =int( math.sqrt(building.maximum_number))

    row_number = student_number // column_number

    width = column_number * oval_size
    height = row_number * oval_size

    startx = center_x - width/2
    starty = center_y - height/2
    return [startx,starty]




def adjust_agent_size(total_students):
    global oval_size
    if total_students < 400:
        oval_size = 6
    elif total_students < 1000:
        oval_size = 5
    elif total_students < 5000:
        oval_size = 4
    elif total_students < 8000:
        oval_size = 3
    else:
        oval_size = 2

    return
