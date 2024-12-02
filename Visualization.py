import tkinter as tk
import Students
import math

builindgs_positions_range = {}
oval_objects_pool = []
oval_size = 6

def visualize_agent(canvas,buildings):
    if len(oval_objects_pool) <=0:
        for i in range(Students.total_students):
            oval_objects_pool.append(canvas.create_oval(0, 0, oval_size, oval_size, fill="green",state = "hidden"))

    #hide all the students
    # for oval in oval_objects_pool:
    #     canvas.itemconfig(oval,state = "hidden")

    oval_id = 0

    for building in buildings.values():
        building_position_range = get_buildings_position_range(building)
        start_position = [building_position_range[0]+oval_size,building_position_range[1]+oval_size]
        width = building_position_range[2]
        height = building_position_range[3]
        column_number =int( math.sqrt(building.maximum_number))
        id_in_list = 0
        for student_id in building.students:

            row = id_in_list // column_number
            column = id_in_list % column_number

            state = Students.get_student_infectiou_state(student_id)


            oval = oval_objects_pool[oval_id]

            # canvas = tk.Canvas(root, width=1200, height=900)
            # canvas.pack()
            start_position_x = start_position[0] + column*oval_size
            start_position_y = start_position[1] + row*oval_size
            canvas.coords(oval,start_position_x, start_position_y,start_position_x+ oval_size,start_position_y+ oval_size)
            canvas.itemconfig(oval, state="normal", fill="red" if state >= 0.5 else "green")
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
