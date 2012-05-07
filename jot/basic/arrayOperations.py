def checkElementInArray(element,array):
	"""
 Iterates through an array or list in search for a given element, then returns boolean.

 Arguments:
 element - the element to be found
 array - the array (or list) on which perform the search

 Example: We want to check if the number 3 is in the array [1,2,3,4,5]
 array1 = [1,2,3,4,5]
 element1 = 3
 checkElementInArray(element1,array1) # True
 
 Author: JOT (javier.otegui@gmail.com)
 """
	
	exists = False
	
	for i in array:
	
		if i == element:
			exists = True

	return exists

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
	
#	from jot.basic.checkElementInArray import checkElementInArray

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

def segmentArray(array, pos = 0):
	"""
 Takes an array of arrays and re-organizes it according to the values in certain position of inner array.
 Requires countDistinctValues

 Arguments:
 array - the array to be scanned
 pos - the index value for inner arrays on which the categorization values are stored

 Example: First item is category
 array1 = [[1,4,'a'],[1,5,'b'],[2,4,'c'],[2,6,'d'],[3,7,'e'],[3,8,'f']]
 segmentArray(array1,0) # [[[4,'a'],[5,'b']],[[4,'c'],[6,'d']],[[7,'e'],[8,'f']]]

 Author: JOT (javier.otegui@gmail.com)
 """
	
#	from jot.basic.countDistinctValues import countDistinctValues
	
	finalarray = []
	provarray = list(countDistinctValues(array, pos).keys())
	
	for i in provarray:
	
		temparray = []
		
		for j in array:
		
			if i == j[0]:
				temparray.append(j[1:])
				
		finalarray.append(temparray)
		
	return finalarray

