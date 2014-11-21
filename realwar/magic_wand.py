#@PydevCodeAnalysisIgnore
def check_grid(x,y,k,image):
    return (abs(image[x][y]-start_val)<=k)

def dfs_visit(x,y,k,image,m,n):
    global flag_map
    if(flag_map[x][y]==1):
        x_1=x-1
        x_2=x+1
        y_1=y-1
        y_2=y+1
        if(x_1>=0):
            if(check_grid(x_1, y, k,image)==True and flag_map[x_1][y]==0):
                flag_map[x_1][y]=1
                dfs_visit(x_1, y, k, image, m,n)
        if(x_2<=n-1):
            if(check_grid(x_2, y, k,image)==True and flag_map[x_2][y]==0):
                flag_map[x_2][y]=1
                dfs_visit(x_2, y, k, image, m,n)
        if(y_1>=0):
            if(check_grid(x, y_1, k,image)==True and flag_map[x][y_1]==0):
                flag_map[x][y_1]=1
                dfs_visit(x, y_1, k, image,  m, n)
        if(y_2<=m-1):
            if(check_grid(x, y_2, k, image)==True and flag_map[x][y_2]==0):
                flag_map[x][y_2]=1
                dfs_visit(x, y_2, k, image,  m, n)
        
            
def magic_wand(n,m,k,image,start_p):
    tmp_count=0
    global flag_map
    flag_map=[]
    for i in range(n):
        flag_map.append([0 for j in range(m)])
    x=start_p[0]
    y=start_p[1]
    global start_val
    start_val=image[x-1][y-1]
    flag_map[x-1][y-1]=1
    dfs_visit(x-1,y-1,k,image,m,n)
    for x in flag_map: print x
    tmp_count=sum([sum(item) for item in flag_map])
    return tmp_count

n=3
m=3
k=2
start_p=[2,2]
image=[[1,5,3],[4,1,2],[1,3,1]]
print magic_wand(n, m, k, image, start_p)

image_2=[
[0 ,0, 0, 1, 1, 1, 0, 1],
[0 ,1, 3, 1, 5, 0, 1, 0],
[0 ,1 ,7 ,7 ,7, 6, 1, 0],
[0 ,1, 5, 6, 6, 6, 5, 2],
[1 ,0 ,1 ,2 ,2 ,4 ,3 ,3],
[1 ,1, 0, 1, 2, 3, 3, 2]]
 
print magic_wand(6, 8, 4, image_2, [3,4])