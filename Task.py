class Task:

    def __init__(self, taskID, procesingTime):
        self.taskID = taskID
        self.inputBuffer = []
        self.batch = None
        self.processingTime = procesingTime
        self.isAvailable = True
        self.nextTask = None
    
    def setNextTask(self, task):
        self.nextTask = task

    def getNextTask(self):
        return self.nextTask

    def getTaskID(self):
        return self.taskID

    def setTaskID(self, taskID):
        self.taskID = taskID

    def addToInputBuffer(self, batch):
        self.inputBuffer.append(batch)

    def removeFromInputBuffer(self):
        batch = self.inputBuffer[0]
        self.inputBuffer.remove(self.inputBuffer[0])
        return batch

    def getSizeOfInputBuffer(self):
        numberOfWafers = 0
        for batch in self.inputBuffer:
            numberOfWafers += batch.getSize()
        return numberOfWafers


    def getInputBuffer(self):
        return self.inputBuffer
        
    def getProcessingTime(self):
        return self.processingTime

    def setAvailable(self):
        self.isAvailable = True
    
    def setOccupied(self):
        self.isAvailable = False
    
    def getAvailability(self):
        return self.isAvailable

    def setBatch(self, batch):
        self.batch = batch

    def getBatch(self):
        return self.batch

    def getNextBatch(self):
        batch = self.inputBuffer[0]
        self.inputBuffer.remove(batch)
        return batch

    def inputBufferAvalible(self, size):
        inputBufferSize = 0
        for batch in self.inputBuffer:
            inputBufferSize += batch.getSize()
        if inputBufferSize + size > 120:
            return False
        else:
            return True