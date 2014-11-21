#@PydevCodeAnalysisIgnore
def build_dict(E):
  d={}
  e_l=len(E)
  for i in range(e_l):
    if E[i] in d:
        d[E[i]].append(i+1)
    else:
        d[E[i]]=[i+1]
  print d
  return d

def check_avl(n,E):
    tmp_dict=build_dict(E)
    result=[[0,True] for i in range(n)]
    for i in range(n-1,-1,-1):
        tmp_item=i+1
        if tmp_item not in tmp_dict:
            result[i]=[0,True]
        else:
            if ( len(tmp_dict[tmp_item]) == 2 ):
                tmp=tmp_dict[tmp_item]
                print tmp
                lh,lisb=result[tmp_dict[tmp_item][0]-1]
                rh,risb=result[tmp_dict[tmp_item][1]-1]
                curr_h=max(lh,rh)+1
                curr_flag= lisb and risb and (abs(lh-rh)<=1)
                result[i]=[curr_h,curr_flag]
            else:
                lh,lisb=result[tmp_dict[tmp_item][0]-1]
                curr_h=lh+1
                curr_flag=lisb and (curr_h<=1)
                result[i]=[curr_h,curr_flag]
        if result[i][1]==False:
            return "NO"
    return "YES"

E= [0, 1, 1, 2, 3, 3, 4, 4]
n= 8
print check_avl(n,E)
print check_avl(4, [0,1,2,2])
print check_avl(5, [0,1,1,2,2])