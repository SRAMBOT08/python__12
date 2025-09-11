def ins(arr):
  n =len(arr)
  for i in range(1,n):
    key = arr[i]
    j = i - 1 
    while j >= 0 and key < arr[j]:
      arr[j+1] = arr[j]
      j = j-1
    arr[j+1] = key
  return arr
arr = (list(map(int,input().split())))
print(ins(arr))
