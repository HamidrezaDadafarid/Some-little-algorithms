def maxDiff(arr, arr_size):
	max_diff = arr[1] - arr[0]
	min_element = arr[0]
	min_index = 0
	max_index = 0
	for i in range( 1, arr_size ):
		if (arr[i] - min_element > max_diff):
			max_diff = arr[i] - min_element
			max_index = i
	
		if (arr[i] < min_element):
			min_element = arr[i]
			min_index = i
	return min_index, max_index
	
arr = [2, 10, 1, 100]
size = len(arr)
min_index, max_index = maxDiff(arr, size)
print (f"Maximum difference is between index {min_index} and {max_index}")

