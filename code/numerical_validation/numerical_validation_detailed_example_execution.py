from implementation_classes.data_collection import DataCollection
from implementation_classes.data_group import DataGroup
import matplotlib.pyplot as plt
from scipy.stats import dunnett
    
def main():
   
    #detailed example
    postTherapyScoresComparison = DataCollection(ascendingOrder=True) #  Ascending Soring, more the Therapy Scores the better out of 15
    
    # Control Group, recover from a disease in days via their immune system
    controlGroup = DataGroup("Control", [6, 12, 12], postTherapyScoresComparison)
    
    # CBT Group
    cbtGroup =  DataGroup("CBT", [14, 15, 13, 13, 15], postTherapyScoresComparison)
    
    # Mindfulness Group
    mindfulnessGroup =  DataGroup("Mindfulness", [9, 8, 8, 7], postTherapyScoresComparison)
    
    # Experimental Group, recover from a disease in days via Drug C 
    pscyhoanalysisGroup =  DataGroup("Psychoanalysis", [2, 1, 3], postTherapyScoresComparison)
    
    # Perform Kruskal Wallish 'H' Test
    postTherapyScoresComparison.computeKruskalTest()
    print("Collection pValue:", postTherapyScoresComparison.psignificanceValue)
    if postTherapyScoresComparison.psignificanceValue < 0.05 :
        print("Deviation in one of Groups Detected!!!")
    else:
        print("No deviation groups")
    
    # perform Dunnett's Test
    result = dunnett(cbtGroup.getDataGroupElementsNumpyArray(),
            mindfulnessGroup.getDataGroupElementsNumpyArray(),
            pscyhoanalysisGroup.getDataGroupElementsNumpyArray(),
            control=controlGroup.getDataGroupElementsNumpyArray())
    
    cbtGroup.pValue = result.pvalue[0].item()
    mindfulnessGroup.pValue = result.pvalue[1].item()
    pscyhoanalysisGroup.pValue = result.pvalue[2].item()
    
    # perform Normalized Performance Measure
    postTherapyScoresComparison.process()
    
    # print and plot the results
    postTherapyScoresComparison.print()   
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.boxplot(postTherapyScoresComparison.getNestedArrayCollection())
    ax.set_xticklabels(postTherapyScoresComparison.getLabels(performenceIndexLabel=True))
    ax.set_ylabel("Post Therapy Scores (out of 15)")
    plt.show()
    
if __name__ == "__main__":
    main()
