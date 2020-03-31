
def arrAdd(arr1, num):
    length = len(arr1)
    #count is used as a place value finder for num and the loop help
    #us determine where to do the addition in the array
    var = num
    while(var > 1):
        var = var / 10
        length = length - 1
    arr1[length] = (var * 10) + arr1[length]
    print(arr1)

