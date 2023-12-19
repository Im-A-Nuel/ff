from SLNC import SingleLinkedList

class PriorityQueueSorted:
    # constructor
    def __init__(self):
        self.pqdata = SingleLinkedList()

    def add(self, new_data, priority):
        if len(self.pqdata) == 0:
            self.pqdata.insertHead(new_data, priority)
        else:
            if self.pqdata.head.prioriry > priority:
                self.pqdata.insertHead(new_data,priority)
            elif self.pqdata.tail.prioriry <= priority:
                self.pqdata.insertTail(new_data, priority)
            else:
                # insert berdasarkan urutam prioritas
                index = self.pqdata.find_insert_position(priority)
                self.pqdata.insertMid(index, new_data, priority)

    def remove(self):
        return self.pqdata.delete_head()

    def peek(self):
        if len(self.pqdata)  == 0:
            return None
        else :
            return self.pqdata.head.data
        
    def __str__(self):
        return str(self.pqdata)
        
if __name__ == '__main__':
    pq = PriorityQueueSorted()
    print(pq)
    pq.add('Yuan', 3)
    pq.add('Bambang', 2)
    pq.add('Paul', 4)
    pq.add('Raul', 3)
    print(pq)
    front = pq.remove()
    print(front)
    print(pq)