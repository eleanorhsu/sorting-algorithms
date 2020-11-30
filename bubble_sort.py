def bubble_sort(arr):
	flag = True
	while flag:
		flag = False
		for i in range(len(arr)-1):
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
				flag = True
	return arr

def main(input):
	arr = input.split(',')
	arr = [int(x) for x in arr]
	print(bubble_sort(arr))

if __name__ == "__main__":
	main(input())