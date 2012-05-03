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
	
	from jot.basic.countDistinctValues import countDistinctValues
	
	finalarray = []
	provarray = list(countDistinctValues(array, pos).keys())
	
	for i in provarray:
	
		temparray = []
		
		for j in array:
		
			if i == j[0]:
				temparray.append(j[1:])
				
		finalarray.append(temparray)
		
	return finalarray

if __name__ == '__main__':
	print("This function should not be executed as a standalone program. It is rather a shortcut for a common python function")