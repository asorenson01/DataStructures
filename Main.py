from monthsoftheyear import Monthsoftheyear
from bdaylocations import Bdaylocations
from sweepstakes import Sweepstakes
from familymembers import Familymembers
from linkedlist import LinkedList
from binarytree import Binarytree

if __name__ == '__main__':
    # test1 = Monthsoftheyear()
    # test.print_moy()
    # test1.find_month(3)
    # test2 = Bdaylocations()
    # test2.print_locations()
    # test2.add_bday_locations("Skippers", "Chuck E Cheese", "Strip Club")
    # test2.print_locations()
    # test3 = Sweepstakes()
    # test3.sweepstatkes_signup("sixth", "six")
    # test3.find_a_winner()
    # test4 = Familymembers()
    # test4.print_family()

    # linked_list = LinkedList()
    #
    # linked_list.append_node(55)
    # linked_list.append_node(60)
    # linked_list.append_node(65)
    # linked_list.append_node(70)
    # linked_list.append_node(75)
    # linked_list.append_node(80)
    # linked_list.add_to_beginning(30)
    # linked_list.contains_node()
    # print("<-------------------------------Hello World--------------------------------------------->")
    # print(linked_list.head.next.next.data)

    tree = Binarytree()
    tree.add_to_tree(50)
    tree.add_to_tree(40)
    tree.add_to_tree(60)
    tree.add_to_tree(30)
    tree.add_to_tree(70)
    tree.add_to_tree(20)
    tree.add_to_tree(80)
    tree.add_to_tree(10)
    tree.add_to_tree(90)

    print(tree.search(100))
    print(tree.in_order(tree.root))
    print(tree.pre_order(tree.root))
