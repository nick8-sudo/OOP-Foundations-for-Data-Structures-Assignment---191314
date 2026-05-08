class Node:
    
    def __init__(self, data):
        
        self.data = data
        self.next = None


#creation and linking of 3 nodes
if __name__ == "__main__":
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    
    node1.next = node2
    node2.next = node3
    
    #traverse and print
    print("Traversing linked nodes:")
    current = node1
    while current is not None:
        print(current.data)
        current = current.next
