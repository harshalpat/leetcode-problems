
# mon -> tue -> wed -> thur -> fri -> sat ->sun

class node:
    def __init__(self, data = None):
        self.data = data;
        self.link = None;

class linkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        while(self.head):
            print(self.head.data);
            self.head = self.head.link;

    def addAtFront(self):
        temp = node(0);
        temp.link = self.head;
        self.head = temp;

    def addAtEnd(self):
        last = node(10);
        while(self.head.link != None):
            self.head = self.head.link;
        self.head.link = last;
            
        
        
if __name__ == '__main__':
    list1 = linkedList();
    list1.head = node(1);
    second = node(2);
    third = node(3);

    list1.head.link = second;
    second.link = third;

    list1.printList
