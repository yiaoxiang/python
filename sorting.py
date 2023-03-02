

def compare_n_swap(lst, val1, val2):
	orig = lst
	value1 = val1
	value2 = val2
	if orig[value1] > orig[value2]:
		tmp = orig[value2]
		orig[value2] = orig[value1]
		orig[value1] = tmp
	elif orig[value1] < orig[value2]:
		pass
	elif orig[value1] == orig[value2]:
		pass
	else:
		print("Error: unidentified error occured")
	return orig

def int_sort(lst, index, length):
	orig = lst
	size = len(orig)
	num_iteration = length
	index = 0
	while num_iteration != 0:
		if index == size - 1:
			while is_sorted != True:
				sorted_list = compare_n_swap(orig, orig[index], orig[index+1])
				currIndex = 0
				currIndex2 = 1
				while size != 1:
					for num in orig:
						if orig[currIndex] <= orig[currIndex2]:
							currIndex = currIndex + 1
							currIndex2 = currIndex2 + 1
							size = size - 1
							pass
						else:
							currIndex = currIndex + 1
							currIndex2 = currIndex2 + 1
							size = size - 1
							pass
							
				is_sorted = False
		
		index = index + 1
		size = size - 1

	int_sort(orig, index, size)
	return orig

def mod_insertion(lst):
	orig = lst
	size = len(lst)
	if size >= 2:
		sorted_list = int_sort(orig, 0, size)
	else:
		print("Error: please enter a valid list")

	return sorted_list

lst = [1, 5, 3, 2, 9, 7, 6, 4, 8, 10]

print(mod_insertion(lst))