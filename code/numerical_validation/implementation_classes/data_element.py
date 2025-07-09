class DataElement:
    """Data element is a value, and the rank assigned is when the data is sorted in ascendinng order
    """
    def __init__(self, value):      
        """This is constructor takes in the value to be set automatically for the object itself

        Args:
            value (variable): It depends on what elements being stored, what's the grading scale is (1-100, A-F etc.)
        """
        self.value = value
        self.rank = None