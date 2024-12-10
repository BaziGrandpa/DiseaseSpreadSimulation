#Global settings

number_of_students=400

max_capacity=100 #the maximum capacity of each building
max_capacity_caffeteria=400 # same as number of students.
public_distancing_precentage=1

building_capacity=max_capacity*public_distancing_precentage
rate_of_dissease_spread=0.001
recovery_rate=0.0003
incubation_rate=0.001
suseptible_again_probability=0.0001

stay_at_home_threshold=1.1

patient_zero_index=50

time_step_per_day = 720

max_time_step = 43200 # corresponds to 60 days. time_step_per_day * 60