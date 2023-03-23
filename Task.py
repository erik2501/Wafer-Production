class Task:

    def __init__(self, taskID, procesingTime):
        self.taskID = taskID
        self.inputBuffer = []
        self.processingTime = procesingTime
        self.isAvailable = True
    
    def getTaskID(self):
        return self.taskID

    def setTaskID(self, taskID):
        self.taskID = taskID

    def addToInputBuffer(self, batch):
        self.inputBuffer.append(batch)

    def removeFromInputBuffer(self):
        self.inputBuffer.remove(self.inputBuffer[0])

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