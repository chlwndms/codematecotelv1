id = []
time =[]
MAX_QUEUE_SIZE = 14

class Queue:
    def __init__(self):
        self.arr = [None] * MAX_QUEUE_SIZE
        self.head = 0
        self.tail = 0

    def is_empty(self):
        if self.head == self.tail:
            return True
        return False

    def is_full(self):
        if (self.tail + 1) % MAX_QUEUE_SIZE == self.head:
            return True
        return False

    def enqueue(self, item):
        if self.is_full():
            print("큐에 더이상 데이터를 넣을 수 없습니다.")
        else:
            self.tail = (self.tail + 1) % MAX_QUEUE_SIZE
            self.arr[self.tail] = item
            

    def dequeue(self):
        if self.is_empty():
            print("큐가 비어있습니다.")
        else:
            self.head = (self.head + 1) % MAX_QUEUE_SIZE
            return self.arr[self.head]
    
    def print(self):
        print("------")
        flag = 1
        txt = str(self.arr[1])
        for i in range (2, int(self.tail)+1):
            if self.arr[i] == 0:
                print(txt)
                flag = 0
                txt = ""
            elif flag == 0:
                txt += str(self.arr[i])
                flag = 1
            elif flag == 1:
                txt += ", "+str(self.arr[i])
        print(txt)
            
            

for i in range(7):
    ID, T = map(int, input().split())
    id.append(ID)
    time.append(T)

check = Queue()

sum = 0
min = 0
for i in range(7):
    e_time = time[i]
    if sum + e_time > 50 :
        check.enqueue(0)
        check.enqueue(id[i])
        sum = e_time
        min += (e_time+10)
    else :
        sum += e_time
        check.enqueue(id[i])
        min += e_time

check.print()
print("\n총 소요시간: "+str(min)+"분")
