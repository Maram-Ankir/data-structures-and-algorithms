
def insertion_Sort(arr):

    arr_lenght=len(arr)
    for i in range(arr_lenght):
        j=i-1
        temp=arr[i]
        while j>=0 and temp < arr[j]:
            arr[j+1]=arr[j]
            j=j-1
            arr[j+1]= temp
    return arr



print(insertion_Sort([8,4,23,42,16,15]))

