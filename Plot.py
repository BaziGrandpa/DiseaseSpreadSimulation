import os
import matplotlib.pyplot as plt
import numpy as np
import Students
import Buildings

recorded_time_steps = []
recorded_sick_students = []
recorded_healthy_students = []
recorded_recovered_students = []

student_learning = []

def record_student_learning(buildings):
    global student_learning
    total_learning_fraction = [] ## append the number fraction of learning
    for building in buildings.values():
        if building.name != "Home" and building.name != "Cafeteria":
                ## keep track of how "active" students are in class. I.e a student with 70% sickness dont learn as much as a healthy one.
                fraction_learning = np.zeros(len(building.students))

                for i,student in enumerate(building.students): 
                    state = Students.get_student_infectiou_state(student)
                    ## interprete state 2 and 0 as the same in this scenario
                    if state == 2:
                        state = 0

                    frac_learning = 1-state # determines how much a student is learning. E.g 80% sick => 20% learning capacity
                    fraction_learning[i] = frac_learning

                fraction_learning_per_class = np.sum(fraction_learning)
                ## 
                total_learning_fraction.append(fraction_learning_per_class/building.maximum_number)

    student_learning.append(np.sum(total_learning_fraction)/4) ## divide by 4 since we are looking at 4 departments


def save_plot_fraction_learning(infectious_rate, recovery_rate):
    # Define the folder path for saving the plot
    plot_folder = "Plot"

    # Ensure the folder exists
    if not os.path.exists(plot_folder):
        os.makedirs(plot_folder)

    final_file_name = str(Students.total_students) + "students_" + str(infectious_rate) + "Irate_" + str(recovery_rate)  +  "Rrate "+ "_percent learning.png"

    # Full path for the plot file
    plot_filename = os.path.join(plot_folder, final_file_name)

    # Create a MATLAB-style plot
    plt.figure(figsize=(10, 6))

    # Plot recorded data
    plt.plot(recorded_time_steps, student_learning, label="Percentage learning", color="red")

    
    plt.xlabel("Time Steps")
    plt.ylabel("Fraction of learning")
    plt.title("Simulation Results: Learning over time as disease spread.")
    plt.legend()
    plt.grid(True)

    # Save the plot in the specified folder
    plt.savefig(plot_filename)

    # Optionally display the plot (can be omitted in a headless environment)
    # plt.show()

    print(f"Plot saved as {plot_filename}")



def record_simulation_data(time_step):
    global recorded_time_steps, recorded_sick_students, recorded_healthy_students
    healthy_students_count = 0
    sick_students_count = 0
    recovered_students_count = 0
    for i in range(Students.total_students):
        infectious_state = Students.get_student_infectiou_state(i)
        if infectious_state < 0.5:
            healthy_students_count += 1
        elif infectious_state == 2:
            recovered_students_count += 1
        else:
            sick_students_count += 1
        
    recorded_time_steps.append(time_step)
    recorded_sick_students.append(sick_students_count)
    recorded_healthy_students.append(healthy_students_count)
    recorded_recovered_students.append(recovered_students_count)
    

def save_plot(infectious_rate, recovery_rate):
    # Define the folder path for saving the plot
    plot_folder = "Plot"

    # Ensure the folder exists
    if not os.path.exists(plot_folder):
        os.makedirs(plot_folder)

    final_file_name = str(Students.total_students) + "students_" + str(infectious_rate) + "Irate_" + str(recovery_rate) + "Rrate.png"

    # Full path for the plot file
    plot_filename = os.path.join(plot_folder, final_file_name)

    # Create a MATLAB-style plot
    plt.figure(figsize=(10, 6))

    # Plot recorded data
    plt.plot(recorded_time_steps, recorded_sick_students, label="Sick Students", color="red")
    plt.plot(recorded_time_steps, recorded_healthy_students, label="Healthy Students", color="green")
    plt.plot(recorded_time_steps, recorded_recovered_students, label="Recovered Students", color="blue")
    
    plt.xlabel("Time Steps")
    plt.ylabel("Number of Students")
    plt.title("Simulation Results: Healthy vs Sick Students")
    plt.legend()
    plt.grid(True)

    # Save the plot in the specified folder
    plt.savefig(plot_filename)

    # Optionally display the plot (can be omitted in a headless environment)
    # plt.show()

    print(f"Plot saved as {plot_filename}")
