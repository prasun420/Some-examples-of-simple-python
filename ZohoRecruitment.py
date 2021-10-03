st='QUERY'
l1=[]
l2=[]
mid=int(len(st)/2)
for i in range(mid,len(st)):
    l1.append(st[mid:i+1])

for i in range(0,mid):
    l2.append(l1[-1]+st[0:i+1])
l3=l1+l2
for i in l3:
    print(i+'$')

  