import tkinter as tk
import Tools
import Background
import Buildings
import SimulationController
import Students
import Visualization
import numpy as np
import Plot
import Settings








# Create the main window
root = tk.Tk()
root.title("Chalmers Campus Map")

running = False
def on_closing():
    global running
    print("User clicked the close button. Cleaning up resources...")
    root.destroy()  # This ensures the application closes properly
    running = False

# Bind the close button event to the handler function
root.protocol("WM_DELETE_WINDOW", on_closing)


# load the background image
background_image = Background.init(root)


# Create a canvas and add the image
canvas_width = 1200
canvas_height = 900
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()
canvas.create_image(0, 0, image=background_image, anchor="nw")


# Bind mouse click event to the canvas
def display_mouse_position(event):
    # Clear previous text (optional, to avoid overlapping text)
    canvas.delete("mouse_position")
    # Get the mouse position and display it on the canvas
    x, y = event.x, event.y
    canvas.create_text(x, y, text=f"({x}, {y})", fill="black", tag="mouse_position", anchor="nw")
canvas.bind("<Button-1>", display_mouse_position)  # Left mouse button click


# Draw all the buildings on the map
buildings = Buildings.init_all_buildings()
for building in buildings.values():
    points = building.position
    text_position = building.text_position
    # Draw the quadrilateral outline
    Tools.draw_quadrilateral_outline(canvas, points, line_color="blue", line_width=3)
    Tools.render_text(canvas, text_position[0], text_position[1], building.name, font=("Arial", 13), color="blue")

# initialize code
Students.init_students()

#create a building map
building_map=["Physics Building","Chemistry",
            "Machine",
            "Computer science and Engineering",
            "Cafeteria",
            "Library",
            "HB",
            "Home"]

# send them back home
for i in range(Students.total_students):
    buildings["Home"].enlist(i)

# the whole simulation
time_step = 0
max_time_step = 10000000
time_step_per_day = 720
visualization_step = 100
#initialize data arrays
running = True
while time_step < max_time_step and running:
    # simulation code
    SimulationController.simulation(time_step% time_step_per_day, buildings,building_map)

    # visualization code
    if time_step % visualization_step == 0:
        try:
            Plot.record_simulation_data(time_step+1)
            Plot.record_student_learning(buildings)

            Visualization.visualize_agent(canvas, buildings)
            # update the canvas
            root.update()
            # wait for a while
            #root.after(100)
        except:
            print("Visualization error")


    time_step += 1



Plot.save_plot(buildings["Home"].infection_rate,buildings["Home"].recovery_rate, Settings.public_distancing_precentage)
Plot.save_plot_fraction_learning(buildings["Home"].infection_rate,buildings["Home"].recovery_rate,Settings.public_distancing_precentage )
print("Simulation completed. Exiting...")
#root.mainloop()
