def b_sort(a,n):
  count=0
  for i in range(n):
    for j in range(1,n-i):
      if (a[j]<a[j-1]):
        a[j],a[j-1]=a[j-1],a[j]
        count+=1
  return count

a_Test=[1,3,5,2,4]
print a_Test
len_Test=len(a_Test)
b_sort(a_Test, len_Test)
print a_Test