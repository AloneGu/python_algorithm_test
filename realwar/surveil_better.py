#@PydevCodeAnalysisIgnore
def msort(x):
    if len(x) < 2:
        return x
    result=[]
    mid = int(len(x)/2)
    y = msort(x[:mid])
    z = msort(x[mid:])
    while (len(y) > 0) and (len(z) > 0):
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
    result += y
    result += z
    return result

def binary_sort(a,low,high,x):
    if(high==low):
        return low   
    mid=(high+low)/2
    if(x>=a[mid]):
        return binary_sort(a, mid+1, high, x)
    else:
        return binary_sort(a, low, mid, x)

def binary_sort2(a,low,high,x):
    if(high==low):
        return low   
    mid=(high+low)/2
    if(x>a[mid]):
        return binary_sort2(a, mid+1, high, x)
    else:
        return binary_sort2(a, low, mid, x)
    
def count_camera(n,cam,m,load_pos):
    list1=[]
    list2=[]
    result=[0 for i in range(m)]
    for i in range(n):
        list1.append(cam[i][0])
        list2.append(cam[i][1])
    list1=msort(list1)
    list2=msort(list2)
    print list1
    print list2
    tmp_pos=0 
    while(tmp_pos<m):
      result[tmp_pos]=result[tmp_pos]+binary_sort(list1,0,n,load_pos[tmp_pos])-binary_sort2(list2,0,n,load_pos[tmp_pos])
      tmp_pos=tmp_pos+1
    return result

cam=[[2,5],[2,6],[4,8],[7,11]]
road=[3,4,6.5,12]
print count_camera(4, cam, 4, road)
print ""
road2=[3,6.5,12,4]
print count_camera(4, cam, 4, road2)
print ""
cam3=[[1,5],[2,3],[3,4]]
road3=[6,5,4,3,2,1,0]
print count_camera(3, cam3, 7, road3)