l=int(input())
ls=[]
if l<15:
    for i in range(l):
        ls.append(int(input()))
    m=max(ls)
    min_num=min(ls)
    sum_num=sum(ls)
    print(sum_num-m-min_num)  
else:
    print("Maximum values")


