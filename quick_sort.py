def quick_sort(arr):
	if len(arr) <= 1:
		return arr
	pivot = arr[len(arr)//2]
	del arr[len(arr)//2]
	arr1, arr2 = [], []
	for i in range(len(arr)):
		if arr[i] <= pivot:
			arr1.append(arr[i])
		else:
			arr2.append(arr[i])
	return quick_sort(arr1) + [pivot] + quick_sort(arr2)

def main(input):
	arr = input.split(',')
	arr = [int(x) for x in arr]
	print(quick_sort(arr))

if __name__ == "__main__":
	main(input())