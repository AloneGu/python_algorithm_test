#@PydevCodeAnalysisIgnore

global count_num
count_num=0              #the number of intersections

def msort(x):            #cost O(nlogn)
    global count_num
    if len(x) < 2:
        return x
    result=[]
    mid = int(len(x)/2)
    y = msort(x[:mid])
    z = msort(x[mid:])
    tmp_len=len(z)
    while (len(y) > 0) and (len(z) > 0):
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)                         
            else:
                result.append(y[0])
                y.pop(0)
                count_num+=(tmp_len-len(z)) #find intersection for this line  
    result += y
    result += z
    count_num+=len(y)*tmp_len               #if y is not empty, add count_num.
    return result

def find_intersection(x):
    global count_num
    print msort(x)
    return count_num

a=[2,5,1,6,4,3]
print find_intersection(a)
count_num=0
b=[1,4,2,5,3,6]
print find_intersection(b)
count_num=0
c=[1,2,3,4]
print find_intersection(c)
count_num=0
d=[3,2,1]
print find_intersection(d)
count_num=0
e=[4,5,6,1,2,3]
print find_intersection(e)