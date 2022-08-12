list1=[1,5,6,3,4,78,9,65]
# list2=[]
# for i in list1:
#     if i%2==0:
#         list2.append(i)
# list2.sort()
# print(list2)
list2=[i for i in list1 if i%2==0 ]
print(list2)