mylists=["apple","banana","ice apple","cherry"]
print("mylists")
#update
mylists[2]="pineapple"
print("mylists")
#append
mylists.append("blue berry")
print("mylists")
#remove
mylists.remove("apple")
print("mylists")
#loop
for x in mylists:
    print(x)
#list
colours=["blue","orange","yellow","black"]
newlists = []
for x in colours:
    if "a" in colours:
        newlists.append(x)
    print("newlists")
#sort
numbers=[2,1,3,5,6,4]
numbers.sort()
print("numbers")
#copy
detaillist=["sita","ram","hari","harini"]
mylist = detaillist.copy()
print(mylist)
#join
list1=["hi","hlo","how"]
list2=["sita","hari","ram krishna"]
list3=list1+list2
print("list3")
#clear
lists=["house","furniture","chairs"]
lists.clear()
print("lists")