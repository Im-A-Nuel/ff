class Node:
    def __init__(self, data, priority):
        self.data = data
        self.prioriry = priority
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.size

    def insertHead(self,new_data, priority):
        # buat node baru
        new_node = Node(new_data, priority)
        # cek dulu list kosong atau tidak
        if self.size == 0:
            # jika kosong, maka data baru menjadi head dan tail sekaligus
            self.head = new_node
            self.tail = new_node
        else:
            # tidak kosong, hubungkan data baru ke head
            new_node.next = self.head
            # pindahkan head ke depan
            self.head = new_node
        # data bertambah satu
        self.size += 1
    
    def insertTail(self, new_data, priority): 
        # buat node baru  
        new_node = Node(new_data, priority)
        # cek dulu linked list kosong atau tidak
        if self.tail == None:
            # masih kosong, node baru menjadi head dan tail sekaligus
            self.head = new_node
            self.tail = new_node
            self.tail.next = None
        else :
            # hubungkan tail ke node baru
            self.tail.next = new_node
            # pindahkan tail ke ujung
            self.tail =  new_node
        # data bertambah satu
        self.size += 1

    def insertMid(self, position,new_data, priority):
        # cek apakah linked list kosong?
        if self.size == 0:
            self.insertHead(new_data, priority)
        else:
            # jika tidak kosong, cek insert di mana
            if position <= 0:
                # insert pada head
                self.insertHead(new_data, priority)
            elif position > self.size :
                # insert pada tail
                self.insertTail(new_data, priority)
            else:
                # insert di tengah
                # buat node baru
                new_node = Node(new_data, priority)
                # taruh helper di posisi sebelum insert dengan looping
                helper = self.head
                for i in range(position-1): #selalu -1 karena pada posisi sebelumnya insert
                    helper = helper.next
                # hubungkan node baru ke node setelah helper
                new_node.next = helper.next
                helper.next = new_node
        self.size += 1

        
    def delete_head(self):
        # linked list kosong tidak bisa dihapus
        if self.size == 0:
            return None
        elif self.size == 1:
            helper =  self.head
            self.head =  None
            self.tail = None
            deleted_value = helper.data
            del helper
            self.size -=1
            return deleted_value
        else:
            helper =  self.head
            deleted_value = helper.data
            self.head = self.head.next
            del helper
            self.size -=1
            return deleted_value
        
    def delete_tail(self):
        # linked list kosong tidak bisa dihapus
        if self.size == 0:
            return None
        elif self.size == 1:
            # linked list menjadi kosong
            delete = self.tail
            deleted_value = delete.data
            self.tail = None
            self.head = None
            # hapus
            del delete
            # jumlah data berkurang satu
            self.size -= 1
            return deleted_value
        else:
            helper = self.head
            while helper.next != self.tail:
                helper = helper.next
            delete = self.tail
            deleted_value = delete.data
            self.tail = helper
            self.tail.next = None
            del delete
            self.size -=1
            return deleted_value
        
    def delete(self, position):
        # linked list kosong tidak bisa dihapus
        if self.size == 0:
            return None
        elif position == 0:
            return self.delete_head()
        elif position + 1 >= self.size:
            return self.delete_tail()
        else:
            # taruh delete di posisi node yang akan dihapus
            delete_node = self.head
            for i in range(position):
                delete_node = delete_node.next
            # taruh helper di posisi sebelum delete
            helper = self.head
            for i in range(position-1):
                helper = helper.next
            # hubungkan helper ke node sebelum delete_node
            helper.next = delete_node.next
            # hapus node delete_node
            deleted_value = delete_node.data
            del delete_node
            # jumlah data berkurang satu
            self.size -= 1
            return deleted_value
    
    def __str__(self):
        if self.size == 0:
            return 'Priority Queue is empty'
        else:
            result = 'Priority Queue contain ' + str(self.size) + ' data\n'
            result = result + '(Front) '
            helper = self.head
            while helper != None:
                result = result + '( ' + str(helper.data) + ', ' + str(helper.prioriry) + ') '
                helper = helper.next
            return result
        
    def find_highest_priority(self):
        highest_priority = self.head.prioriry
        highest_priority_index = 0
        position = 0
        helper = self.head
        while helper != None:
            if helper.prioriry < highest_priority:
                highest_priority = helper.prioriry
                highest_priority_index = position
            helper = helper.next
            position+=1
        return highest_priority_index
    
    def get(self, index):
        # cek apakah indexnya valid?
        if index < self.size and index >= 0:
            helper = self.head
            for i in range(index):
                helper = helper.next
            return helper.data
        else:
            return None

    def find_insert_position(self, priority):
        if self.size != 0:
            helper = self.head
            index = 0
            while helper != None:
                if helper.prioriry > priority:
                    break
                else:
                    helper = helper.next
                    index += 1
            return index


