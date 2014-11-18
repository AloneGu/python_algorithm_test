#@PydevCodeAnalysisIgnore
import math
def cal_dis(k,b,x,y):
  div=math.sqrt(k*k+1)
  tmp=k*x+b-y
  distance=abs(tmp/div)
  print "[",x,',',y,'] distance:',distance
  return distance

def cal_set_lin(x,y,p,q):
    k=(y-q)/(x-p)
    b=y-k*x
    return [k,b]

def check_3_points(points):
    p=points
    print p
    for i in range(3):
        start=p[0]
        rest=p[1:]
        tmp1=rest[0]
        tmp2=rest[1]
        if(tmp1[0]==tmp2[0]):
            dis=abs(start[0]-tmp1[0])
        else:
            line=cal_set_lin(tmp1[0], tmp1[1], tmp2[0], tmp2[1])
            k=line[0]
            b=line[1]
            dis=cal_dis(k, b, start[0], start[1])
        if(dis<=2):
            return True
        p=p[1:]+[start]
    return False
           
def check_line(points):
     if(len(points)<=2):
       return "YES"
     points_num = len(points)
     for i in range(points_num-2):
         for j in range(i+1,points_num-1):
             for k in range(j+1,points_num):
                 tmp_points=[points[i],points[j],points[k]]
                 if(check_3_points(tmp_points)==False):
                     return "NO"
     return "YES"
     

p=[[2,2],[1,0],[-1,0],[0,-1]]
print check_line(p)
p2=[[1,1],[0,0.5],[-4,0]]
print check_line(p2)
p3=[[0,2],[0,-2],[3,0]]
print check_line(p3)
