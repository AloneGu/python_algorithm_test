def shoot_score(a,n,m):
    max=0
    if n>m:
     score=0
     for j in range(m):
         score=score+a[j]
     max = score
     for i in range(m,n):
        score=score+a[i]-a[i-m]
        if(score>max):
           max=score
    else:
       for i in range(0,n):
          max=max+a[i]
    return max
 
a=[1,2,3,3,2,1]
print shoot_score(a,6,2)
 
b=[1,2,6,0,5,4,3,4]
print shoot_score(b,8,3)
 
c=[1,2,3,4,5]
print shoot_score(c,5,5)