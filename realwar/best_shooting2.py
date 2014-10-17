#@PydevCodeAnalysisIgnore

def get_sum(a,pos,m,sum2):
     return sum2+a[pos+m-1]-a[pos-1]
   
def shoot_score2(a,n,m):
    result=max1=0
    if (n>2*m):
        pos_now=0
        for i in range(m):
            max1=max1+a[i]
        sum2=max1        #initial max1 and sum2
            
        temp_queue=[]    #initial queue
        pos_now=pos_now+1
        while(pos_now<=m):
            sum2=get_sum(a,pos_now,m,sum2)
            temp_queue.append(sum2)
            pos_now=pos_now+1
        
        pos_now=pos_now-1
        print "initial queue",temp_queue
        
        result=max1+sum2         #initial result
        
        while(pos_now+m<n):          #when sum2 moves, refresh the max1 and result
          pos_now=pos_now+1
          sum2=get_sum(a,pos_now,m,sum2)
          temp_queue.append(sum2)         
          max1=max(temp_queue.pop(0),max1)   #find the largest sum in the left
          result=max(result,sum2+max1)
                        
        print "result is ",
        return result
    
    else: 
      for i in range(n):
        result=result+a[i]
      print "result is: ",
      return result


a=[1,2,3,3,2,1]
print shoot_score2(a, 6, 2)
print ""
b=[1,2,6,0,5,4,3,4]
print shoot_score2(b,8,3)
print ""
c=[1,2,3,4,5]
print shoot_score2(c, 5, 5)
print ""
d=[1,7,2,9,3,4,5]
print shoot_score2(d,7,1)


