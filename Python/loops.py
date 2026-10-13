list_a=[2,1,4,2,5]
for i in range(len(list_a)):
    for j in range(len(list_a)):
        if(list_a[i]<list_a[j]):
            list_a[i],list_a[j]=list_a[j],list_a[i]

print(list_a)