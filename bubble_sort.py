def bubble_sort(input):
	arr = input.split(',')
	flag = True
	while flag:
		flag = False
		for i in range(len(arr)-1):
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
				flag = True
	return arr

def main(input):
	print(bubble_sort(input))

if __name__ == "__main__":
	main(input())