#@PydevCodeAnalysisIgnore


import math

def msort(x):
    if len(x) < 2:
        return x
    result=[]
    mid = int(len(x)/2)
    y = msort(x[:mid])
    z = msort(x[mid:])
    while (len(y) > 0) and (len(z) > 0):
            if y[0] < z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
    result += y
    result += z
    return result

def pack_num(pack,weight):
    pack_count=len(pack)
    pack=msort(pack)                    #merge sort
    print pack
    box_num=pack_count/2+pack_count%2  #at least equal to half of the packs
    ini_list1=pack[:box_num]
    ini_list2=pack[box_num:]
    pos=box_num-1
    while(len(ini_list2)!=0):           # one while loop
        tmp_pack=ini_list2.pop(0)
        if(tmp_pack+ini_list1[pos]<=weight):   #finish a box
              ini_list1.pop(pos)  
              pos=pos-1  
        else:                                  #too big, set a new box
              ini_list1.append(tmp_pack)
              pos=pos+1
              box_num=box_num+1
    msg="box_num: %s" % box_num
    return msg

a=[2,3,5,7]
print pack_num(a, 9)
b=[1,2,3,4,5]
print pack_num(b, 6)
print pack_num(b, 100)
c=[3,3,2,2,5,5,5,5]
print pack_num(c, 5)

                
    