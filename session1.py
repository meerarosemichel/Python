#list=[1,2,3,4,5,6,7]
#list1=[1,"saad",9.439279,True,2,3,4,5]
#list2=[[1,2],[3,4],[5.8]]
#print("The length of the list1 is",len(list1))
#print(list[1:7])
#print(list[5::2])
#print(list[5:10])
#print("Access element at 3 index",list[3])

#Append
#list.append(10)
#print(list)
#print(list1)
#wholeNum=[]
#for i in range(21):
   # wholeNum.append(i)
#print(wholeNum)

#insert operation
wholeNum.insert(2,10)
print(wholeNum)

#extend operation
wholeNum.extend([21,22])
print(wholeNum)

#pop operation
list.pop(3)
print(list)

#clear operation
wholeNum.clear()
print(wholeNum)

#index operation
print(list.index(3))

#For loop
fruits=["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)
for i in range(len(fruits)):
    print(fruits[i])
 #while loop
i=0
while i<len(fruits):
    print(fruits[i])
    i+=1

#set operation
#set operation
s1=[1,2,3,4,5,6,7]
print(s1)
s2=[1,2,3,4]
print(s2)
s3={10,"hello",3.14,True}
print(s3)
s4={1,2,2,2,3,3,3}
print(s4)
s1.add(20)
s.add(10)
print(s)
s.update([5,6,34,34])
s.remove(3)
s.discard(10)
print(s)

