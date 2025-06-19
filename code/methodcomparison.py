import math
from scipy import stats

class DataCollection:
    def __init__(self):
        self.dataCollectionList = []
        self.netTotalItemsInCollection = 0
        self.sumTotal = 0
        self.sumLowerDominantHalf = 0
        self.sumUpperDominantHalf = 0
        self.psignificanceValue = 0

    def computeKruskalTest(self):

        arrayDataCollectionGroups = []
        
        for itemGroup in self.dataCollectionList:
            arrayDataCollectionGroups.append(itemGroup.getDataGroupTupleElements())

        tupleDataCollectionGroups = tuple(arrayDataCollectionGroups)
        h, self.psignificanceValue = stats.kruskal(*tupleDataCollectionGroups)

    def getNumberOfGroups(self):
        return len(self.dataCollectionList)

    def print(self):
        print("collection p Significance Value:", self.psignificanceValue)
        for itemGroup in self.dataCollectionList:
            print(itemGroup.name, "Dominance Value:", itemGroup.dominanceValue)
            for itemElement in itemGroup.dataList:
                print(itemGroup.name, itemElement.value, itemElement.rank)

    def __getNextElement(self):
        for itemGroup in self.dataCollectionList:
            for itemElement in itemGroup.dataList:
                if itemElement.rank == -1:
                    return itemElement
                
    def __getListBelongingToSameRank(self, valueToCheck):
        lstBelongingToSameRank = []
        for itemGroup in self.dataCollectionList:
            for itemElement in itemGroup.dataList:
                if itemElement.value == valueToCheck:
                    lstBelongingToSameRank.append(itemElement)

        return lstBelongingToSameRank
    
        
    def __calculateNetTotalItemsInCollection(self):
        self.netTotalItemsInCollection = 0
        for itemGroup in self.dataCollectionList:
            self.netTotalItemsInCollection += len(itemGroup.dataList)
        # print("self.netTotalItemsInCollection", self.netTotalItemsInCollection)

    def __calculateTotalSum(self):
        self.sumTotal = self.netTotalItemsInCollection * (self.netTotalItemsInCollection + 1) * 0.5


    def __calculateLowerDominantHalf(self):
         a = math.floor(self.netTotalItemsInCollection/2)
         self.sumLowerDominantHalf = a * (a + 1) * 0.5

    def __calculateUpperDominantHalf(self):
        self.sumUpperDominantHalf = self.sumTotal - self.sumLowerDominantHalf

    def __orderByRank(self):
        rank = 0
        itemToRank = self.__getNextElement()
        while itemToRank:
            for itemGroup in self.dataCollectionList:
                for itemElement in itemGroup.dataList:
                    if itemElement.rank == -1:
                        if itemElement.value < itemToRank.value:
                            itemToRank = itemElement

            rank += 1
            itemToRank.rank = rank
            itemToRank = self.__getNextElement()

    def __averageOutSameRanks(self):
        for itemGroup in self.dataCollectionList:
            for itemElement in itemGroup.dataList:
                lstBelongingToSameRanks = self.__getListBelongingToSameRank(itemElement.value)
                if len(lstBelongingToSameRanks) > 1:
                    totalSum = 0
                    for item in lstBelongingToSameRanks:
                        totalSum += item.rank

                    average = totalSum / len(lstBelongingToSameRanks)
                    
                    for item in lstBelongingToSameRanks:
                        item.rank = average

    def process(self):
        self.__orderByRank()
        self.__averageOutSameRanks()
        self.__calculateNetTotalItemsInCollection()
        self.__calculateTotalSum()
        self.__calculateLowerDominantHalf()
        self.__calculateUpperDominantHalf()

        for group in self.dataCollectionList:
            group.setDominanceValue()

class DataGroup:
    def __init__(self, name, parent):
        self.name = name
        self.dataList = []
        self.dominanceValue = -1
        self.parent = parent
        parent.dataCollectionList.append(self)

    def getDataGroupTupleElements(self):
        returnArray = []
        for elem in self.dataList:
            returnArray.append(elem.value)
        return tuple(returnArray)

    def getRankedGroupSum(self):
        sum = 0
        for elem in self.dataList:
            sum += elem.rank
        return sum

    def setDominanceValue(self):
        weightbias = self.parent.netTotalItemsInCollection /  (self.parent.getNumberOfGroups() * len(self.dataList))
        rankedGroupSum = self.getRankedGroupSum()
        self.dominanceValue = weightbias * rankedGroupSum / self.parent.sumUpperDominantHalf

class DataElement:
    def __init__(self, value):
        self.value = value
        self.rank = -1

def main():
     
    #example with multiple groups and tied ranks and uneven weights
    dataCollection = DataCollection()

    dataGroup1 = DataGroup("GroupA", dataCollection)
    dataGroup1.dataList.append(DataElement(95))
    dataGroup1.dataList.append(DataElement(48))
    dataGroup1.dataList.append(DataElement(25))
    dataGroup1.dataList.append(DataElement(15))

    dataGroup2 = DataGroup("GroupB", dataCollection)
    dataGroup2.dataList.append(DataElement(83))
    dataGroup2.dataList.append(DataElement(57))
    dataGroup2.dataList.append(DataElement(100))

    dataGroup3 = DataGroup("GroupC", dataCollection)
    dataGroup3.dataList.append(DataElement(70))
    dataGroup3.dataList.append(DataElement(20))
    dataGroup3.dataList.append(DataElement(40))

    dataGroup4 = DataGroup("GroupD", dataCollection)
    dataGroup4.dataList.append(DataElement(95))
    dataGroup4.dataList.append(DataElement(15))
    dataGroup4.dataList.append(DataElement(18))
    dataGroup4.dataList.append(DataElement(30))
    dataGroup4.dataList.append(DataElement(10))

    dataCollection.computeKruskalTest()
    dataCollection.process()
    dataCollection.print()
    
    #another simpler example
    dataCollectionAnotherExample = DataCollection()
    dg1 = DataGroup("GrpI", dataCollectionAnotherExample)
    dg1.dataList.append(DataElement(10))
    dg1.dataList.append(DataElement(11))
    dg1.dataList.append(DataElement(11))
    dg1.dataList.append(DataElement(11))
    dg1.dataList.append(DataElement(11))


    dg2 = DataGroup("GrpII", dataCollectionAnotherExample)
    dg2.dataList.append(DataElement(11))
    dg2.dataList.append(DataElement(11))
    dg2.dataList.append(DataElement(11))
    dg2.dataList.append(DataElement(11))
    dg2.dataList.append(DataElement(11))

    dataCollectionAnotherExample.computeKruskalTest()
    dataCollectionAnotherExample.process()
    dataCollectionAnotherExample.print()

if __name__ == "__main__":
    main()
