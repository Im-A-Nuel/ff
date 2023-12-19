class PriorityQueue:
    def _init_(self):
        self.queue = []

    def enqueue(self, item, priority):
        # Menambahkan elemen dengan prioritas ke dalam antrian
        entry = (priority, item)
        i = 0
        while i < len(self.queue) and self.queue[i][0] < priority:
            i += 1
        self.queue.insert(i, entry)

    def dequeue(self):
        if not self.is_empty():
            # Mengambil elemen dengan prioritas tertinggi
            return self.queue.pop(0)
        else:
            return "Antrian kosong"

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Contoh penggunaan:
pq = PriorityQueue()
pq.enqueue("Tugas 1", 3)
pq.enqueue("Tugas 2", 1)
pq.enqueue("Tugas 3", 2)

print(pq.dequeue())  # Output: "Tugas 2" (prioritas terendah)
print(pq.dequeue())  # Output: "Tugas 3"
print(pq.dequeue())  # Output: "Tugas 1" (prioritas tertinggi)