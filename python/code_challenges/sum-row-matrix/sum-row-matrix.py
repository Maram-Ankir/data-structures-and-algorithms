
row=3
col = 3

def row_sum(arr) :
	sum = 0
	print("\nFinding Sum of each row:\n")
	for i in range(row) :
		for j in range(col) :
			sum += arr[i][j]
		print("Sum of the row",i,"=",sum)
		sum = 0

if __name__ == "__main__" :

	row_sum([ [0, 1, 5], [-4, 7, 2], [-3, 12, 11] ])

