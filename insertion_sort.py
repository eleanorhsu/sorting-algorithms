def insertion_sort(arr):
	for i in range(1, len(arr)):
		for j in range(i):
			if arr[i] < arr[j]:
				arr.insert(j, arr[i])
				del arr[i+1]
				break
	return arr

def main(input):
	arr = input.split(',')
	arr = [int(x) for x in arr]
	print(insertion_sort(arr))

if __name__ == "__main__":
	main(input())