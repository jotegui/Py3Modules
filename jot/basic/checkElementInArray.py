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

if __name__ == '__main__':
	print("This function should not be executed as a standalone program. It is rather a shortcut for a common python function")