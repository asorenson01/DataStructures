import random

class Sweepstakes:
    def __init__(self):
        self.contestants = [
            {"firstname": "First",
             "lastname": "One"
             },
            {"firstname": "Second",
             "lastname": "Two"
            },
            {"firstname": "Third",
             "lastname": "Three"
             },
            {"firstname": "Fourth",
             "lastname": "Four"
             },
            {"firstname": "Fifth",
             "lastname": "Five"
            }
        ]
    def test_print(self):
        print(self.contestants[1]['firstname'])

    def sweepstatkes_signup(self, firstname, lastname):
        self.contestants.append(
            {"firstname": firstname,
             "lastname": lastname
            })


    def find_a_winner(self):
        x = random.randint(0,len(self.contestants)-1)
        print(f"{self.contestants[x]['firstname']} {self.contestants[x]['lastname']} has won the random sweepstateks")