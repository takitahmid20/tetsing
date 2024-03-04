def money(arr, n, sum):
    if(sum==0):
        return 0
    if(sum<0):
        return 0
    if(sum<=0):
        return 0
    
    return money(arr, n-1, sum)+money(arr, n, sum-arr[n-1])

arr = [1,2,5,10,20,50,100,200,500,1000]
n = len(arr)
money(arr, n, 20)




