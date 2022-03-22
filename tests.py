from circularQueue import MyCircularQueue

def test_enQueue():
    obj = MyCircularQueue(3)

    assert obj.enQueue(0) == True
    
    obj.enQueue(1)
    obj.enQueue(2)
    
    assert obj.queue == [0,1,2]
    assert obj.enQueue(1) == False
    
    #Simulating the removal of a number from the queue
    #without using deQueue()
    #Ensuring proper wrap-around.
    obj.queue = [None, 1, 2]
    obj.qu = 1
    obj.enQueue(3)
    
    assert obj.queue == [3,1,2]

def test_deQueue():
    obj = MyCircularQueue(3)
    obj.queue = [0,1,2]

    assert obj.deQueue() == True
    
    assert obj.queue == [None, 1, 2]

    obj.deQueue()
    obj.deQueue()
    
    assert obj.queue == [None, None, None]
    
    #Ensuring wrap-around.
    obj.queue = [3, None, None]
    obj.deQueue()
    
    assert obj.queue == [None, None, None]
    assert obj.deQueue() == False

#Normally, you should only call the function that is being tested.
#However, the values that dictate the front and rear of the queue
#are managed by queue and dequeue. Thus, they will be called in this
#test.

def test_Front():
    obj = MyCircularQueue(3)
    obj.enQueue(0)
    obj.enQueue(1)
    obj.enQueue(2)

    assert obj.Front() == 2

    obj.deQueue()
    obj.enQueue(3)

    assert obj.Front() == 3

    obj.deQueue()
    obj.deQueue()
    obj.deQueue()

    assert obj.Front() == -1

def test_Rear():
    obj = MyCircularQueue(3)
    obj.enQueue(0)
    obj.enQueue(1)
    obj.enQueue(2)

    assert obj.Rear() == 0

    obj.deQueue()
    obj.enQueue(3)

    assert obj.Rear() == 1
    
    obj.deQueue()
    obj.deQueue()
    obj.deQueue()

    assert obj.Rear() == -1

def test_isEmpty():
    obj = MyCircularQueue(3)

    assert obj.isEmpty() == True

    obj.queue = [0,1,2]

    assert obj.isEmpty() == False

    obj.queue = [None, 1, 2]
    obj.it = 0
    obj.qu = 1

    assert obj.isEmpty() == False

def test_isFull():
    obj = MyCircularQueue(3)

    assert obj.isFull() == False

    obj.queue = [0,1,2]

    assert obj.isFull() == True

    obj.queue = [None, 1, 2]
    obj.it = 0
    obj.qu = 1

    assert obj.isFull() == False