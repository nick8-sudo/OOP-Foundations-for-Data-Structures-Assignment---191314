# Node and LinkedList implementation
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = new_node
    
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False


#a demonstration
if __name__ == "__main__":
    print("=== Linked List  ===")
    
    my_list = LinkedList()
    
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    
    print("List of contents:")
    my_list.display()
    
    print(f"Search for 20: {my_list.search(20)}")
    print(f"Search for 80: {my_list.search(80)}")
