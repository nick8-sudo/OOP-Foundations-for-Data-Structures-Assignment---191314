# OOP Foundations for Data Structures Assignment

## Part 2: Basic OOP Practice

For Part 2, I created a Node class with data and next.
data stores the value of the node, while next stores the link to the next node.
I then created 3 nodes manually and linked them together.
node1.next = node2
node2.next = node3
This created the linked list:
10 → 20 → 30
I used a while loop to traverse through the nodes and print each value until it reached None.


## Part 3: Simple Linked List

For Part 3, I created a LinkedList class to manage the nodes more easily.
`append(data)` adds a new node at the end of the list.
`display()` prints all the node values.
`search(data)` checks whether a value exists in the list.
I tested the program by adding values 10, 20, and 30, displaying them, and searching for values in the linked list.

# Part 4: Concept Questions

## 1. What is the role of a class in a linked list?

A class is used to define the structure and behavior of objects in a linked list.
For example, the `Node` class is used to create nodes that store data and links, while the `LinkedList` class manages operations such as adding, displaying, and searching nodes.
Classes help organize the code and make it easier to reuse and manage.


## 2. What is the difference between a node and a linked list?

A node is a single element in the structure that contains data and a reference to the next node.
A linked list is a collection of many connected nodes working together.
Without nodes, a linked list cannot exist because nodes are the building blocks of the list.


## 3. Why do we use None in next?

`None` is used to show that a node is not connected to another node.
When a node is first created, its `next` value is set to `None` because it does not yet point anywhere.
In a linked list, the last node always has `next = None` to indicate the end of the list.


## 4. How is a linked list different from a Python list?

A Python list stores elements in continuous memory locations and allows direct access using indexes like `list[0]`.
A linked list stores elements in separate nodes connected using links or pointers.
In a linked list, elements are accessed by moving from one node to the next.
Linked lists are more flexible when inserting or deleting data, while Python lists are faster for direct access.

## 5. Why is OOP useful for data structures?

OOP is useful because it organizes data and functions into classes and objects.
This makes data structures easier to understand, create, and maintain.
Using OOP also improves code reusability and reduces repetition since the same classes and methods can be used multiple times.
It also helps model real-world structures clearly and logically.
