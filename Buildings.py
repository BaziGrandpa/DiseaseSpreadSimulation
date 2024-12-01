class Building:
    def __init__(self, name, position,text_position, maximum_number):
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

    def __str__(self):
        """
        Return a string representation of the building.
        """
        return f"Building(name={self.name}, position={self.position}, maximum_number={self.maximum_number})"

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

    buildings["Cafeteria"] = building1
    buildings["Library"] = building2
    buildings["Physics Building"] = building3
    buildings["HB"] = building4

    return buildings
