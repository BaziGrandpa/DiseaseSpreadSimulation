import Students

# all key timestep variables
START_OF_A_DAY = 0
END_OF_FIRST_CLASS = 100
END_OF_SECOND_CLASS = 200
END_OF_LUNCH = 300
END_OF_THIRD_CLASS = 400
END_OF_FOURTH_CLASS = 500
END_OF_A_DAY = 1000

def simulation(time_step_in_day):

    # at critical time steps, do something
    if time_step_in_day  == START_OF_A_DAY:
        # send all students to their respective buildings
        from_home_to_campus()
    elif time_step_in_day == END_OF_FIRST_CLASS:
        # maybe move them from one building to class room
        change_classroom()
    elif time_step_in_day == END_OF_SECOND_CLASS:
        # move them to lunch
        from_classroom_to_cafeteria()
    elif time_step_in_day == END_OF_LUNCH:
        # move them to class
        from_cafeteria_to_classroom()
    elif time_step_in_day == END_OF_THIRD_CLASS:
        # move them from one building to class room
        change_classroom()
    elif time_step_in_day == END_OF_FOURTH_CLASS:
        change_classroom()
    elif time_step_in_day == END_OF_A_DAY:
        # bed time, back home!!
        from_campus_to_home()
    else:
        simulate_disease_spread()
        
        
    return 
   
def from_home_to_campus():
    print("from home to campus")
    return

def from_campus_to_home():
    print("from campus to home")
    return

def change_classroom():
    print("change classroom")
    return

def from_classroom_to_cafeteria():
    print("from classroom to lunch")
    return

def from_cafeteria_to_classroom():
    print("from lunch to classroom")
    return

def simulate_disease_spread():
    # for each student, check if they are infectious
    # if they are, check if they are in the same building as other students
    # if they are, check if they are close to other students
    # if they are, infect
    return



