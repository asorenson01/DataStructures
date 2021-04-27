class Bdaylocations:
    # set data structure
    def __init__(self):
        self.locations = {"home", "Red Robbin", "Iraq", "Afghanistan", "In a Helicopter"}

    def add_bday_locations(self, location1, location2, location3):
        self.locations.update({location1, location2, location3})
        print("<---------- ADDED 3 Locations------------>")

    def print_locations(self):
        for loc in self.locations:
            print(loc)
