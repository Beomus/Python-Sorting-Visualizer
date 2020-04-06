"""
Check through the array if the elements are sorted or not
if not move them down so that they are in a sorted order
It is not good for large array
since it uses nested loops to sort
The runtime is O(n**2)
"""

def insertion_sort_for(arr):
	for i in range(1, len(arr)):
		for j in range(i-1, 0, -1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
			else:
				break


def insertion_sort_while(arr):
	for i in range(1, len(arr)):
		j = i-1
		while arr[j] > arr[j+1] and j >= 0:
			arr[j], arr[j+1] = arr[j+1], arr[j]
			j -= 1
			yield arr
	#return arr

# Best
def insertion_sort_shifting(a):
	for i in range(1, len(a)):
		curNum = a[i]
		for j in range(i-1, 0, -1):
			if a[j] > curNum:
				a[j+1] = a[j]
			else:
				a[j+1] = curNum
				break

if __name__ == "__main__":
	nums = [0 ,1 ,5 ,7 ,9 ,2, 13]
	print(insertion_sort_while(nums))