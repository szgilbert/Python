#Linked-Lists are chains of data nodes where each node has a pointer to the next
#Allowing an adjustable number of data nodes as well as the ability to add and delete nodes

#I made a single direction linked list using nodes

#node class used to store data at each node in the link
class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def has_next(self):
        return self.next_node != None

class LinkedList(object):
    def __init__(self, head = None, tail = None):
        self.head = head

#the linked list has a head with no data. every time a new node is added it replaces the head and points at the old head
    def insert_head(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

#adds a node to the end of the linked list
    def insert_tail(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.has_next():
            current_node = current_node.get_next()
        current_node.set_next(new_node)

#makes the node prior to the data skip it in the list, removing it
    def delete_node(self, data):
        current_node = self.head
        previous_node = None
        found = False
        while current_node and found is False:
            if current_node.get_data() == data:
                found = True
            else:
                previous_node = current_node
                current_node = current_node.get_next
        if current_node is None:
            raise ValueError("Data not in list")
        if previous_node is None:
            self.head = current_node.get_next()
        else:
            previous_node.set_next(current_node.get_next())

#seaches each node for the value and returns the node that has it
    def search_list(self, data):
        current_node = self.head
        found = False
        while current_node and found is False:
            if current_node.get_data() == data:
                found = True
            else:
                current_node = current_node.get_next()
        if current_node is None:
            raise ValueError("Data not in list")
        else:
            return current_node





