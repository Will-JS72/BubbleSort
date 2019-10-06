TestArray = [6,4,8,2,6,8,4,9,6,5,7]
def bubble(array):
    arraylength = len(array)
    for i in range(arraylength - 2):
        for j in range(arraylength - i -2):
            if array[j] > array[j+1]:
                swapping = array[j]
                array[j] = array[j+1]
                array[j+1] = swapping
        print(array)
    print("the final array is" + str(array))


bubble(TestArray) 
