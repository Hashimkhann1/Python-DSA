


class Queue:
    
    
    def __init__(self):
        self.values = []
        
    def enQueue(self , x):
        self.values.append(x)
        
    def deQueue(self):
        front = self.values[0]
        self.values = self.values[1:]
        
        return front

    def showAllVlaues(self):
        return self.values
    

q1 = Queue()
q1.enQueue(3)
q1.enQueue(2)
q1.enQueue(6)
q1.enQueue(13)
print(q1.showAllVlaues())
q1.deQueue()
print(q1.showAllVlaues())