class DataGroup:
    """This is a group, for which dominance value is calculte, which have date elements
    """
    def __init__(self, name, parent):
        self.name = name
        self.dataList = []
        self.performanceMeasureValue = -1
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

    def setPerformanceMeasureValue(self):
        """Calculates the normalized performance value, using the formula in the research paper
        """
        ni = self.getElementCount()
        sigma_ri = self.getRankedGroupSum()
        n = self.parent.netTotalItemsInCollection
        k = self.parent.getNumberOfGroups()
        self.performanceMeasureValue = (-ni + sigma_ri)/(ni*(n-1))