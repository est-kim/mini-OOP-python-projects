from linked_list import LinkedList


my_linked_list = LinkedList()

my_linked_list.insert_node(9)
my_linked_list.insert_node(3)
my_linked_list.insert_node(6)

# 1st: 9
# 2nd: 3 -> 9
# 3rd: 3 -> 6 -> 9

print(my_linked_list.find_node(6))
