from implementation_classes.data_element import DataElement
import numpy as np

class DataGroup:
    """This is a group, for which the Normalized Performance Measure is calculted, also contain the data elements
    """
    def __init__(self, name = "", dataList = None, parent = None):
        self.name = name
        
        self.dataList = []
        if dataList:
            self.addElements(dataList)
            
        self.performanceMeasureValue = None
        self.parent = parent
        if parent:
            parent.dataCollectionList.append(self)
        
    def addElements(self, dataList):
        for val in dataList:
            self.dataList.append(DataElement(val))
    
    def addElement(self, elementValue):
        self.dataList.append(DataElement(elementValue))
               
    def getDataGroupElementsArray(self):
        """returns Data Elements in the Group in the form of List

        Returns:
            List : Data Elements but only values
        """           
        elementsValueList = []
        for dataElement in self.dataList:
            elementsValueList.append(dataElement.value)
        
        return elementsValueList

    def getDataGroupElementsTuple(self):
        """returns Data Elements in the Group in the form of Tuple

        Returns:
            Tuple : Data Elements but only values
        """
        return tuple(self.getDataGroupElementsArray())
    
    def getDataGroupElementsNumpyArray(self):
        """returns Data Elements in the Group in the form of Numpy Array

        Returns:
            Numpy Array : Data Elements but only values
        """
        return np.array(self.getDataGroupElementsArray())

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