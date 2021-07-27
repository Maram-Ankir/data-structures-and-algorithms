def BinarySearch(arr,val):
  for i in arr :
    midVal =int((0+len(arr)-1)/2)
    if val==arr[midVal] :
        print('val found in index',midVal)
        break
    if val>arr[midVal]:
       midVal=int((midVal+len(arr)-1)/2)
    elif val==arr[midVal] :
        print('val found in index',midVal)
        break
    if val< arr[midVal]:
       midVal=int(midVal/2)
    if val==arr[midVal] :
        print('val found in index',midVal)
        break
    else :
        print('val not exist in this arr',-1)
        break
BinarySearch([1, 2, 3, 5, 6, 7], 4)
