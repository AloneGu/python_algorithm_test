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

def msort1(x):                       #sort by index
    if len(x) < 2:
        return x
    result=[]
    mid = int(len(x)/2)
    y = msort1(x[:mid])
    z = msort1(x[mid:])
    while (len(y) > 0) and (len(z) > 0):
            if y[0][0] > z[0][0]:      #compare index
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
    result += y
    result += z
    return result
 
def msort2(x):                       #sort by value
    if len(x) < 2:
        return x
    result=[]
    mid = int(len(x)/2)
    y = msort2(x[:mid])
    z = msort2(x[mid:])
    while (len(y) > 0) and (len(z) > 0):
            if y[0][1] > z[0][1]:      #compare value
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
    result += y
    result += z
    return result
 
def count_camera(n,cam,m,load_pos):
    list1=[]
    list2=[]
    result=[0 for i in range(m)]
    for i in range(n):
        list1.append(cam[i][0])
        list2.append(cam[i][1])
    list1=msort(list1)
    list2=msort(list2)
    tmp_record_index=[]
    for i in range(m):
        tmp_record_index.append([i,load_pos[i]])
   # print tmp_record_index
    tmp_record_index=msort2(tmp_record_index)
    print tmp_record_index
    load_pos=msort(load_pos)
    #print list1
    #print list2
    #print load_pos
    tmp_pos=tmp_left=tmp_right=0
    while (tmp_pos<m):
        if(tmp_left==n):
            result[tmp_pos]=result[tmp_pos]+tmp_left
            tmp_pos=tmp_pos+1
        elif(load_pos[tmp_pos]>=list1[tmp_left]):
            tmp_left=tmp_left+1
        else:
            result[tmp_pos]=result[tmp_pos]+tmp_left
            tmp_pos=tmp_pos+1
    #print "add num:",result
    tmp_pos=0
    result2=[]
    while(tmp_pos<m):
        if(tmp_right==n):
            result[tmp_pos]=result[tmp_pos]-tmp_right
            result2.append((0-tmp_right))
            tmp_pos=tmp_pos+1
        elif(load_pos[tmp_pos]>list2[tmp_right]):
            tmp_right=tmp_right+1
        else:
            result[tmp_pos]=result[tmp_pos]-tmp_right
            result2.append((0-tmp_right))
            tmp_pos=tmp_pos+1
    #print "cut num:",result2
    #print "sorted result:",result
    tmp_result=[]
    final_result=[]
    for i in range(m):
        tmp_result.append([tmp_record_index[i][0],result[i]])
    print "tmpresult",tmp_result
    tmp_result=msort1(tmp_result)
    print "sort tmp",tmp_result
    for i in range(m):
        final_result.append(tmp_result[i][1])
    return final_result

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