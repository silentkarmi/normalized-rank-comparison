import math

class DataCollection:
    # sumUpperDominantHalf = 0
    # sumLowerDominantHalf = 0

    # netTotalItemsInCollection = 0

    def __init__(self):
        self.dataCollectionList = []
        DataCollection.netTotalItemsInCollection = 0
        DataCollection.sumLowerDominantHalf = 0
        DataCollection.sumUpperDominantHalf = 0


    def print(self):
        for itemGroup in self.dataCollectionList:
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
        DataCollection.netTotalItemsInCollection = 0
        for itemGroup in self.dataCollectionList:
            DataCollection.netTotalItemsInCollection += len(itemGroup.dataList)
        # print("DataCollection.netTotalItemsInCollection", DataCollection.netTotalItemsInCollection)

    def __calculateLowerDominantHalf(self):
         DataCollection.sumLowerDominantHalf = 0
         a = math.ceil(DataCollection.netTotalItemsInCollection)

    def __calculateUpperDominantHalf(self):
        pass

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
        self.__calculateLowerDominantHalf()
        self.__calculateUpperDominantHalf()

class DataGroup:
    def __init__(self, name):
        self.name = name
        self.dataList = []
        self.dominanceValue = -1

class DataElement:
    def __init__(self, value):
        self.value = value
        self.rank = -1

def main():
    dataGroup1 = DataGroup("GroupA")
    dataGroup1.dataList.append(DataElement(10))
    dataGroup1.dataList.append(DataElement(10))
    dataGroup1.dataList.append(DataElement(10))
    dataGroup1.dataList.append(DataElement(10))


    dataGroup2 = DataGroup("GroupB")
    dataGroup2.dataList.append(DataElement(100))
    dataGroup2.dataList.append(DataElement(100))
    dataGroup2.dataList.append(DataElement(100))
    dataGroup2.dataList.append(DataElement(100))

    dataCollection = DataCollection()
    dataCollection.dataCollectionList.append(dataGroup1)
    dataCollection.dataCollectionList.append(dataGroup2)

    dataCollection.process()
    dataCollection.print()

if __name__ == "__main__":
    main()
