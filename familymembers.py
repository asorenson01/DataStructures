class Familymembers:
    def __init__(self):
        self.family = [
            {"Firstname": "Laura",
             "LastName": "Sorenson",
             "Relationship": "Wife"
             },
            {"Firstname": "Chase",
             "LastName": "Sorenson",
             "Relationship": "Son"
             },
            {"Firstname": "Robert",
             "LastName": "Sorenson",
             "Relationship": "Son"
             },
            {"Firstname": "Paige",
             "LastName": "Sorenson",
             "Relationship": "Daughter In Law"
             },
            {"Firstname": "Barbara",
             "Lastname": "Sorenson",
             "Relationship": "Mother"
             }
        ]

    def print_family(self):
        print(self.family)
