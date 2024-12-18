import os
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import Students
import Buildings
import Settings
import SimulationController

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
                total_learning_fraction.append(fraction_learning_per_class/Settings.max_capacity)

    student_learning.append(np.sum(total_learning_fraction)/4) ## divide by 4 since we are looking at 4 departments







def record_simulation_data(time_step):
    global recorded_time_steps, recorded_sick_students, recorded_healthy_students
    healthy_students_count = 0
    sick_students_count = 0
    recovered_students_count = 0
    for i in range(Students.total_students):
        infectious_state = Students.get_student_infectiou_state(i)
        if infectious_state < 0.1:
            healthy_students_count += 1
        elif infectious_state == 2:
            recovered_students_count += 1
        else:
            sick_students_count += 1
        
    recorded_time_steps.append(time_step)
    recorded_sick_students.append(sick_students_count)
    recorded_healthy_students.append(healthy_students_count)
    recorded_recovered_students.append(recovered_students_count)
    

import os
import numpy as np
import matplotlib.pyplot as plt

def save_plot(infectious_rate, recovery_rate, social_dist, stay_home_thresh):
    # Define the folder path for saving the plot
    plot_folder = "Plot"

    # Ensure the folder exists
    if not os.path.exists(plot_folder):
        os.makedirs(plot_folder)

    final_file_name = (
        str(Students.total_students) + "students_" + str(infectious_rate) + "Irate_" + 
        str(recovery_rate) + "Rrate_" + str(stay_home_thresh) + "StayHome_" + 
        str(social_dist) + "social dist.png"
    )

    # Full path for the plot file
    plot_filename = os.path.join(plot_folder, final_file_name)

    fig, ax = plt.subplots(1, 2, figsize=(14, 6))

    # Plot recorded data
    ax[0].plot(
        np.array(recorded_time_steps) / Settings.time_step_per_day, 
        recorded_sick_students, 
        label="Sick Students", 
        color="red"
    )
    ax[0].plot(
        np.array(recorded_time_steps) / Settings.time_step_per_day, 
        recorded_healthy_students, 
        label="Healthy Students", 
        color="green"
    )
    ax[0].plot(
        np.array(recorded_time_steps) / Settings.time_step_per_day, 
        recorded_recovered_students, 
        label="Recovered Students", 
        color="blue"
    )

    ax[0].set_xlabel("Time Steps (Days)", fontsize=18)
    ax[0].set_ylabel("Number of Students", fontsize=18)
    ax[0].set_title("Simulation Results: Healthy vs Sick Students", fontsize=16)
    ax[0].legend(fontsize=14)
    ax[0].tick_params(axis='both', which='major', labelsize=18)
    ax[0].grid(True)

    # Non-zero-learning refers to the time when the students are at school.
    non_zero_learning = np.array([rate for rate in student_learning if rate >= 0.02])
    avg_learning = np.sum(non_zero_learning) / len(non_zero_learning)

    # Plotting on the second subplot
    ax[1].plot(
        np.array(recorded_time_steps) / Settings.time_step_per_day, 
        student_learning, 
        label="Percentage learning", 
        color="red"
    )
    ax[1].axhline(
        y=avg_learning, 
        color='blue', 
        linestyle='--', 
        label=f'Average learning in class: {avg_learning:.2f}'
    )
    ax[1].set_xlabel("Time Steps (Days)", fontsize=18)
    ax[1].set_ylabel("Learning (%)", fontsize=18)
    ax[1].set_title("Simulation Results: Learning over time as disease spread.", fontsize=16)
    ax[1].set_ylim([0, 1.1])
    ax[1].legend(fontsize=14)
    ax[1].tick_params(axis='both', which='major', labelsize=18)
    ax[1].grid(True)

    # Save the plot in the specified folder
    plt.savefig(plot_filename)

    # Optionally display the plot (can be omitted in a headless environment)
    # plt.show()

    print(f"Plot saved as {plot_filename}")

