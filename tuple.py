t5=1,2,3
print(t5)
t6=(5,)
print(type(t6))

numbers=(10,20,30,40,50)
print(numbers[0])
print(numbers[-1])
print(numbers[1:4])

t1=(1,2,3,4,5)
t2=(3,5,6,7,8)
print(t1+t2)
print(t1*2)
print(2 in t1)
print(6 not in t1)
print(len(t1))

#common list of tuple
tuple=(1,2,3,4,4)
print(tuple[0])
print(tuple[-1])
print(tuple[1:3])
print(len(tuple))
print(tuple.count(4))
print(tuple.index(3))
print(max(tuple))
print(min(tuple))
print(sum(tuple))

t=(5,6,7,8,9)
print(max(t))
print(min(t))
print(sum(t))
print(t.count(7))

#packing
person="Alice",25,"Engineer"
name,age,profession=person
print(name)
print(age)
print(profession)

#dictionaries
d1={}
d2={"name":"Alice","age":25,"city":"coimbatore"}
d3={"Name":"meera","age":21,"city":"nagercoil"}
print(d3)
d3=dict(id=101,branch="CSE")
print(d3)
print(d2)
d2=dict(id=100,branch="CSBS")
print(d2)

#nested dictionaries
d4={
    "student":{"name": "Bob","age":22},
    "marks":{"maths":90,"Science":89}
}
print(d4)

d1={}
d2={"name":"Alice","age":25,"city":"coimbatore"}
d3={"Name":"meera","age":21,"city":"nagercoil"}
print(d3)
print(d3["city"])
print(d3["age"])
d3=dict(id=101,branch="CSE")
print(d3)

#remove
d1={}
d2={"name":"Alice","age":25,"city":"coimbatore"}
d3={"Name":"meera","age":21,"city":"nagercoil"}
print(d3)
print(del.d3["age"])