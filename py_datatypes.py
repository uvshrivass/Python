###Program to convert a tuple to list and vice versa.

tuple1 = ("a", "b", "c")
list1 = list(tuple1)
print("The tuple1 is: ", tuple1)
print("The list1 is: ", list1)

list2 = [1,2,3]
tuple2 = tuple(list2)
print("The list2 is: ", list2)
print("The tuple2 is: ", tuple2)

###Program to perform difference, intersection & union operation.

A={"u","j","j","w","a","l"}
B={"s","h","r","i","v","a","s"}
C=set()
print(A|B) #To perfom union operation, use "|".

print(A&B) #To perform intersection, use "&".

print(A-B) #To perform difference, use "-".

###Program to update,delete,clear,remove a set.

set1 = {1,2,3}

set1.add(4) #To add just one item, use "add".
print(set1)

set1.update([5,6]) #To add multiple items, use "update"
print(set1)

set1.remove(6) #To remove any specific item, use "remove".
print(set1) 

set1.pop() #To remove the last item, use "pop"
print(set1)

set1.clear() #To remove all items, use "clear".
print(set1)

#set1.delete() #To delete the entire set, use "delete"
#print(set1)

###Program to find the frequency of characters in a string 
###using dictionary and setdefault method.

sample_str= "mississippi"
freq_dict = {}

for i in sample_str:
    freq_dict[i] = freq_dict.setdefault(i,0)+1
print(freq_dict)