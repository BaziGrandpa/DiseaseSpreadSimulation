import numpy as np
class Building:
    def __init__(self, name, position, text_position, maximum_number):
        """
        Initialize the Building class.

        :param name: Name of the building (string).
        :param position: Position of the building on the map (tuple of x, y coordinates).
        :param maximum_number: Maximum capacity of the building (integer).

        """
        self.name = name
        self.position = position
        self.maximum_number = maximum_number
        self.text_position = text_position
        self.students = []
        building_id_map = {
            "Physics Building": 0,
            "Chemistry": 1,
            "Machine": 2,
            "Computer science and Engineering": 3,
            "Cafeteria": 4,
            "Library": 5,
            "HB": 6,
            "Home": 7
        }
        
        # Assign ID based on the name
        self.id = building_id_map.get(name, -1)  # Default to -1 if name is not found


    def enlist(self, student):
        if(self.is_over_capacity(len(self.students))):
            print("Building full")
            return

        self.students.append(student)
    

    def remove_student(self, student):
        if(len(self.students) == 0):
            print("Building empty, cant remove student.")
            return
        elif(student not in self.students):
            print(f"student :{student} is not in the building")
            return

        self.students.remove(student)

    def spread_disease_cafeteria(self):
        return

    def __str__(self):
        """
        Return a string representation of the building.
        """
        return f"Building(name={self.name}, position={self.position}, maximum_number={self.maximum_number}, students={self.students})"


    def is_over_capacity(self, current_number):
        """
        Check if the building exceeds its maximum capacity.

        :param current_number: The current number of occupants in the building.
        :return: True if over capacity, False otherwise.
        """
        return current_number > self.maximum_number

def init_all_buildings():
    buildings = {}
    building1 = Building(name="Cafeteria", position=[(501, 401), (618, 404), (621, 451), (498, 467)],text_position=[563, 480], maximum_number=300)
    building2 = Building(name="Library", position=[(497, 197), (423, 179), (427, 138), (504, 145)], text_position=[473, 133], maximum_number=300)
    building3 = Building(name="Physics Building", position=[(355, 277), (478, 281), (478, 350), (353, 337)], text_position=[415, 360], maximum_number=300)
    building4=  Building(name="HB", position=[(590, 162), (594, 193), (674, 196), (669, 163)], text_position=[632, 143], maximum_number=300)
    building5=  Building(name="Chemistry", position=[(400, 260), (405, 170), (345, 180),(350, 265)], text_position=[373, 162], maximum_number=300)
    building6 = Building(name="Home", position=[(227, 384), (237, 447), (57, 473),(45, 418)], text_position=[165, 380], maximum_number=300)
    building7 = Building(name="Computer science and Engineering", position=[(728, 204), (789, 200), (795, 274),(728, 281)], text_position=[761, 290], maximum_number=300)
    building8 = Building(name="Machine", position=[(663, 204), (667, 296), (561, 295),(561, 204)], text_position=[591, 307], maximum_number=300)

    buildings["Cafeteria"] = building1
    buildings["Library"] = building2
    buildings["Physics Building"] = building3
    buildings["HB"] = building4
    buildings["Chemistry"] = building5
    buildings["Home"] = building6
    buildings["Computer science and Engineering"] = building7
    buildings["Machine"] = building8

    return buildings


## Example usage and test for ID ##
physics= Building(name="Physics Building", position=[(400, 260), (405, 170), (345, 180),(350, 265)], text_position=[373, 162], maximum_number=300)
print(physics.id)