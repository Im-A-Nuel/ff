from SLNC import SingleLinkedList

class PriorityQueueUnsorted:
    #constructor
    def __init__(self):
        self.pqdata = SingleLinkedList()
    
    # memasukkan data (insert/add)
    def add(self, new_data, priority):
        # insert tail
        self.pqdata.insertTail(new_data, priority)
        

    # hapus data dengan priority tertinggi (remove/delete)
    def remove(self):
        # cek apakah priority queue masih kosong?
        if len(self.pqdata) == 0:
            return None
        else :
            # cari posisi data dengan priority tertinggi
            index = self.pqdata.find_highest_priority()
            deleted_value = self.pqdata.delete(index)
            return deleted_value

    # ambil nilai data dengan priority tertinggi (peek/min)
    def peek(self):
        index = self.pqdata.find_highest_priority()
        return self.pqdata.get(index)
    
    def __str__(self):
        return str(self.pqdata)
    

if __name__ ==  '__main__':
    pq = PriorityQueueUnsorted()
    print(pq)
    pq.add('Yuan', 3)
    pq.add('Bambang', 2)
    pq.add('Paul', 4)
    print(pq)
    front = pq.remove()
    print(front)
    print(pq)


        
