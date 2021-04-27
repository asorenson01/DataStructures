from monthsoftheyear import Monthsoftheyear
from bdaylocations import Bdaylocations
from sweepstakes import Sweepstakes
from familymembers import Familymembers
from linkedlist import LinkedList
from binarytree import Binarytree

if __name__ == '__main__':
    test1 = Monthsoftheyear()
    test1.print_moy()
    test1.find_month(3)
    print("<-------------------bdaylocations---------------------------------------->")
    test2 = Bdaylocations()
    test2.print_locations()
    test2.add_bday_locations("Skippers", "Chuck E Cheese", "Strip Club")
    test2.print_locations()
    print("<-------------------Sweepstakes---------------------------------------->")
    test3 = Sweepstakes()
    test3.sweepstatkes_signup("sixth", "six")
    test3.find_a_winner()
    print("<-------------------Family Dictionary---------------------------------------->")
    test4 = Familymembers()
    test4.print_family()

    print("<-------------------LinkedList---------------------------------------->")

    linked_list = LinkedList()

    linked_list.append_node(55)
    linked_list.append_node(60)
    linked_list.append_node(65)
    linked_list.append_node(70)
    linked_list.append_node(75)
    linked_list.append_node(80)
    linked_list.add_to_beginning(30)
    linked_list.contains_node()
    print("<-------------------BinaryTree---------------------------------------->")



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

    print(tree.search(50))
    print(tree.search(100))
    print(tree.in_order(tree.root))
    print(tree.pre_order(tree.root))
