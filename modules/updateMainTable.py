import main

def updateWorker(self,values):
    main.MainWindow.updateWorkerInTable(self,values)

def addNewWorkerRow(self,values):
    main.MainWindow.addWorkerRecordInTable(self,values)

def updateWorkerColumn(self,column,pValue,nValue):
    main.MainWindow.updateColumnInTable(self,column,pValue,nValue)