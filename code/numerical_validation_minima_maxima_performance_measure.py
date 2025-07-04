import math
from scipy import stats

class DataCollection:
    """Collection contains groups, which in turn contain data elements 
    """
    
    def __init__(self):
        """Constructor defining, N (netTotalItemsInCollection), also contains list of groups.
        """
        self.dataCollectionList = []
        self.netTotalItemsInCollection = 0

    def computeKruskalTest(self):
        arrayDataCollectionGroups = []
        
        for itemGroup in self.dataCollectionList:
            arrayDataCollectionGroups.append(itemGroup.getDataGroupTupleElements())

        tupleDataCollectionGroups = tuple(arrayDataCollectionGroups)
        h, self.psignificanceValue = stats.kruskal(*tupleDataCollectionGroups)

    def getNumberOfGroups(self):
        return len(self.dataCollectionList)

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
        """this function will process the DataCollection, in strict order,
    1. sort the data in ascending order
    2. if some data have tied ranks then average it out
    3. calculates the total sum, lower dominant half to calculate the upper dominant half
    4. then for each group in the collection, calculate the dominance value
        """
        self.__orderByRank()
        self.__averageOutSameRanks()
        self.__calculateNetTotalItemsInCollection()

        for group in self.dataCollectionList:
            group.setDominanceValue()
    
            
    def print(self):
        """prints information regarding our group showing each group dominance value and 
        all the data contained within each group and what rank the data element in the group
        has been assigned
        """
        print("-" * 15)
        print("Total Items in Collection ( N =", self.netTotalItemsInCollection,")")
        for itemGroup in self.dataCollectionList:
            print()
            print(itemGroup.name, "Normalized Performance Measure:", itemGroup.dominanceValue)
            for itemElement in itemGroup.dataList:
                print(itemGroup.name,", Value:", itemElement.value,", Rank", itemElement.rank)
        print("-" * 15)

class DataGroup:
    """This is a group, for which dominance value is calculte, which have date elements
    """
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
    
    def getElementCount(self):
        return len(self.dataList)

    def setDominanceValue(self):
        """Calculates the normalized performance value, using the formula in the research paper
        """
        ni = self.getElementCount()
        sigma_ri = self.getRankedGroupSum()
        n = self.parent.netTotalItemsInCollection
        k = self.parent.getNumberOfGroups()
        self.dominanceValue = (-ni + sigma_ri)/(ni*(n-1))
        

class DataElement:
    """Data element is a value, and the rank assigned is when the data is sorted in ascendinng order
    """
    def __init__(self, value):      
        """This is constructor takes in the value to be set automatically for the object itself

        Args:
            value (variable): It depends on what elements being stored, what's the grading scale is (1-100, A-F etc.)
        """
        self.value = value
        self.rank = -1

def main():
   
    # simple example, will calculate min and max bounds and,
    # validate the research paper written bounds theoretically for Normalized Performance Measure
    dataCollectionAnotherExampleOdd = DataCollection()
    
    # Group 1
    dg1 = DataGroup("Group I", dataCollectionAnotherExampleOdd)
    dg1.dataList.append(DataElement(1))  #minima as contains one element with rank 1

    # Group 2
    dg2 = DataGroup("Gropup II", dataCollectionAnotherExampleOdd)
    dg2.dataList.append(DataElement(2))
    dg2.dataList.append(DataElement(3))
    dg2.dataList.append(DataElement(4))
    dg2.dataList.append(DataElement(5))
    dg2.dataList.append(DataElement(6))
    dg2.dataList.append(DataElement(7))
    dg2.dataList.append(DataElement(8))
    dg2.dataList.append(DataElement(9))
    dg2.dataList.append(DataElement(10))
    
    # Group 3
    dg3 = DataGroup("Group III", dataCollectionAnotherExampleOdd)
    dg3.dataList.append(DataElement(11)) #maxima as contains one element with the Nth rank
    
    dataCollectionAnotherExampleOdd.process()
    dataCollectionAnotherExampleOdd.print()

if __name__ == "__main__":
    main()
