#@PydevCodeAnalysisIgnore
def func(x):
    if (len(x)==0):
        return 0
    if (len(x)==1):
       return [x[0]]
    if (len(x)==2):
       return [x,[x[1],x[0]]]
    else:
       result=[]
       for i in range(len(x)):
         tmp=[x[i]]
         rest=x[:i]+x[i+1:]
         get_back=func(rest)
         for item in get_back:
             tmp=tmp+item
             result.append(tmp)
             tmp=[x[i]]
       return result

a=[1,2,3]
print func(a)
