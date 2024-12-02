import Buildings
import Students
import numpy as np


########## Example usage and tests ##########

def test_spread():
    physics = Buildings.Building(name="Physics Building", position=[(400, 260), (405, 170), (345, 180),(350, 265)], text_position=[373, 162], maximum_number=100)
    print(physics.id)

    ## Put 100 students in the physics building
    for i in range(100):
        physics.enlist(i)

    Students.init_students()
    ### Number of iterations to spread disease.
    for i in range(10):
        physics.spread_disease()

    ## 100 students => 10x10 grid
    print(np.array(Students.student_infectious_state_list).reshape(10, 10))
    ### Number of infected students (state == 1 is infected)
    print(np.sum(Students.student_infectious_state_list))


test_spread()