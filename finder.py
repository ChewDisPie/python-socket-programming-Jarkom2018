def find(searchElement, array):
	for element in array:
		if searchElement in element:
			return element

	return ''
