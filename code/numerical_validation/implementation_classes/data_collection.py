from scipy import stats

class DataCollection:
    """Collection contains groups, which in turn contain data elements 
    """
    
    def __init__(self, ascendingOrder = True):
        """Constructor defining, N (netTotalItemsInCollection), also contains list of groups.
        """
        self.dataCollectionList = []
        self.netTotalItemsInCollection = 0
        self.ascendingOrder = ascendingOrder

    def computeKruskalTest(self):
        arrayDataCollectionGroups = []
        
        for itemGroup in self.dataCollectionList:
            arrayDataCollectionGroups.append(itemGroup.getDataGroupElementsTuple())

        tupleDataCollectionGroups = tuple(arrayDataCollectionGroups)
        h, self.psignificanceValue = stats.kruskal(*tupleDataCollectionGroups)
        
    def getNestedArrayCollection(self):
        arrayDataCollectionGroups = []
        
        for itemGroup in self.dataCollectionList:
            arrayDataCollectionGroups.append(itemGroup.getDataGroupElementsArray())
            
        return arrayDataCollectionGroups
        
    def getLabels(self, performenceIndexLabel = False):
        listLabels = []
        for itemGroup in self.dataCollectionList:
            if performenceIndexLabel:
                
                if itemGroup.name == "Control Group":
                    listLabels.append(itemGroup.name + 
                                    ",\n$P_i=$" + str(round(itemGroup.performanceMeasureValue,2))
                                    )
                else:
                    listLabels.append(itemGroup.name + 
                                    ",\n$P_i=$" + str(round(itemGroup.performanceMeasureValue,2)) +
                                    ",\n$pValue=$" + str(round(itemGroup.pValue,4))
                                    )
            else:
                listLabels.append(itemGroup.name)
        
        return listLabels

    def getNumberOfGroups(self):
        return len(self.dataCollectionList)

    def __getNextElement(self):
        for itemGroup in self.dataCollectionList:
            for itemElement in itemGroup.dataList:
                if itemElement.rank == None:
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

    def __orderByRank(self):
        rank = 0
        itemToRank = self.__getNextElement()
        while itemToRank:
            for itemGroup in self.dataCollectionList:
                for itemElement in itemGroup.dataList:
                    if itemElement.rank == None:
                        if self.ascendingOrder:
                            if itemElement.value < itemToRank.value:
                                itemToRank = itemElement
                        else:
                            if itemElement.value > itemToRank.value:
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
        """this function will process the DataCollection, in strict order,
    1. sort the data in ascending order
    2. if some data have tied ranks then average it out
    3. calculates the N, the total items across all collection
    4. then for each group in the collection, calculate the Normalized Performance Measure
        """
        self.__orderByRank()
        self.__averageOutSameRanks()
        self.__calculateNetTotalItemsInCollection()

        for group in self.dataCollectionList:
            group.setPerformanceMeasureValue()
            group.setNonNormalizedPerformanceMeasureValue()
    
            
    def print(self):
        """prints information regarding our group showing each Normalized Performance Measure and 
        all the data contained within each group and what rank the data element in the group
        has been assigned
        """
        print("-" * 15)
        print("Total Items in Collection ( N =", self.netTotalItemsInCollection,")")
        for itemGroup in self.dataCollectionList:
            print()
            print(itemGroup.name, "Normalized Performance Measure:", itemGroup.performanceMeasureValue)
            print(itemGroup.name, "Non Normalized Performance Measure:", itemGroup.nonNormalizedPerformanceMeasureValue)
            for itemElement in itemGroup.dataList:
                print(itemGroup.name,", Value:", itemElement.value,", Rank", itemElement.rank)
        print("-" * 15)