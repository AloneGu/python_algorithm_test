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

def wall_high(wall,m):
    wall=msort(wall)       #merge sort
    print wall
    if(m==0):              #m=0, return the first number after sort
        return wall[0]
    wide=len(wall)
    diff_list=[]
    for i in range(wide-1):
      diff_list.append(wall[i+1]-wall[i])  #get difference of adjacent columns
    tmp_wid=1
    while(m>0):                            #we have bricks
        if(tmp_wid==wide):                 #every column is equal
            wall[wide-1]=wall[wide-1]+m/wide
            return wall[wide-1]
        else:                              #kill the difference from the first
            tmp_add=m
            m=m-diff_list.pop(0)*tmp_wid
            tmp_wid=tmp_wid+1
            if(m==0):
               return wall[tmp_wid-1]
    hight=wall[tmp_wid-2]+tmp_add/(tmp_wid-1)      
    return hight

a=[1,2,6,6,6,6]
print wall_high(a, 5)
b=[1]
print wall_high(b, 100)
c=[1,2,3]
print wall_high(c, 1)     
print wall_high(c, 0)
print wall_high(c, 6)
d=[1,4,2,5,3,6]
print wall_high(d, 5)   