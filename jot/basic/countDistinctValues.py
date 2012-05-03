def countDistinctValues(array, pos = -1):
	"""
 Counts the number of times each element appears in an array, and returns a dictionary.
 Requires checkElementInArray function

 Arguments:
 array - the array to be scanned
 pos - (only with multi-level arrays) the index value to perform the search

 Example with simple array: We want to know the amount of times each number is in the next array
 array1 = [1,1,1,2,2,3,4,4,4,4,4,5]
 countDistinctValues(array1) # {1:3, 2:2, 3:1, 4:5, 5:1}

 Example with complex array: we want to know the different values of the first item in each inner array
 array2 = [[1,3],[1,6],[1,4],[2,5]]
 countDistinctValues(array2,0) # {1:3, 2:1}

 Author: JOT (javier.otegui@gmail.com)
 """
	
	from jot.basic.checkElementInArray import checkElementInArray

	finalDict = {}
	
	for i in array:
		
		match = 0
		
		if pos == -1:
			checkValue = i
		else:
			checkValue = i[pos]
			
		match = checkElementInArray(checkValue,finalDict)
		
		if match == False:
			finalDict[checkValue] = 1
		else:
			finalDict[checkValue] = finalDict[checkValue]+1
			
	return finalDict

if __name__ == '__main__':
	print("This function should not be executed as a standalone program. It is rather a shortcut for a common python function")