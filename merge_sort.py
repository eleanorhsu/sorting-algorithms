def merge_sort(arr):
	if len(arr) <= 1:
		return arr
	arr1 = merge_sort(arr[:len(arr)//2])
	arr2 = merge_sort(arr[len(arr)//2:])
	print("merge:",arr1, arr2)
	index = 0
	for i in range(len(arr2)):
		while index < len(arr1) and arr2[i] > arr1[index]:
			index += 1
		arr1.insert(index, arr2[i])
		index += 1
	print("res:",arr1)
	return arr1

def main(input):
	arr = input.split(',')
	arr = [int(x) for x in arr]
	print(merge_sort(arr))

if __name__ == "__main__":
	main(input())