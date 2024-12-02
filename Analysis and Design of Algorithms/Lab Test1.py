#Lab 
def q(n,arr)->bool:
    d={}
    d_arr=[]
    for i in range(1,n):
        d[i]=False
    for i in range(1,n):
        ans=arr[i]-arr[i-1]
        ans=-ans if(ans<0) else ans
        if(d.get(ans,None) is None):
            continue
        else:                                                                                                                                               
            d[ans]=True
    for i in d.values():
        if i is False:
            return False     
    return True  
ar=[5,1,4,2,-1,6]
ar1=[5,1,4,2,3]
char='s'
ar2=[]
while(char=='s'):
    ans=(input('o to stop'))
    if ans=='o':
        break
    ar2.append(int(ans))
print(q(len(ar2),ar2))           
