def bubble_sort(a):
    for i in range(0, len(a) - 1):
        for j in range(0, len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                yield a

if __name__ == "__main__":
	myList = [3, 4, 7, 1, 2, 4, 9, 2, 0]
	print(bubble_sort(myList))


# check git