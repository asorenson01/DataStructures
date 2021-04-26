from monthsoftheyear import Monthsoftheyear
from bdaylocations import Bdaylocations
from sweepstakes import Sweepstakes

if __name__ == '__main__':
    test1 = Monthsoftheyear()
    # test.print_moy()
    # test1.find_month(3)
    test2 = Bdaylocations()
    # test2.print_locations()
    # test2.add_bday_locations("Skippers", "Chuck E Cheese", "Strip Club")
    # test2.print_locations()
    test3 = Sweepstakes()
    test3.test_print()
    test3.find_a_winner()

