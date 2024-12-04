import Students
import Buildings
import numpy as np

# all key timestep variables
START_OF_A_DAY = 100
END_OF_FIRST_CLASS = 200
END_OF_SECOND_CLASS = 300
END_OF_LUNCH = 400
END_OF_THIRD_CLASS = 500
END_OF_FOURTH_CLASS = 600
END_OF_A_DAY = 700

def simulation(time_step_in_day,buildings,building_map):
    
    # at critical time steps, do something
    if time_step_in_day  == START_OF_A_DAY:
        # send all students to their respective buildings
        from_home_to_campus(buildings,building_map)
        # print('people in chemistry' ,buildings["Chemistry"].students)
    elif time_step_in_day == END_OF_FIRST_CLASS:
        # maybe move them from one building to class room
        change_classroom()
    elif time_step_in_day == END_OF_SECOND_CLASS:
        # move them to lunch
        
        from_classroom_to_cafeteria(buildings,building_map)

    elif time_step_in_day == END_OF_LUNCH:
        # move them to class
        
        from_cafeteria_to_classroom(buildings,building_map)
    elif time_step_in_day == END_OF_THIRD_CLASS:
        # move them from one building to class room
        change_classroom()
    elif time_step_in_day == END_OF_FOURTH_CLASS:
        change_classroom()
    elif time_step_in_day == END_OF_A_DAY:
        # bed time, back home!!
        
        from_campus_to_home(buildings,building_map)
        
    simulate_disease_spread(buildings)
    # return 
    # for i in range(7):
    #     # print('number of students in',building_map[i],'is:',len(buildings[building_map[i]].students))
def from_home_to_campus(buildings,building_map):
    students_at_home= buildings["Home"].students.copy()
    max_sickness_level=0.5 ## should be general
    
    for i in students_at_home:
        
        healthy_enough_for_school=max_sickness_level<Students.student_infectious_state_list[i]
        
        departement=building_map[Students.student_department_list[i]]

        current_number_occupants=len(buildings[departement].students)
        
        if not(buildings[departement].is_over_capacity(current_number_occupants)) and healthy_enough_for_school:

            
            buildings["Home"].remove_student(i)
            buildings[departement].enlist(i)


    # print("from home to campus")
    return buildings

def from_campus_to_home(buildings,building_map):
    #remove students from campus
    print('currently home',len(buildings[building_map[7]].students))
    

    for i in range(len(building_map)-1):
        students_in_building=buildings[building_map[i]].students.copy()
        
        
        for j in students_in_building:
            buildings[building_map[i]].remove_student(j)
            buildings["Home"].enlist(j) #send them home
        print('left in building',len(buildings[building_map[i]].students))
        
        
    print('home from campus',len(buildings["Home"].students))

    # print("from campus to home")
    return buildings

def change_classroom():
    # print("change classroom")
    return

def from_classroom_to_cafeteria(buildings,building_map):

    number_of_students=Students.total_students
    caffeteria_capacity=min(buildings["Cafeteria"].maximum_number,number_of_students)
    
    

    # random_students=np.random.randint(number_of_students,size=caffeteria_capacity)
    random_students=np.random.choice(range(number_of_students), caffeteria_capacity, replace=False)
    
    for i in random_students:
        
        departement=building_map[Students.student_department_list[i]]

        buildings[departement].remove_student(i)

        buildings["Cafeteria"].enlist(i) #send them to Lunch

    
    # print("from classroom to lunch")
    return buildings

def from_cafeteria_to_classroom(buildings,building_map):
    students_in_cafeteria=buildings["Cafeteria"].students.copy()
    # print("students in cafeteria",len(students_in_cafeteria))
    for i in students_in_cafeteria:
        departement=building_map[Students.student_department_list[i]]
        buildings["Cafeteria"].remove_student(i)
        buildings[departement].enlist(i) #send them home
    
    # print("from lunch to classroom")
    # print("students in cafeteria",len(buildings["Cafeteria"].students))
    return

# @param buildings: a dictionary of buildings
def simulate_disease_spread(buildings):

    # for each student, check if they are infectious
    # if they are, check if they are in the same building as other students
    # if they are, check if they are close to other students
    # if they are, infect
    # this would be excecuted at every time step
    # Draw all the buildings on the map
    for building in buildings.values():
        if building.name != "Home":
            building.spread_disease()
        

    return



