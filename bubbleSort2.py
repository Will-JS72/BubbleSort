
def sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]

array = [64, 34, 25, 12, 22, 11, 90, 
         63, 33, 23, 15, 21, 17, 50, 
         69, 31, 65, 27, 29, 10, 9]

sort(array)

print("Sorted array is: %s" % array)