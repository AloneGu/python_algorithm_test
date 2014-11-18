#@PydevCodeAnalysisIgnore
def get_adj(n,E):
    adj={}
    for item in E:
        if( item[0] in adj ):
            adj[item[0]].append(item[1])
        else:
            adj[item[0]]=[item[1]]
    print adj
    return adj

def diameter(n,E):
    tree_adj=get_adj(n, E)
    tmp_max=0
    result=[[0,0] for i in range(n)]
    for i in range(n-1,-1,-1):
        if i+1 not in tree_adj:
            result[i]=[0,0]
        else:
            if(len(tree_adj[i+1])==1):
                tmp_a=tree_adj[i][0]
                result[i]=[result[tmp_a-1][0]+1,0]
                tmp_max=max(tmp_max,result[i][0]+result[i][1])
            else:
                tmp_adj=tree_adj[i+1]
                for j in tmp_adj:
                    if( result[j-1][0]+1>=result[i][0]):
                        result[i][1]=result[i][0]
                        result[i][0]=result[j-1][0]+1
                    elif(result[j-1][0]+1>=result[i][1]):
                        result[i][1]=result[j-1][0]+1
                    else:
                        continue
                tmp_max=max(tmp_max,result[i][0]+result[i][1])
    return tmp_max   
                                  
n=7
E=[(1,2),(1,3),(1,4),(2,5),(3,6),(3,7)]
print diameter(n, E)
