nums_list=[10,20,40,30,60]

print(nums_list)
print(type(nums_list))
print(len(nums_list))

print(max(nums_list))
print(min(nums_list))
print(sum(nums_list))

nums_list.append(10)
print(nums_list)

list2=[70,90,80]
nums_list.extend(list2)
print(nums_list)

nums_list.insert(2,30)
print(nums_list)

nums_list.remove(30)
print(nums_list)

nums_list.pop()
print(nums_list)

list2.clear()
print(list2)

print(nums_list.index(60))

print(nums_list.count(30))

nums_list.sort()
print(nums_list)

ages_list=[21,34,56,12,32,46,45,50]
print(ages_list)
sorted_ages=sorted(ages_list)
print(sorted_ages)

fruits_list=['apple','grapes','banana','orange','guava']
print(fruits_list)
fruits_list.reverse()
print(fruits_list)

vegies_list=['carrot','brinjal','bottle guard','drum stick','beet root']
dup_vegies=vegies_list.copy()
print(vegies_list)

print(dup_vegies)


cubes=[x**3 for x in range(1,10)]
print(cubes)
