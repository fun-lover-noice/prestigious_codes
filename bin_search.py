def bin_search(arr,n):
    l=0
    u=len(arr)-1
    while l<=u:
        mid=(l+u)//2
        if arr[mid]==n:
            print('found')
            break
        elif arr[mid]>n:
            u=mid-1
        elif arr[mid]<n:
            l=mid+1
    if l>u:
        print('not found')
arr=[10,20,30,40,50]
bin_search(arr,40)