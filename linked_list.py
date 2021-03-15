from box_class import Box

# Linked List class contains a Node object 
class LinkedList: 
  
    # function to initialize head 
    def __init__(self): 
        self.head = None

    def insert_box(self, box): 

        if self.head == None:
            # add box to linked list
            self.head = box

        else:
            # make next of new Node as head 
            box.next = self.head 
                
            # move the head to point to new Node  
            self.head = box


    def print_list(self):
        temp = self.head

        while(temp):
            print(temp.height)
            temp = temp.next

    def traverse_list(self):
        pass