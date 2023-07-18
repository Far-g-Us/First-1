#-------------Hw-13-#1----------------------------#
# С помощью классов в python создать ПК
# Корпус
# порядок запуска
#   1. Блок питания
#   2. Мат плата
#   3. Процессор
#   4. Оперативная память
#   5. Видеокарта
#   6. Постоянная память (SSD HDD m2.ssd)


from abc import ABC,abstractmethod
# В данном коде абстрактный метод не работает или по крайнем мере я не понимаю как его тут реализовать(код придётся переписать с нуля при реализации абстрактного метода)
class Corpus(ABC):
    @abstractmethod
    def __init__(self,pu,motherboard,cpu,ram,gpu,externalMemory):
        self.PU = pu
        self.motherboard = motherboard
        self.CPU = cpu
        self.RAM = ram
        self.GPU = gpu
        self.externalMemory = externalMemory

class PU:
    def __init__(self,power):
        self.power = power

    def start(self):
        print("Запуск")

    def stop(self):
        print("Стоп")  

class Motherboard:
    def __init__(self,socket,chipset,compatibleProcessorCoresAMD):
        self.socket = socket
        self.chipset = chipset
        self.compatibleProcessorCoresAMD = compatibleProcessorCoresAMD
    
    def start(self):
        print("Запуск")

    def stop(self):
        print("Стоп")

class CPU:
    def __init__(self,totalNumberOfCores,baseFrequencyOfTheProcessor,maximumNumberOfThreads):
        self.totalNumberOfCores = totalNumberOfCores
        self.baseFrequencyOfTheProcessor = baseFrequencyOfTheProcessor
        self.maximumNumberOfThreads = maximumNumberOfThreads

    def start(self):
        print("Запуск")

    def stop(self):
        print("Стоп")

class RAM:
    def __init__(self,memoryType,memoryFormFactor,clockFrequency):
        self.memoryType = memoryType
        self.memoryFormFactor = memoryFormFactor
        self.clockFrequency = clockFrequency

    def start(self):
        print("Запуск")

    def stop(self):
        print("Стоп")

class GPU:
    def __init__(self,theAmountOfVideoMemory,memoryType,theNominalFrequencyOfTheVideoChip,numberOfUniversalProcessors):
        self.theAmountOfVideoMemory = theAmountOfVideoMemory
        self.memoryType = memoryType
        self.theNominalFrequencyOfTheVideoChip = theNominalFrequencyOfTheVideoChip
        self.numberOfUniversalProcessors = numberOfUniversalProcessors

    def start(self):
        print("Запуск")

    def stop(self):
        print("Стоп")

class ExternalMemory:
    def __init__(self,externalMemory,volume,maximumDataTransferRate):
        self.externalMemory = externalMemory
        self.volume = volume
        self.maximumDataTransferRate = maximumDataTransferRate
        
    def start(self):
        print("Запуск")

    def stop(self):
        print("Стоп")  

myPU = PU("550w")
myMotherboard = Motherboard("AM5","AMD B650","Raphael")
myCPU = CPU("6","4.7GHz","12")
myRAM = RAM("DDR5","DIMM","4800MHz")
myGPU = GPU("12Gb","GDDR6X","2310MHz","7680")
myExternalMemory = ExternalMemory("SSD","120Gb","530MB/sec")
myPC = Corpus(myPU,myMotherboard,myCPU,myRAM,myGPU,myExternalMemory)
print(myPC.motherboard.chipset)
print(myPC.motherboard.compatibleProcessorCoresAMD)
print(myPC.motherboard.socket)
myCPU.start()

