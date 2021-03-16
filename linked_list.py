
# Linked List class contains a Node object 
class LinkedList: 
  
    # function to initialize head 
    def __init__(self): 
        self.head = None
        self.size = 0

    def insert_box(self, box): 
        # if first box in list
        if self.head == None:

            self.head = box

            # one box in list
            self.size = 1

        else:

            # make next of new Node as head 
            box.next = self.head 
                
            # move the head to point to new Node  
            self.head = box

            # increase size of list by one
            self.size += 1

    def remove_box(self, box):
        temp = self.head

        # if head is selected
        if temp is not None:

            # disconnect then deallocate 
            self.head = temp.next
            temp = None

            self.size -= 1
            
        else:
            while(temp is not None):
                if temp == box:
                    break

                # disconnect node
                prev = temp
                temp = temp.next 

            # if selection isn't in list
            if temp == None:
                return

            # deallocate node
            temp = None

            self.size -= 1


    def print_list(self):

        # one way to traverse linked list
        temp = self.head
        
        while temp.next is not None:
            print(temp.height)
            temp = temp.next
        
        # last box in list
        print(temp.height)


        # splite up two methods to console
        print()


        # another way to traverse linked list
        temp = self.head

        for i in range(llist.size):
            print(temp.height)
            temp = temp.next

        return
            

    def traverse_list(self):
        pass



# using code below to test linked list

if __name__ == "__main__":

    from box_class import Box
    from display_class import Display

    llist = LinkedList()

    display = Display()

    for box in range(3):
        box = Box(display)
        llist.insert_box(box)


    llist.print_list()