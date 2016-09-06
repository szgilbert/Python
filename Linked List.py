
#single direction linked list using nodes

#node class used to store data at each node in the link
class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head

    #the linked list has a head with no data.
    # every time a new node is added it replaces the head and points at the old head
    def insert_head(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    #adds a node to the end of the linked list
    def insert_tail(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = new_node

    #makes the node prior to the data skip it in the list, removing it
    def delete_node(self, data):
        current_node = self.head
        previous_node = None
        found = False
        while current_node and found is False:
            if current_node.data is data:
                found = True
            else:
                previous_node = current_node
                current_node = current_node.next_node
        if current_node is None:
            return None
        if previous_node is None:
            self.head = current_node.next_node
        else:
            previous_node.next_node = current_node.next_node

    #seaches each node for the value and returns the node that has it
    def search_list(self, data):
        current_node = self.head
        found = False
        while current_node and found is False:
            if current_node.data is data:
                found = True
            else:
                current_node = current_node.next_node
        return current_node





