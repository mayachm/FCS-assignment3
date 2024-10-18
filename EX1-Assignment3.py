def mybinary(l,high,low,m):
    l.sort()

    mid=(low+high)//2
    if low>high:
        return "incorrect"

    elif l[mid]==m:
        return m
    elif l[mid]<m:
        return mybinary(l,high,mid+1,m)
    else:
         return mybinary(l,mid-1,low,m)
l=[1,5,3,6,8]
mybinary(l,len(l)-1,l[0],5)