from implementation_classes.data_collection import DataCollection
from implementation_classes.data_group import DataGroup
from implementation_classes.data_element import DataElement
    
def main():
   
    # simple example, will calculate min and max bounds and,
    # validate the research paper written bounds theoretically for Normalized Performance Measure
    dataCollectionExample = DataCollection()
    
    # Group 1
    dg1 = DataGroup("Group I", dataCollectionExample)
    dg1.dataList.append(DataElement(1))  #minima as contains one element with rank 1
    
    # Group 2
    dg2 = DataGroup("Gropup II", dataCollectionExample)
    for i in range(2,11):
        dg2.dataList.append(DataElement(i))
    
    # Group 3
    dg3 = DataGroup("Group III", dataCollectionExample)
    dg3.dataList.append(DataElement(11)) #maxima as contains one element with the Nth rank
    
    dataCollectionExample.process()
    dataCollectionExample.print()
    
    #Test Cases to see to check if Performance measure is numerically validated or not
    assert dg1.performanceMeasureValue == 0 
    print("Minima Performance Measure is Validated")
    
    assert dg3.performanceMeasureValue == 1
    print("Maxima Performance Measure is Validated")

if __name__ == "__main__":
    main()
