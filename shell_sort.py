def shell_sort(arr):
	gap = len(arr)//2
	while gap >= 1:
		for start in range(gap):
			for i in range(start,len(arr),gap):
				for j in range(start, i, gap):
					if arr[i] < arr[j]:
						arr.insert(j, arr[i])
						del arr[i+1]
						break
		gap -=1
	return arr

def main(input):
	arr = input.split(',')
	arr = [int(x) for x in arr]
	print(shell_sort(arr))

if __name__ == "__main__":
	main(input())