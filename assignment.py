# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside Enqueue() and Dequeue() - move the pointers yourself.

# Exercise 1
Queue = []
HeadPointer = -1
TailPointer = -1
NumberItems = 0
# Write code here to fill Queue with 10 elements, all -1
for i in range(10):
    Queue.append(-1)


def Enqueue(Data):
    # Write your code here
    global Queue, HeadPointer, TailPointer, NumberItems
    if NumberItems == 10:
        return False
    if NumberItems == 0:
        HeadPointer = 0
        TailPointer = 0
    else:
        TailPointer = TailPointer + 1
        if TailPointer == 10:
            TailPointer = 0
    Queue[TailPointer] = Data
    NumberItems = NumberItems + 1
    return True


def Dequeue():
    # Write your code here
    global Queue, HeadPointer, TailPointer, NumberItems
    if NumberItems == 0:
        return -999
    Item = Queue[HeadPointer]
    HeadPointer = HeadPointer + 1
    if HeadPointer == 10:
        HeadPointer = 0
    NumberItems = NumberItems - 1
    if NumberItems == 0:
        HeadPointer = -1
        TailPointer = -1
    return Item


# Exercise 2
def LoadQueue(Filename):
    # Write your code here
    Count = 0
    File = open(Filename, "r")
    for Line in File:
        Line = Line.strip()
        if Line != "":
            if Enqueue(int(Line)) == False:
                print("Queue full")
                break
            Count = Count + 1
    File.close()
    return Count


# Exercise 3
def RemoveNegatives():
    # Write your code here
    Total = NumberItems
    Removed = 0
    for i in range(Total):
        Item = Dequeue()
        if Item >= 0:
            Enqueue(Item)
        else:
            Removed = Removed + 1
    return Removed
