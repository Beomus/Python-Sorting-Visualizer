# Run time: O(n**2)

def selection(a):
	for i in range(len(a)):
		minIndex = i
		minVal = a[i]
		for j in range(i, len(a)):
			if a[j] < minVal:
				minIndex = j
				minVal = a[j]
			yield a
		if minIndex != i:
			a[i], a[minIndex] = a[minIndex], a[i]
		yield a