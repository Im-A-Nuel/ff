class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None
        self.prev = None
    
class PriorityQueueSorted:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    def __len__(self):
        return self.size
    
    def print_all(self):
        if self.is_empty() == True:
            print('Priority Queue is empty')
        else:
            bantu = self.head
            while bantu != None:
                print(' (', bantu.data, ',', bantu.priority, ')', end=' ')
                bantu = bantu.next
            print()
    
    def remove(self):
        if self.is_empty == False:
            hapus = self.head
            if self.size ==  1:
                self.head = None
            else:
                self.head =  self.head.next
                self.head.prev = None
            del hapus
            self.size -=1

    def peek(self):
        if self.is_empty ==  True:
            return None
        else:
            return tuple([self.head.data, self.head.priority])
        
    def add (self, data, priority):
        baru = Node(data, priority)
        if self.is_empty():
            self.head = baru
            self.tail = baru
        elif self.size ==  1:
            if self.head.priority > priority:
                baru.next = self.head
                self.head.prev = baru
                self.head = baru
            else:
                self.head.next = baru
                baru.prev = self.head
                self.tail =  baru
        else:
            if self.head.priority > priority:
                baru.next = self.head
                self.head.prev =  baru
                self.head = baru
            elif self.tail.priority <= priority:
                self.tail.next = baru
                baru.prev = self.tail
                self.tail = baru
                self.tail.next =  None
            else:
                bantu = self.head
                while bantu.priority < priority:
                    bantu = bantu.next
                bantu2 =  bantu.prev
                baru.next = bantu
                bantu.prev = baru
                bantu2.next = baru
                baru.prev = bantu2
        self.size += 1

if __name__ == '__main__':
    myQueue =  PriorityQueueSorted()
    myQueue.add('Amber', 5)
    myQueue.add('Diluc', 1)
    myQueue.add('Beido', 3)
    myQueue.add('Kaeya', 4)
    myQueue.print_all()
            
