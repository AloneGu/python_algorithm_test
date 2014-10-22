#@PydevCodeAnalysisIgnore
def find_2_line_max(a_input,b_input,map_col): #cost n
    a=[]
    for i in range(map_col):
        a.append(a_input[i]+b_input[i])
    tmp_max1=a[0]
    tmp_max2=a[0]
    index_1=0
    index_2=0
    for i in range(map_col):
        if(a[i]>=tmp_max1):
            tmp_max2=tmp_max1
            tmp_max1=a[i]
            index_2=index_1
            index_1=i
    max=tmp_max1+tmp_max2
    return [max,index_1,index_2]

def find_low_hill(map,map_row,map_col):
    x_combination=[]
    for i in range(map_row):                #cost n^2
        for j in range(i+1,map_row):
            x_combination.append([i,j])
           
    print x_combination
    r=[]
    max_result=[0,0,0]
    for x in x_combination:                 #cost n^3
        max_tmp=find_2_line_max(map[x[0]], map[x[1]], map_col)
        #print max_tmp
        if (max_tmp[0]>max_result[0]):
            max_result=max_tmp
            r=max_result[1:]+x
    print r
    final_result=min(map[r[2]][r[0]],map[r[2]][r[1]],map[r[3]][r[0]],map[r[3]][r[0]])
    return final_result

map=[[1,3,2],[3,2,1],[1,2,3]]
print find_low_hill(map,3,3)  

map2=[[1,1,2,1,2,5],[2,4,1,5,5,2],[1,5,5,1,4,5],[3,1,1,2,3,3]] 
print map2[0]
print find_low_hill(map2, 4, 6)         
a=[1,2,3,4]
b=[6,2,1,4]
print find_2_line_max(a, b, 4)   