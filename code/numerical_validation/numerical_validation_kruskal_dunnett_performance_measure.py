from implementation_classes.data_collection import DataCollection
from implementation_classes.data_group import DataGroup
import matplotlib.pyplot as plt
from scipy.stats import dunnett
    
def main():
   
    # simple example, will calculate min and max bounds and,
    # validate the research paper written bounds theoretically for Normalized Performance Measure
    dataCollectionDrugsComparison = DataCollection(ascendingOrder=False) #  Descending Order Sorting, lower the recovery days higher the ranks
    
    # Control Group, recover from a disease in days via their immune system
    controlGroup = DataGroup("Control Group", [7,6,5,9,10,7], dataCollectionDrugsComparison)
    
    # Experimental Group, recover from a disease in days via Drug A
    experimentalGroupDrugA =  DataGroup("Drug A", [1,2,3,2,1,3], dataCollectionDrugsComparison)
    
    # Experimental Group, recover from a disease in days via Drug B
    experimentalGroupDrugB =  DataGroup("Drug B", [3,7,8,2,9,10], dataCollectionDrugsComparison)
    
    # Experimental Group, recover from a disease in days via Drug C 
    experimentalGroupDrugC =  DataGroup("Drug C", [13,12,10,11,14,15], dataCollectionDrugsComparison)
    
    # Perform Kruskal Wallish 'H' Test
    dataCollectionDrugsComparison.computeKruskalTest()
    print("Collection pValue:", dataCollectionDrugsComparison.psignificanceValue)
    if dataCollectionDrugsComparison.psignificanceValue < 0.05 :
        print("Deviation in one of Groups Detected!!!")
    else:
        print("No deviation groups")
    
    # perform Dunnett's Test
    result = dunnett(experimentalGroupDrugA.getDataGroupElementsNumpyArray(),
            experimentalGroupDrugB.getDataGroupElementsNumpyArray(),
            experimentalGroupDrugC.getDataGroupElementsNumpyArray(),
            control=controlGroup.getDataGroupElementsNumpyArray())
    
    experimentalGroupDrugA.pValue = result.pvalue[0].item()
    experimentalGroupDrugB.pValue = result.pvalue[1].item()
    experimentalGroupDrugC.pValue = result.pvalue[2].item()
    
    # perform Normalized Performance Measure
    dataCollectionDrugsComparison.process()
    
    # print and plot the results
    dataCollectionDrugsComparison.print()   
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.boxplot(dataCollectionDrugsComparison.getNestedArrayCollection())
    ax.set_xticklabels(dataCollectionDrugsComparison.getLabels(performenceIndexLabel=True))
    ax.set_ylabel("Recovery in Days")
    plt.show()
    
if __name__ == "__main__":
    main()
