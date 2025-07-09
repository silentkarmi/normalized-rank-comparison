from implementation_classes.data_collection import DataCollection
from implementation_classes.data_group import DataGroup
import matplotlib.pyplot as plt
    
def main():
   
    # simple example, will calculate min and max bounds and,
    # validate the research paper written bounds theoretically for Normalized Performance Measure
    dataCollectionDrugsComparison = DataCollection()
    
    # Control Group, recover from a disease in days via their immune system
    controlGroup = DataGroup("Control Group", [7,6,5,9,10,7], dataCollectionDrugsComparison)
    
    # Experimental Group, recover from a disease in days via Drug A
    experimentalGroupDrugA =  DataGroup("Drug A", [1,2,3,2,1,3], dataCollectionDrugsComparison)
    
    # Experimental Group, recover from a disease in days via Drug B
    experimentalGroupDrugB =  DataGroup("Drug B", [3,4,5,2,3,5], dataCollectionDrugsComparison)
    
    
    fig, ax = plt.subplots(1, 1)
    ax.boxplot(dataCollectionDrugsComparison.getNestedArrayCollection())
    ax.set_xticklabels(dataCollectionDrugsComparison.getLabels())
    ax.set_ylabel("Recovery in Days")
    plt.show()
    
if __name__ == "__main__":
    main()
