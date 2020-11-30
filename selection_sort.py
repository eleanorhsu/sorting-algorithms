def selection_sort(arr):
	for i in range(len(arr)):
		m, index = arr[i], i
		for j in range(i, len(arr)):
			if arr[j] < m:
				m, index = arr[j], j
		arr[i], arr[index] = arr[index], arr[i]
	return arr

def main(input):
	arr = input.split(',')
	arr = [int(x) for x in arr]
	print(selection_sort(arr))

if __name__ == "__main__":
	main(input())