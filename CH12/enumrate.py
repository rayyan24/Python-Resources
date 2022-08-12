list1=['Rayyan',"Affan","Zia","Sheza",False,1,5,6,3,4]
# item_no=1
# for i in list1:
#     print(f"{item_no}-{i}")
#     item_no+=1
for i,j in enumerate(list1):
    if i==0:
        continue
    print(i,j)