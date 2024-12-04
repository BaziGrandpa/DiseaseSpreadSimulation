total_students = 500

department_number = 4

# the id of the array should be the student id from 0-total_students
# stored the state of the student from 0-1, 0 for healthy, 1 for severly infectious
student_infectious_state_list = [0] * total_students
#stored the department of the student, 0-3 
student_department_list = [0] * total_students

def init_students():
    for i in range(total_students):
        student_infectious_state_list[i] = 0
        if i == 50:
            student_infectious_state_list[i] = 1
        student_department_list[i] = i % department_number

def get_student_infectiou_state(student_id):
    return student_infectious_state_list[student_id]


def set_student_infectiou_state(student_id, state):
    if state > 1 or state<0:
        raise ValueError("The state should be between 0 and 1") 
    student_infectious_state_list[student_id] = state


# no setter, department is fixed
def get_student_department(student_id):
    return student_department_list[student_id]


