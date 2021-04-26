class Monthsoftheyear:
    def __init__(self):
        self.moy = (
            "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
            "November", "December")

    def print_moy(self):
        for month in range(len(self.moy)):
            print(self.moy[month])

    def find_month(self, number):
        for month in range(len(self.moy)):
            if self.moy[month] == self.moy[number-1]:
                print (self.moy[month])