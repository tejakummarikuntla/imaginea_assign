def subArraySum(arr, n, ssum):
    h = 0
    for i in range(n):
        if arr[i].isdigit():
            h=i
            curr_sum = int(arr[i])
            break
    start = h

    i = start+1
    while i <= n:
        while curr_sum > ssum and start < i-1 and arr[i].isdigit():
            curr_sum = curr_sum - int(arr[start])
            start += 1
        if curr_sum == ssum:
            print("Sum Found between indexes" )
            print("%d and %d" %(start, i-1))
            return 1
        if i < n and arr[i].isdigit():
            curr_sum = curr_sum + int(arr[i])
        i += 1
    print("No subarray found")
    return 0

if __name__ == '__main__':
    arr = "a12b4ccd5ab"
    n = len(arr)
    ssum = 9
    subArraySum(arr, n, ssum)
